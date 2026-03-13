# Moving Extents

This server has been running for two years on an old 20 GB SATA drive. It is time to migrate the data to a new 100 GB NVMe drive. The long-term plan may be RAID, but today the goal is simply to get all data off the old drive and onto the new one.

Company policy says machines must be powered off before service work. Shut the VM down with `sudo poweroff`.

Using VMware Workstation, add a 100 GB NVMe drive to the VM.

![Add Hardware Wizard screen for choosing an NVMe virtual disk type.](assets/images/file-62cea20b950e6.png)

![Add Hardware Wizard screen for naming the new 100 GB NVMe disk file.](assets/images/file-62cea2183f945.png)

![VMware virtual machine settings showing both the original SCSI disk and the new 100 GB NVMe disk attached.](assets/images/file-62cea2e34931f.png)

Once the new NVMe drive is installed, boot the VM again.

When you run `lsblk`, the physical volume `nvme0n1` should appear.

![`lsblk` output showing the original `sda` disk and the newly attached `nvme0n1` disk.](assets/images/file-62cea393ba6ac.png)

Before LVM can use the new drive, create a partition on it with `sudo fdisk /dev/nvme0n1`.

![`fdisk /dev/nvme0n1` starting on the new 100 GiB VMware NVMe disk.](assets/images/file-62cea7b93077c.png)

Enter `p` to verify that there are no partitions yet.

![`fdisk` output confirming the new NVMe disk is currently unpartitioned.](assets/images/file-62cea7f0556b1.png)

Enter `F` to verify the free space available for partitioning. It should be about 100G.

![`fdisk` free-space view showing the full 100 GiB of the new disk available.](assets/images/file-62cea8a644b3d.png)

Press `n` to create a new partition, then choose `p` for primary and `1` for partition 1.

For the highlighted entries, press Enter to accept the defaults.

![`fdisk` prompts for a new primary partition using the default first and last sector values.](assets/images/file-62cea9665ec62.png)

Enter `p` again to verify the new partition. If everything looks correct, press `w` to write the partition table.

![`fdisk` output after writing the new partition table to the NVMe disk.](assets/images/file-62cea9c30ad1a.png)

Create a physical volume on the new partition:

```bash
sudo pvcreate /dev/nvme0n1p1
```

![`sudo pvcreate /dev/nvme0n1p1` confirming the new NVMe partition is now an LVM physical volume.](assets/images/file-62ceaa74617d7.png)

## Working with the Volume Group

So far you have done the physical work: adding the disk and partitioning it. Now we extend the existing volume group to include the new drive. Substitute your own volume-group name if it differs from the screenshot example.

Start by running:

```bash
sudo vgextend VG-Sharpe /dev/nvme0n1p1
```

![`sudo vgextend VG-Sharpe /dev/nvme0n1p1` output showing the volume group successfully extended onto the NVMe partition.](assets/images/file-62ceadb8949b4.png)

At this point, the new free space is part of the volume group, but the existing data still lives on the old SATA-backed physical volume. Because both drives now belong to the same volume group, we can migrate the extents off `/dev/sda1`.

Run:

```bash
sudo pvmove -i2 /dev/sda1 /dev/nvme0n1p1
```

The `-i2` reporting interval prints progress every two seconds.

![`sudo pvmove -i2 /dev/sda1 /dev/nvme0n1p1` showing progress as extents are migrated from the old drive to the new NVMe partition.](assets/images/file-62ceaeed01041.png)

Once the move is complete, remove `/dev/sda1` from the volume group:

```bash
sudo vgreduce VG-Sharpe /dev/sda1
```

![`sudo vgreduce VG-Sharpe /dev/sda1` confirming the old SATA partition has been removed from the volume group.](assets/images/file-62ceb094ef3d2.png)

![`sudo pvdisplay` output showing the new NVMe physical volume as part of the volume group and the old `sda1` no longer assigned.](assets/images/file-62cebca10fa3f.png)

## Screenshot 3

Capture the `pvdisplay` output and highlight it exactly as shown so it is clear that the new NVMe drive belongs to the volume group and the old `sda1` drive no longer does.

---
[Prev](03_shuffling-space.md) | [Home](README.md) | [Next](05_removing-old-drive.md)
