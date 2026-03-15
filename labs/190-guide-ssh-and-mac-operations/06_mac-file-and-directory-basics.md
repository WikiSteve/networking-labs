# MAC File and Directory Basics

In operations work, **MAC** means **move, add, and change**. Here it refers to common file and directory tasks, not a network-card MAC address.

## The commands to know first

These commands cover most everyday file-management work:

- `pwd` shows your current directory
- `ls` lists directory contents
- `cd` changes directories
- `mkdir` creates directories
- `touch` creates an empty file or updates its timestamp
- `cat` displays file contents
- `cp` copies files or directories
- `mv` moves or renames files
- `rm` removes files
- `rmdir` removes empty directories
- `more`, `less`, `head`, and `tail` help you read large files

## Listing and navigation

Use these constantly:

```bash
pwd
ls
ls -al
cd /etc
cd ~
```

Useful `ls` options:

- `-a` includes hidden files such as `.bashrc` and `.ssh`
- `-l` shows details such as permissions, owner, size, and timestamps

## Create directories efficiently

Instead of making one directory at a time, use `mkdir -p`:

```bash
mkdir -p Science/{grants/{approved,pending},patents/current}
```

That creates this structure in one command:

```text
Science/
├── grants/
│   ├── approved/
│   └── pending/
└── patents/
    └── current/
```

## Create and inspect files

```bash
touch myfile
echo "my contents" > file2
cat file2
head -n 5 ~/.bashrc
tail -n 5 ~/.bashrc
less ~/.bashrc
```

Use:

- `cat` for short files
- `less` for longer files you may need to scroll through
- `head` and `tail` when you only need the beginning or end

## Copy, move, and remove

```bash
cp file2 backup.txt
cp -r Science Science-copy
mv backup.txt archived.txt
rm myfile
rmdir emptydir
```

Notes:

- `cp -r` is needed when copying directories
- `mv` is used for both moves and renames
- `rmdir` only works on empty directories
- `rm -r` can remove an entire directory tree, so use it carefully

## Pipes and pagers

The pipe character sends the output of one command into another:

```bash
cat ~/.bashrc | more
cat ~/.bashrc | tail -n 50 | less
```

That is useful when a file is too large to read comfortably in one screen.

## Practical reminder

When you are not sure what a command did, verify immediately with:

```bash
pwd
ls -al
```

That habit catches mistakes quickly.

---
[Prev](05_configure-putty-to-use-your-private-key.md) | [Home](README.md)
