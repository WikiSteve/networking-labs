# Mode: sticky bit

## Sticky bit

The sticky bit on a directory restricts deletion so that only the file owner, the directory owner, or `root` can remove files from it.

The classic example is `/tmp`:

![`ls -ld /tmp` showing the sticky bit on the world-writable `/tmp` directory.](assets/images/file-62d76984e77e3.png)

In a long listing, you can spot the sticky bit by a lowercase `t` where you would normally expect the other execute bit. If execute is not set for others, the `t` becomes an uppercase `T`.

## Video Walkthrough

### 🎥 Sticky Bit Video

[Watch Video](https://youtu.be/G8LaNoqpmIc)

---
[Prev](08_mode-setgid.md) | [Home](README.md) | [Next](10_mode-applying.md)
