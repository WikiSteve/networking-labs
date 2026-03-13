# Got Root?

The root account is a liability if it remains directly usable all the time. Before disabling it again, we need to install `sudo` and make sure a normal user has administrative access.

![Decorative slide image introducing the sudo configuration section.](assets/images/file-62bd1979e9988.png)

## Configuring Sudo

First, make sure `sudo` is installed:

```bash
apt install sudo
```

![`apt install sudo` output showing the sudo package being installed on Debian.](assets/images/file-62bd1af1800b1.png)

During the Debian install you may have done one of two things:

1. chosen a username and password at random
2. used your first name as the regular username

If you used a different name earlier, make sure you know that username and its password. If needed, you can reset that user's password with:

```bash
passwd <username>
```

To create a new user, use the Perl wrapper script `adduser`.

![`adduser bbunny` creating a new regular account and home directory.](assets/images/file-62bd1c2312e51.png)

Verify that the `sudo` group exists before continuing. Many distributions use the name `wheel`, but Debian-based systems such as Debian, Ubuntu, and Mint typically use `sudo`.

![`grep sudo /etc/group` confirming that the `sudo` group exists on the system.](assets/images/file-62bd1d5dd40c6.png)

As shown below, the regular user does not yet have sudo access.

![`id steve` output showing the regular user before being added to the `sudo` group.](assets/images/file-62bd1f501854b.png)

To add the user:

- `-a` means append; without it you could overwrite the user's current supplementary groups
- `-G` uppercase means supplementary groups; lowercase `-g` would change the primary group

![`usermod -aG sudo steve` followed by `id steve`, proving the user now belongs to the `sudo` group.](assets/images/file-62bd2132c6bf8.png)

## Screenshot 3

Prove that your user now has sudo access.

![Regular user shell showing the command used to disable the root account with `sudo usermod -L root`.](assets/images/file-62bd2352e15b6.png)

## Screenshot 4

Prove that root was disabled. The screenshot must include the `!` after `root` in `/etc/shadow`, which shows the account has been locked.

![`sudo grep root /etc/shadow` output showing the locked root entry beginning with `!`.](assets/images/file-62bd276fda97b.png)

---
[Prev](02_let-me-in.md) | [Home](README.md)
