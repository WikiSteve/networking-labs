# Groups

## /etc/group

[Group identifier](https://en.wikipedia.org/wiki/Group_identifier)

Groups in Linux are similar to groups in Windows, with one major difference: Linux groups do not contain other groups.

The following rules apply:

1. Every user has exactly one primary group.
2. A user may also belong to zero or many supplemental groups.

Looking at `/etc/group` shows both human groups and service groups. Those service groups let administrators grant limited access without giving away full root privileges.

To see who currently has `sudo` access, run:

```bash
grep sudo /etc/group
```

![`grep sudo /etc/group` output showing which users currently belong to the `sudo` group.](assets/images/file-62d61b4f7ec36.png)

In the example, `steve` and `dduck` are in the `sudo` group.

To add another user to `sudo`, use:

```bash
sudo usermod -aG sudo batman
```

The important flags are:

- `-a` means append; without it, you risk replacing the user's existing supplementary groups
- `-G` means supplementary groups; lowercase `-g` would change the primary group

![Terminal output showing `sudo usermod -aG sudo batman`, followed by `id batman` and `grep sudo /etc/group` to verify the change.](assets/images/file-62d61c6451d01.png)

### Create a Group

```bash
groupadd <groupname>
```

### login.defs Reference

Using `/etc/login.defs`, the lecture's GID defaults are:

```text
GID_MIN     1000
GID_MAX    60000
#SYS_GID_MIN 100
#SYS_GID_MAX 999
```

---
### 🧠 Anyone can view /etc/group?

> [!NOTE]
> **Statement:** Anyone can view `/etc/group`.
>
> - [ ] True
> - [ ] False

<details>
<summary>👉 <b>Reveal answer</b></summary>

**Correct:** True
</details>

---

## Video Walkthrough

### 🎥 Groups Video

[Watch Video](https://youtu.be/R_7VhH7U4eE)

---
[Prev](03_shadow.md) | [Home](README.md) | [Next](05_groups-exercise.md)
