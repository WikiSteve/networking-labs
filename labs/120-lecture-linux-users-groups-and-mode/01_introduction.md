# Introduction

## File Permissions

Linux file permissions are the standard mechanism for restricting access to files and directories.

There are three core permissions for three classes of users:

**Users**

- **User**: the account that owns the file
- **Group**: the group that owns the file
- **Others**: everyone who is not in the first two categories

**Permissions**

- `r` - read
- `w` - write
- `x` - execute

## Default Primary Group

- By default, each user gets a primary group with the same name as the username.
- If you add a user named `fred`, the system typically also creates a primary group named `fred`.
- User account information is stored in `/etc/passwd`, while password hashes are stored in `/etc/shadow`.
- Group information is stored in `/etc/group`.

## Users and Groups

Windows also has users and groups. The concept is similar, and historically Windows borrowed heavily from Unix ideas here.

In Linux, a user can belong to multiple groups, but groups cannot contain other groups.

## Common Commands

### Add a user

```bash
adduser <username>
```

### Add a group

```bash
groupadd <groupname>
```

## PowerPoint Video Overview

This lecture was adapted from an original PowerPoint deck to reduce slide-heavy delivery. The main skipped topics are `umask` and ACLs. Both are worth learning, but they are not the focus of this lecture.

- Users and groups: slides 1-9
- Regular file permissions: slides 10-19
- Special permissions: slides 20-24
- Default permissions through `umask`: slides 25-26
- UGO exercise solution: slide 27
- ACL introduction: slides 28-29
- ACL on files: slides 30-36
- ACL on directories: slides 37-44
- ACL recap and final remarks: slides 47-61

---
[Home](README.md) | [Next](02_users.md)
