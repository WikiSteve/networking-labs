# Linux Root and Single User Mode

- Filename: `Linux Root and single user mode.pptx`
- Subject: `systems`
- Type: `lecture`
- Reusable: `yes`
- Source file: [Source copy](../../sources/Linux%20Root%20and%20single%20user%20mode.pptx)

## Summary

This reusable Linux lecture deck covers root recovery, init or systemd basics, GRUB boot-parameter editing, terminal management, and the difference between physical terminals and pseudoterminals. It starts by reviewing an earlier root-password recovery workflow in single-user mode, including editing GRUB, remounting the root filesystem read-write, recalculating a password hash, and updating `/etc/shadow`. From there it shifts into what `init` really is on modern Debian systems, using `ps`, `pstree`, `lsof`, and symbolic links to show that `/usr/sbin/init` is a legacy symlink to `systemd`, which actually controls the system's startup and many core services.

## Key Details

- Reviews a prior root-recovery task done from single-user mode, including editing GRUB, remounting `/` as read-write, recalculating a password hash, and storing it in `/etc/shadow`.
- Explains that the historical first process is `init` with PID 1, then clarifies that on this Debian-style system `init` is really a symlink and the actual process in memory is `systemd`.
- Uses `ps`, `pstree`, and `lsof` as a teaching comparison, showing how each command reveals different views of processes and opened files.
- States that `systemd` controls major system behavior, including spawning getty sessions and managing services.
- Breaks down GRUB kernel-line edits, especially replacing `ro quiet` with `single init=/bin/bash`, and explains how that changes boot behavior for recovery.
- Includes an argument against `quiet` on servers because suppressing boot messages makes startup failures harder to troubleshoot at the console.
- Has the reader remove `quiet` from boot configuration using `sudo` and an editor, then reboot to observe more visible kernel and systemd messages.
- Introduces `getty` or `agetty` as the mechanism that creates physical console logins and ties that to the Linux TTY model.
- Includes an activity to create extra user accounts, then log into multiple local consoles so readers can see `tty1`, `tty2`, and `tty3` in use.
- Teaches console switching with Alt+function keys and the Ctrl+Alt+function key variation when a graphical desktop is running.
- Ends by distinguishing local physical terminals like TTYs from remote pseudoterminals such as `pts`.
- Uses SSH versus Telnet as a brief framing example for pseudoterminals.

## Tags

- `linux`
- `systemd`
- `init`
- `grub`
- `single-user-mode`
- `tty`
- `pts`
- `root-recovery`
