# Mode: setuid

## setuid

The `setuid` bit on an executable means the program runs with the effective user ID of the file owner instead of the user who launched it.

One of the standard examples is `passwd`:

![`ls -l /usr/bin/passwd` showing the setuid bit in the owner execute position.](assets/images/file-62d75a8c76e97.png)

In a long listing, you can spot `setuid` by a lowercase `s` where you would normally expect the owner's execute bit to appear. If the owner execute bit is not set, you will see an uppercase `S` instead.

### Practice check

The `passwd` command needs `setuid` because the password hashes are stored in `/etc/shadow`, which is writable only by `root`.

---
[Prev](06_mode-standard.md) | [Home](README.md) | [Next](08_mode-setgid.md)
