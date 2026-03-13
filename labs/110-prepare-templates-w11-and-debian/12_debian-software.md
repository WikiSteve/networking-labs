# Debian Software

Install the following baseline software on the Debian template:

- SSH server
- `net-tools`
- Firefox ESR

### Install Debian Without a Graphical Interface

Install Debian without selecting a graphical user interface. This keeps the template lean and predictable for later labs.

### Verify and Install SSH

SSH is essential for remote access to the Debian template.

1. Check whether `openssh-server` is already installed:

```bash
dpkg -l | grep openssh-server
```

If SSH is installed, you should see output similar to:

```text
ii  openssh-server      1:9.2p1-2+deb12u3
```

2. If SSH is not installed, install it:

```bash
sudo apt update
sudo apt install openssh-server
```

3. Start the service and enable it at boot:

```bash
sudo systemctl start ssh
sudo systemctl enable ssh
sudo systemctl status ssh
```

You should see an active `(running)` status.

### Install and Verify `net-tools`

`net-tools` provides legacy networking commands such as `ifconfig`.

1. Install `net-tools`:

```bash
sudo apt install net-tools
```

2. Verify the installation:

```bash
ifconfig
```

Expected output will show your network interfaces, similar to:

```text
eth0: flags=4163  mtu 1500
inet 192.168.1.10 netmask 255.255.255.0 broadcast 192.168.1.255
inet6 fe80::a00:27ff:fe4e:66a1 prefixlen 64 scopeid 0x20
...
```

### Test SSH Access

Confirm that SSH works by connecting to the local machine:

```bash
ssh user@localhost
```

Expected behavior:

- You should be prompted for a password.
- After entering the correct password, you should get a shell on the Debian system.

### Install Firefox ESR

Firefox on Debian is packaged as `firefox-esr`.

```bash
sudo apt install firefox-esr
```

---
[Prev](11_w11-software.md) | [Home](README.md) | [Next](13_debian-naming.md)
