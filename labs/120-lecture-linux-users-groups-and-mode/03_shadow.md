# Shadow

## /etc/shadow

As we saw previously, if `/etc/passwd` shows an `x` in the password field, the actual password hash is stored in `/etc/shadow`.

These are password hashes, not plaintext passwords.

![`sudo tail /etc/shadow` output showing hashed passwords and password-aging fields for local accounts.](assets/images/file-62d5e93292a18.png)

- `#1` **User name**
- `#2` **Hashing algorithm** or a **status marker** such as `!` for a disabled account
- `#3` **Salt**
- `#4` **Hashed password**
- `#5` **Days since epoch of last password change**
- `#6` **Days until change is allowed**
- `#7` **Days before change is required**
- `#8` **Warning days before expiration**

Common hash markers include:

- `$1$` - MD5
- `$2a$`, `$2b$`, `$2y$` - bcrypt
- `$5$` - SHA-256
- `$6$` - SHA-512
- `$y$` - yescrypt

The remaining shadow fields track inactivity, account expiry, and reserved values.

[Columns and history of the shadow file](https://en.wikipedia.org/wiki/Passwd#Shadow_file)

---
### 🧠 shadow access

> [!NOTE]
> **Statement:** Everyone on the system is able to read the shadow file.
>
> - [ ] True
> - [ ] False

<details>
<summary>👉 <b>Reveal answer</b></summary>

**Correct:** False
</details>

---
[Prev](02_users.md) | [Home](README.md) | [Next](04_groups.md)
