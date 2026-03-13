# Mode: applying

## Using chmod with special permissions

| Special permission | Effect on files | Effect on directories |
| --- | --- | --- |
| `u+s` (`setuid`) | Executable runs as the file owner | No normal effect on directories |
| `g+s` (`setgid`) | Executable runs as the file group | New files inherit the directory's group |
| `o+t` (`sticky`) | No special effect on regular files | Users with write access can remove only their own files unless they are `root` |

## Setting Special Permissions

- Symbolically: `setuid = u+s`, `setgid = g+s`, `sticky = o+t`
- Numerically, the leading special-permission digit is:
  - `4` for `setuid`
  - `2` for `setgid`
  - `1` for `sticky`

### Examples

![Slide showing `chmod g+s directory` and `chmod 2770 directory` as symbolic and octal setgid examples.](assets/images/file-62d76dcedc741.png)

### Reminder

When you answer octal questions that include a special permission, include the leading special-permission digit as part of the value.

---
[Prev](09_mode-sticky-bit.md) | [Home](README.md) | [Next](11_mode-exercise.md)
