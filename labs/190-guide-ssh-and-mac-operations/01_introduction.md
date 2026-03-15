# Introduction

This guide covers two related topics:

- setting up SSH keys so PuTTY can log in without a password prompt on every connection
- reviewing the Linux file and directory commands commonly used for move, add, and change work

## What you will do

1. Generate an SSH key pair with PuTTYgen.
2. Publish the public key to GitHub.
3. Import that key onto two Linux systems.
4. Configure PuTTY to use the saved private key.
5. Review the core Linux commands used to inspect, create, move, copy, and remove files and directories.

## Why this matters

Key-based SSH access is both more convenient and more secure than repeated password entry when it is set up correctly. The MAC commands then give you the basic file-management skills needed once you are logged in.

## Before you start

- Make sure both Linux systems are running and reachable.
- Confirm PuTTY and PuTTYgen are installed on the Windows system you are using.
- Decide on a simple naming pattern for your keys and saved PuTTY sessions.

Recommended examples:

- key comment: `yourusername@yourpc`
- saved PuTTY sessions: `ubuntu-key` and `centos-key`

---
[Home](README.md) | [Next](02_generate-ssh-keys-with-puttygen.md)
