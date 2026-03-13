# Mode: standard

## Introduction

There are three standard Linux permissions:

- **Read**
- **Write**
- **Execute**

Together they are written as `rwx`.

Permissions are evaluated for:

- **User**
- **Group**
- **Others**

This is often abbreviated as `ugo`.

## Viewing Permissions and Ownership

The `-l` option to `ls` expands the listing to show both permissions and ownership.

![`ls -l` output showing a file with its permission string, owner, and group.](assets/images/file-62d71be52a600.png)

- `#1` **Mode** or permission string. A leading `-` means a regular file. The next three characters are user permissions, the next three are group permissions, and the last three are other permissions.
- `#2` Owner user
- `#3` Owner group

If you run `ls -l directoryname`, you normally see the contents of the directory. To see the directory's own metadata instead, add `-d`:

![`ls -ld /home/steve` output showing the permissions and ownership of the directory itself.](assets/images/file-62d72748d6bcf.png)

Without `-ld`, you need more awkward alternatives to inspect a directory's own mode and ownership.

![`ls -al` output in a home directory, illustrating why a normal long listing shows contents instead of only the directory metadata.](assets/images/file-62d7283d5b4db.png)

## Permission Notes

- Permissions in standard Linux mode bits apply to each file or directory individually.
- Unlike NTFS, standard `ugo` permissions are not inherited in the same way.
- To list files in a directory, you need read permission on that directory.
- To `cd` into a directory, you need execute permission on that directory.

## Changing a File Owner and Group

Use `chown` to change file ownership.

```bash
chown [owner][:group] [-R] <target>
```

- You can specify the owner, the group, or both.
- The target can be a file, a directory, or a wildcard expression.
- `-R` means recursive if the target is a directory.

### Examples of chown

Jean-Luc does not want to share `~/earl/grey` with Spock and wants the file fully owned by him:

```bash
chown jean-luc grey
```

![Long listing in `~/earls` showing the file `grey` after its owner is changed with `chown`.](assets/images/file-62d72c45990ac.png)

`~/earl` turns out to be owned by Steve. To change just the group, put a colon before the group name. Here we are changing the directory `earl`, not the file inside it:

```bash
chown :jean-luc .
```

![Before-and-after `ls -ld ~/earl` output showing the directory group change after `chown :jean-luc .`.](assets/images/file-62d72f8035299.png)

### Practice check

Using `.` means the **current** directory. Using `..` would mean the **parent** directory.

To change the directory `alice` and **all subdirectories** to user `spock` and group `science`, use:

```bash
sudo chown -R spock:science alice
```

![`tree -pug alice` output showing a recursive directory tree used to explain `sudo chown -R spock:science alice`.](assets/images/file-62d73d8a22337.png)

## Changing File Permissions

- The command used to change permissions is `chmod`, short for **change mode**.
- `chmod` takes a permission instruction followed by the file or directory to change.
- The permission instruction can be symbolic or numeric.

### Symbolic Changes

- Start with `u`, `g`, `o`, or `a` for user, group, other, or all
- Follow with `+`, `-`, or `=` to add, remove, or set
- Finish with one or more of `r`, `w`, and `x`

Examples:

```bash
chmod go-rw file1
chmod a+x file2
chmod u=rw file3
```

### Numeric Permissions

- Numeric permissions are usually three digits: user, group, other
- `x = 1`, `w = 2`, `r = 4`
- For example, `644` appears as `-rw-r--r--`

### Practice check

The octal value for `-rwxr-xr-x` is `755`.

### Examples of chmod numeric

```bash
chmod 644 file1
chmod 755 file2
chmod 750 file3
```

## Video Walkthroughs

### 🎥 Standard Permissions Video 1

[Watch Video](https://youtu.be/cIKG5rsOWZQ)

### 🎥 Standard Permissions Video 2

[Watch Video](https://youtu.be/-efuzdIYD-k)

---
[Prev](05_groups-exercise.md) | [Home](README.md) | [Next](07_mode-setuid.md)
