# Mode: setgid

## setgid

On an executable file, `setgid` causes the program to run with the file's group ID. On a directory, it means newly created files inherit the directory's group instead of the creator's default primary group.

This is commonly used on collaborative directories so a shared group stays attached to new files automatically.

In a long listing, you can spot `setgid` by a lowercase `s` where you would normally expect the group's execute bit to appear. If group execute is not set, this becomes an uppercase `S`.

![Before-and-after `ls -ld alice/` output showing the group execute position change after `chmod g+s alice/`.](assets/images/file-62d76ab43784b.png)

## Video Walkthroughs

### 🎥 setgid Video 1

[Watch Video](https://youtu.be/jpcVlVcWA4g)

### 🎥 setgid Video 2

[Watch Video](https://youtu.be/INM6NS-DrnI)

---
[Prev](07_mode-setuid.md) | [Home](README.md) | [Next](09_mode-sticky-bit.md)
