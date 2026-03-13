# Sudo Password

In production, you would normally require a user password every time `sudo` is used. In this academic lab environment, constantly retyping that password is mostly just typing practice, so this section changes `sudo` so it does not prompt.

The file `/etc/sudoers` controls `sudo`. If you make a mistake in that file, you can lock yourself out of administrative access, so do not edit it directly. Instead, use `visudo`, which validates the syntax before saving.

Run `visudo` and find the line shown below:

![`/etc/sudoers` open in `visudo`, showing the `%sudo ALL=(ALL:ALL) ALL` rule for members of the sudo group.](assets/images/file-62cdee5c9b4c3.png)

That line means:

- members of the `sudo` group may use `sudo`
- they may run any command
- they may do so on any host
- the last `ALL` portion controls whether a password is required

Add `NOPASSWD:` in front of the final `ALL` so the rule becomes `NOPASSWD:ALL`.

![`/etc/sudoers` after editing the sudo-group rule so it uses `NOPASSWD:ALL`.](assets/images/file-62cdef2973ea3.png)

Log out and back in again. Then test a command with `sudo` and confirm it no longer prompts for your password.

![SSH session showing a successful login and a `sudo` command that runs without prompting for a password.](assets/images/file-62cdf0cc48fe4.png)

## Screenshot 1

Your screenshot must include your login information and show that you can run `echo` with `sudo` without being prompted for a password. Include a good computer joke in quotation marks.

---
[Prev](01_evaluation.md) | [Home](README.md) | [Next](03_shuffling-space.md)
