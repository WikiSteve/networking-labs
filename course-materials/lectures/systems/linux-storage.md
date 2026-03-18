# Linux Storage

- Filename: `Linux Storage.pptx`
- Subject: `systems`
- Type: `lecture`
- Reusable: `yes`
- Source file: [Source copy](../../sources/Linux%20Storage.pptx)

## Summary

This reusable lecture deck covers Linux storage fundamentals with the goal of giving a broad introductory map of storage types, block-level concepts, LVM, caching, redundancy, filesystems, and backup-oriented features before readers get lost in commands. It starts by distinguishing file, block, and object storage, then explains Linux block concepts such as ext4 block size, inodes, inode metadata, and block devices. From there it moves into storage design decisions for bare metal versus virtual machines, the performance and risk tradeoffs of write caching, and the role of the device mapper as the abstraction layer behind features like encryption, snapshots, mirroring, striping, thin provisioning, and LVM.

## Key Details

- Opens by dividing storage into file, block, and object storage and explicitly tells the reader to understand the differences among those three models first.
- Explains ext4 block size as 4 KB, then uses that to introduce how larger files span multiple inodes and how `ls -ail` can be used to inspect inode numbers.
- Covers what inodes store besides file data pointers, including change time, access time, modification time, permissions, and owner metadata.
- Lists common block devices such as hard drives, CD-ROMs, USB storage, iSCSI devices, and loop devices.
- Compares storage decisions on bare metal versus virtual machines, noting that RAID or redundancy must exist somewhere, but in VMs the host platform often handles much of that responsibility.
- Introduces write caching and write-through behavior, with a warning that cached writes improve apparent performance but can cause data loss during power loss or kernel failure unless mitigations exist.
- Identifies the device mapper as the underlying framework that enables caching, encryption, snapshots, striping, mirroring, and thin provisioning, then links that to `dm-crypt` and LVM2.
- Walks through core LVM terminology: physical volume, physical partition, volume group, physical extents, logical volume, filesystem, and mount point.
- Explains physical extents as 4 MB chunks inside a volume group.
- Covers advanced LVM features including LVM RAID, `dm-cache`, snapshots with copy on write, filesystem resizing with `resize2fs`, and moving data between disks with `pvmove`.
- Ends with broader storage topics such as object storage, tape, `tar`, and off-site backup strategy.
- Warns against blindly using LVM everywhere, especially in virtual machines where some benefits are reduced.

## Tags

- `linux-storage`
- `lvm`
- `device-mapper`
- `inodes`
- `block-storage`
- `dm-cache`
- `snapshots`
- `backups`
