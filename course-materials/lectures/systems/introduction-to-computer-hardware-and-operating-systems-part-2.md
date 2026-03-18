# Introduction to Computer Hardware and Operating Systems Part 2

- Filename: `Introduction to Computer Hardware and Operating Systems part 2.pptx`
- Subject: `systems`
- Type: `lecture`
- Reusable: `yes`
- Source file: [Source copy](../../sources/Introduction%20to%20Computer%20Hardware%20and%20Operating%20Systems%20part%202.pptx)

## Summary

This reusable lecture deck teaches storage hardware, secure data deletion, filesystems, partitioning, and volume management as a continuation of an introductory hardware and operating systems unit. It explains how HDDs physically store data with platters, read/write heads, spinning disks, and magnetic bit orientation, then uses that model to explain why deleted data can remain recoverable until overwritten. It compares overwrite tools such as DBAN and KillDisk, degaussing, and physical destruction, then contrasts HDD erasure with SSD-specific complications like wear leveling and TRIM. The second half shifts into operating-system storage organization by explaining filesystems, comparing FAT32, exFAT, NTFS, and Ext4, introducing journaling and its tradeoffs, and then walking through partitions, volumes, RAID, Windows Disk Management, and Linux LVM.

## Key Details

- Covers HDD mechanics in concrete physical terms including platters, actuator arms, read/write heads, spindle speed, and magnetic storage.
- Explains that file deletion often removes references rather than instantly erasing platter data.
- Presents three hard-drive erasure strategies: overwrite tools, degaussing, and physical destruction.
- Distinguishes SSDs from HDDs by discussing wear leveling and TRIM.
- Introduces flash memory concepts and compares USB flash drives and SSDs.
- Explains SSD internals such as DRAM cache, controllers, garbage collection, error correction, and self-encrypting drives.
- Teaches the purpose of filesystems and compares FAT32, exFAT, NTFS, and Ext4.
- Includes a clear section on journaling and why it helps crash recovery.
- Covers the difference between partitions and volumes.
- Names platform-specific tools such as Windows Disk Management and Linux LVM.
- References Storage Spaces and RAID for later reading and follow-up work.
- Ends with homework on partitioning, LVM, Storage Spaces, RAID, and a live Debian installation lab.

## Tags

- `hardware`
- `storage`
- `hdd`
- `ssd`
- `filesystems`
- `partitioning`
- `lvm`
- `raid`
