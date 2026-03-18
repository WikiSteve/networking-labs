# Linux and SSH Challenge

- Filename: `Linux and SSH Challenge.pdf`
- Subject: `security`
- Type: `challenge`
- Reusable: `yes`
- Source file: [Source copy](../../sources/Linux%20and%20SSH%20Challenge.pdf)
- Submission template: [Linux and SSH Challenge Submission Template](../../templates/security/linux-and-ssh-challenge-submission-template.md)

## Summary

This reusable challenge guide focuses on Linux and SSH administration tasks. It requires one submission document containing five screenshots, each with a visible timestamp from either the `date` command or the system clock. The challenge covers steganography with `steghide`, SSH public key authentication using PuTTY, X11 forwarding with `xeyes`, inspection of SSH host and user key files and permissions, and SSH hardening through the `AllowUsers` directive in `sshd_config`. The learning goals are hands-on command execution, key-based remote access, GUI forwarding over SSH, understanding the difference between server and user keys, and basic SSH access control and service management.

## Key Details

- The challenge requires a single document containing five screenshots with a visible timestamp in each.
- Screenshot 1 uses the provided challenge image and `steghide` to embed the text `challenge complete` with the password `ssh-is-secure`.
- Screenshot 2 requires PuTTY SSH login using a private key and a themed username based on a favorite musician or band.
- The private key comment must be set to `First Name's CHALLENGE key`.
- Successful SSH login proof must include the `date` output immediately after login.
- Screenshot 3 tests X11 forwarding by running `xeyes` from the SSH session while keeping the terminal visible.
- Screenshot 4 compares SSH host keys and user key files, including file details and permissions.
- Screenshot 5 hardens SSH with an `AllowUsers` line in `/etc/ssh/sshd_config`, restarts `sshd`, and proves an unauthorized login fails.
- The final screenshot must show both a failed PuTTY login attempt and a successful approved-user session.
- The challenge names the main tools explicitly: `steghide`, PuTTY, SSH keys, X11 forwarding, `xeyes`, `nano`, `sshd_config`, and `systemctl`.

## Tags

- `challenge`
- `ssh`
- `putty`
- `steghide`
- `x11-forwarding`
- `ssh-keys`
- `ssh-hardening`
- `linux`
