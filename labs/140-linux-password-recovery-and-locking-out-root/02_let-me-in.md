# Let Me In

Right now you should not have normal administrative access to your Linux machine, because neither the root password nor the regular user path is set up the way this lab needs.

![Decorative penguin image introducing maintenance mode.](assets/images/file-62bcfa31ea5b5.png)

## Single-User Mode

Single-user mode, sometimes called maintenance mode, is handled slightly differently across Linux distributions. Older systems often accepted the `single` keyword directly, while newer GRUB setups usually require you to edit the kernel boot line.

Boot the VM and press `Esc` when the bootloader appears so GRUB stops at the menu.

![GRUB boot menu for Debian, shown before entering the editor.](assets/images/file-62bcfc4095728.png)

Press `e` to open the GRUB editor.

![GRUB editor showing the boot entry before modifying the kernel command line.](assets/images/file-62bd024f6d203.png)

Locate the Linux boot line and replace `ro quiet` with `single init=/bin/bash`.

![GRUB editor focused on the kernel line where `ro quiet` is still present.](assets/images/file-62bd032045e53.png)

![GRUB editor after changing the kernel parameters to `single init=/bin/bash`.](assets/images/file-62bd048a0b933.png)

After making the change, press `Ctrl+X` to boot into single-user mode.

## Screenshot 1

![Single-user boot output showing the system entering maintenance mode and prompting for recovery actions.](assets/images/file-62bd0613b4f5c.png)

Your screenshot must include both highlighted portions.

## Why Did the Password Not Change?

The root filesystem is mounted read-only in this mode.

![Root shell output showing the read-only mount state in single-user mode.](assets/images/file-62bd0a4454df6.png)

Remount the root filesystem read-write with:

```bash
mount -o remount,rw /
```

![Root shell output showing the remount command followed by a successful `passwd` change.](assets/images/file-62bd0bcceac56.png)

The password change should succeed after that.

## Screenshot 2

![Root shell output showing `passwd` reporting success and `/etc/passwd` listing the regular user created during the Debian install.](assets/images/file-62bd0d1042faa.png)

Your screenshot must show:

- that the password was updated successfully
- the regular user account created during the Debian install

Type `exit` and the system will likely panic because it was booted into this recovery shell directly. Use the VMware reset option, then log in with your new password.

---
[Prev](01_evaluation.md) | [Home](README.md) | [Next](03_got-root.md)
