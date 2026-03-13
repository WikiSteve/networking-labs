# Users

## /etc/passwd

Linux is a multi-user system. A quick way to inspect recent user entries is to look at the end of `/etc/passwd`.

![Terminal output from `tail /etc/passwd` showing regular user accounts near the end of the passwd file.](assets/images/file-62d5a2c8cbbf9.png)

The highlighted entries are human users. What about all of the accounts that use `/usr/sbin/nologin`?

![Terminal output from `tail /etc/passwd` showing service accounts that use `/usr/sbin/nologin` as their shell.](assets/images/file-62d5a38b73104.png)

Much like disabling root with `/usr/sbin/nologin`, these are service accounts. Linux uses them in roughly the same way Windows uses service accounts.

![`ps aux | grep systemd` output showing background services running as dedicated accounts instead of as root.](assets/images/file-62d5a7ee5e66c.png)

When root access is not required, a daemon is often run as a dedicated service account. If that service is compromised, the attacker gets the limited permissions of that service account instead of full root access.

### GECOS Field

![Excerpt from `/etc/passwd` with the GECOS field highlighted for user-account contact information.](assets/images/file-62d5adb56e370.png)

The highlighted portion is the GECOS field.

The typical format for the GECOS field is a comma-delimited list with this order:

- User's full name or application name
- Building and room number or contact person
- Office telephone number
- Home telephone number
- Other contact information such as pager, fax, or external email

To change contact information, use `chfn`. To change the login shell, use `chsh`.

![`ls -l /etc/passwd` showing that the passwd file is readable by all users.](assets/images/file-62d5b53e2ad5a.png)

---
### 🧠 /etc/passwd access

> [!NOTE]
> **Statement:** Anyone can view `/etc/passwd`.
>
> - [ ] True
> - [ ] False

<details>
<summary>👉 <b>Reveal answer</b></summary>

**Correct:** True
</details>

---

Instead of parsing the GECOS field directly from `/etc/passwd`, you can use `finger`.

You may need to install `finger` first.

![`finger bbunny` output showing formatted GECOS details such as name, home directory, shell, and office information.](assets/images/file-62d5b5e33c899.png)

`finger` formats the GECOS information in a more readable way. Historically, the finger protocol could even expose this information over the network as a primitive directory service.

### Remaining Columns in passwd

![Excerpt from `/etc/passwd` annotated to identify the username, UID, GID, and home-directory fields.](assets/images/file-62d5bbe2c87cc.png)

- `#1` **Username**
- `#2` **User ID (UID)**: `0` is root; `1-99` are traditionally special system accounts; `100-999` are commonly reserved for administrative or service accounts
- `#3` **Group ID (GID)**: the primary group ID, stored in `/etc/group`
- `#4` **Home directory**

![Excerpt from `/etc/passwd` highlighting the `x` password placeholder that points to `/etc/shadow`.](assets/images/file-62d5c10d0ceb9.png)

- `#5` **Password field**: an `x` means the password hash is stored in `/etc/shadow`

### Practice Check

The first usable regular-user UID in the example defaults is `1000`.

### Creating Users

The exact tooling varies slightly between distributions, but in this lecture we focus on Debian-style systems.

If the Perl wrapper exists, the recommended command is `adduser`.

![Terminal output from `whereis adduser` and `head /usr/sbin/adduser`, confirming that `adduser` is an installed wrapper script.](assets/images/file-62d5c994b8dcb.png)

If `adduser` is not available, `useradd` will be.

```bash
adduser <username>
```

Square brackets in command syntax mean the argument is optional.

It's not necessary to customize the groups right away. The `adduser` script will automatically:

1. Create a group with the same name as the user
2. Make that new group the user's primary group

For example, if you create the user `spock`, the group `spock` is also created and becomes the primary group.

> [!NOTE]
> Even when Linux authenticates against local users in `/etc/passwd`, PAM can integrate with external identity systems such as Active Directory by using SSSD.

### login.defs Reference

Using `/etc/login.defs`, the lecture's UID defaults are:

```text
UID_MIN     1000
UID_MAX    60000
#SYS_UID_MIN 100
#SYS_UID_MAX 999
```

---
[Prev](01_introduction.md) | [Home](README.md) | [Next](03_shadow.md)
