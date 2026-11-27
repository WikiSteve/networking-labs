#include <arpa/inet.h>
#include <errno.h>
#include <netinet/in.h>
#include <poll.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

static int copy_streams(int client, int upstream)
{
    struct pollfd streams[2] = {{client, POLLIN, 0}, {upstream, POLLIN, 0}};
    int peers[2] = {upstream, client};
    char buffer[16384];

    while (streams[0].fd >= 0 || streams[1].fd >= 0) {
        if (poll(streams, 2, -1) < 0) {
            if (errno == EINTR)
                continue;
            return 1;
        }
        for (int i = 0; i < 2; i++) {
            if (!streams[i].revents)
                continue;
            ssize_t count = read(streams[i].fd, buffer, sizeof(buffer));
            if (count < 0)
                return 1;
            if (!count) {
                shutdown(peers[i], SHUT_WR);
                streams[i].fd = -1;
                continue;
            }
            for (ssize_t offset = 0; offset < count;) {
                ssize_t sent = write(peers[i], buffer + offset, count - offset);
                if (sent <= 0)
                    return 1;
                offset += sent;
            }
        }
    }
    return 0;
}

static int serve(int client, const struct sockaddr_in *target)
{
    int upstream = socket(AF_INET, SOCK_STREAM, 0);
    if (upstream < 0)
        return 1;
    if (connect(upstream, (const struct sockaddr *)target, sizeof(*target)) < 0)
        return 1;
    return copy_streams(client, upstream);
}

int main(int argc, char **argv)
{
    struct sockaddr_in target = {.sin_family = AF_INET};
    struct sockaddr_in6 local = {.sin6_family = AF_INET6, .sin6_port = htons(80)};
    if (argc != 3 || inet_pton(AF_INET, argv[1], &target.sin_addr) != 1 ||
        !argv[2][0] || strspn(argv[2], "0123456789") != strlen(argv[2])) {
        fputs("Expected an IPv4 address and TCP port.\n", stderr);
        return 2;
    }
    long port = strtol(argv[2], NULL, 10);
    if (port < 1 || port > 65535) {
        fputs("Upstream TCP port must be 1–65535.\n", stderr);
        return 2;
    }
    target.sin_port = htons((unsigned short)port);
    inet_pton(AF_INET6, "fd00:1ab:5::102", &local.sin6_addr);
    signal(SIGCHLD, SIG_IGN);
    signal(SIGPIPE, SIG_IGN);
    int server = socket(AF_INET6, SOCK_STREAM, 0);
    int enabled = 1;
    if (server < 0 ||
        setsockopt(server, SOL_SOCKET, SO_REUSEADDR, &enabled, sizeof(enabled)) < 0 ||
        setsockopt(server, IPPROTO_IPV6, IPV6_V6ONLY, &enabled, sizeof(enabled)) < 0)
        return 1;
    while (bind(server, (struct sockaddr *)&local, sizeof(local)) < 0) {
        if (errno != EADDRNOTAVAIL) {
            perror("bind");
            return 1;
        }
        sleep(2);
    }
    if (listen(server, 32) < 0)
        return 1;
    for (;;) {
        int client = accept(server, NULL, NULL);
        if (client < 0) {
            if (errno == EINTR)
                continue;
            return 1;
        }
        if (fork() == 0) {
            close(server);
            _exit(serve(client, &target));
        }
        close(client);
    }
}
