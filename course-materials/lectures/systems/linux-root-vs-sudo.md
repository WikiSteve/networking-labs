# Linux Root vs sudo

- Filename: `Linux root vs sudo.pptx`
- Subject: `systems`
- Type: `lecture`
- Reusable: `yes`
- Source file: [Source copy](../../sources/Linux%20root%20vs%20sudo.pptx)

## Summary

This reusable Linux security and administration lecture deck teaches the practical difference between recovering or using the root account directly and performing privileged work through `sudo`. It begins by reviewing classic Unix and Linux runlevels, especially runlevel 1 as single-user maintenance mode and the special shutdown and reboot runlevels, then explains how boot-loader changes can be used to enter single-user mode even when the root account is disabled. From there it moves into recovery techniques using `chroot`, including mounting a damaged system from a live Linux environment and resetting passwords for root or other users.

## Key Details

- Reviews classic runlevels, including `init 0` for shutdown, `init 6` for reboot, `runlevel 1` for single-user maintenance mode, and `2-5` for multi-user operation, while noting that Debian treats `2-5` the same.
- Explains that systems normally boot into multi-user mode, but changing boot-loader options can force a boot into single-user mode for maintenance or recovery.
- Notes that even when the root account is disabled, single-user mode often still permits recovery without a password prompt.
- Introduces `chroot` as a recovery method using a live Linux ISO, with steps to mount the target root filesystem, run `chroot <mountpoint>`, and then use `passwd root` or `passwd user`.
- Asks how to defend against unauthorized single-user recovery and answers with GRUB password protection.
- Expands the physical security discussion to alternate boot devices, BIOS boot-order changes, and direct drive removal.
- Identifies full-disk encryption as the real defense against offline password-reset attacks when someone can remove the system drive.
- Includes a lab where the reader must boot into single-user mode and reset the root password without being told the existing one.
- Explains why root SSH login should be denied or the root account disabled, especially on public-facing systems.
- Distinguishes `su` from `sudo`, explaining that `su` switches identity while `sudo` runs a command as another user, usually root.
- Makes the accountability case for `sudo`, stressing that it records who used elevation and what they ran.
- Includes a second lab requiring the reader to install `sudo`, grant a user sudo rights, and secure the system by disabling root afterward.

## Tags

- `linux`
- `root`
- `sudo`
- `single-user-mode`
- `chroot`
- `grub`
- `full-disk-encryption`
- `privilege-escalation`
