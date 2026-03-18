# Glossary

This glossary collects the terms students are most likely to encounter repeatedly across the book.

## Access control

The process of deciding which subject may perform which action on which object.

## ACL

An **Access Control List**. A more detailed permission model that can extend beyond basic owner/group/other Unix permissions.

## Address binding

The process of associating the addresses a program uses with the real memory locations used by the system.

## Backup

A recoverable copy of data used to restore information after deletion, corruption, ransomware, or other loss. Backup is not the same as RAID.

## Batch file

A plain-text file containing commands for `cmd.exe` to execute in sequence on Windows.

## BIOS

An older firmware model used to start a computer before the operating system takes over.

## Bootloader

Software that loads the operating-system kernel during startup.

## Business continuity

Planning for how an organization continues operating during and after disruption.

## CA

Short for **Certificate Authority**, the entity that signs certificates in a PKI model.

## Certificate

A signed data structure that binds identity information to a public key.

## `chroot`

A mechanism that lets an administrator treat another mounted filesystem as the working root filesystem.

## CLI

A **Command-Line Interface**, where users interact with the system by typing commands.

## Cluster

A filesystem allocation unit made from one or more lower-level storage units such as sectors.

## Context switch

The act of saving one process state and restoring another so the OS can switch CPU attention.

## CSR

A **Certificate Signing Request**, used to ask a certificate authority to issue a certificate.

## Differential backup

A backup containing changes since the last full backup.

## Directory permissions

Permissions on a directory that govern listing, entry/traversal, and modification of directory entries.

## Disaster recovery

The technical and procedural work needed to restore systems and data after failure.

## Distribution

A curated operating-system package built around the Linux kernel plus user-space tools, repositories, defaults, and support choices.

## ext4

A commonly used Linux filesystem and the course’s main working example for Linux filesystem behavior.

## File system

The structure an operating system uses to organize files, directories, metadata, and storage allocation.

## FTPS

FTP protected with TLS.

## GPT

The **GUID Partition Table**, a newer disk-partitioning model commonly associated with UEFI systems.

## GRUB

A common Linux bootloader used to select and start operating systems.

## GUI

A **Graphical User Interface**, using windows, menus, and pointing devices rather than typed commands.

## Hypervisor

The software layer that enables and manages virtual machines.

## Incremental backup

A backup containing changes since the previous backup of any kind.

## Inode

A Linux filesystem structure that stores metadata about a file and points to its data blocks.

## Interrupt

A signal that tells the CPU and OS that something needs attention.

## `iproute2`

The modern Linux networking toolkit centered around the `ip` command.

## Journaling

A filesystem behavior that helps preserve consistency after crashes by recording intended or in-progress changes.

## Kernel

The core privileged part of the operating system that manages hardware access, memory, processes, and devices.

## Kernel mode

The privileged operating mode used by the operating system core.

## LUKS

A Linux disk-encryption framework used to protect stored data.

## LVM

The **Logical Volume Manager**, used to pool storage and create logical volumes on Linux.

## Logical volume

A storage unit carved from an LVM volume group.

## MMU

The **Memory Management Unit**, hardware that helps translate logical addresses to physical memory addresses.

## MBR

The **Master Boot Record**, an older disk boot and partition structure.

## Netplan

An Ubuntu-centered declarative network-configuration layer that can hand off to `systemd-networkd` or `NetworkManager`.

## Object storage

A storage model where data is stored and retrieved as objects with metadata, typically through a service model rather than as directly mounted local filesystems.

## OpenSSL

A widely used toolkit for TLS, certificates, keys, and cryptographic inspection or troubleshooting.

## Parity

Depending on context, either an error-detection concept in communications or a recovery-enabling data concept in storage RAID designs.

## Partition

A defined region of a physical disk.

## PATH

An environment variable that tells the shell where to search for commands.

## Physical volume

An LVM-prepared disk or partition that contributes storage to a volume group.

## PKI

**Public Key Infrastructure**, the trust framework around certificates, signing, and trusted authorities.

## Process

A running instance of a program, including execution state and associated resources.

## Pseudo-terminal

A software-mediated terminal session, often represented as `pts`, commonly used for remote shells.

## RAID

A **Redundant Array of Independent Disks**, used to improve availability and/or performance across multiple drives.

## Root account

The highest-privilege Linux account, capable of unrestricted administrative actions.

## Rootkit

A stealth mechanism used to hide malicious activity by altering what the operating system reports.

## Sector

A low-level storage unit on disk, especially in classic disk-layout teaching.

## `ss`

A modern Linux inspection tool commonly used in place of older `netstat` habits.

## Standard error

The error output stream of a command.

## Standard output

The normal output stream of a command.

## Sticky bit

A special permission bit, especially useful on shared writable directories, to limit who may delete or rename entries.

## `sudo`

A command that lets an authorized user run specific commands with elevated privileges.

## Symbolic link

A reference to another file or directory path.

## System call

A controlled request from a user-mode program to the operating system for a privileged service.

## `systemd`

The modern init and service-management system used by many Linux distributions.

## TLS

**Transport Layer Security**, the protocol family used to protect network communication such as HTTPS and FTPS.

## `tty`

A local console or virtual console terminal context on Linux.

## UEFI

A newer firmware model commonly paired with GPT partitioning.

## `umask`

The file mode creation mask that removes permissions from default creation modes for new files and directories.

## User mode

The less-privileged execution mode where ordinary applications run.

## Virtual machine

A software-defined system that behaves like an independent computer while sharing underlying physical hardware.

## Volume group

An LVM storage pool created from one or more physical volumes.
