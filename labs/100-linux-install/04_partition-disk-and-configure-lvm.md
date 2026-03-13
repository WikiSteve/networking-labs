# Partition disk and configure LVM

![Disk layout diagram showing sda, the VG-LastName volume group, and the lv-swap, lv-root, and lv-home logical volumes.](assets/images/file-62da2b87552f9.png)

![Illustration introducing the manual partitioning and LVM configuration section.](assets/images/file-62bbcba592be0.jpg)

![Debian installer partitioning method screen with Manual selected.](assets/images/file-62bbcc73a9ef0.png)

Select manual

![Debian installer partition overview showing sda selected for manual partitioning.](assets/images/file-62bbcdb486180.png)

Select **sda** as shown.

![Debian installer confirmation screen for creating a new empty partition table on the disk.](assets/images/file-62bbce124fefe.png)

Select **Yes**.

![Debian installer partition menu after the disk has been initialized.](assets/images/file-62bbce5883a3c.png)

You should now have a partition with 21.5 GB of **free space**.

![Debian installer partition overview showing free space and the Configure the Logical Volume Manager option.](assets/images/file-62bbcf28478a5.png)

Select **Configure the Logical Volume Manager**

![Debian installer warning that the partition changes must be written before configuring LVM.](assets/images/file-62bbcfa295f1c.png)

Answer **Yes**.

![Debian installer LVM configuration summary with the Create volume group option.](assets/images/file-62bbd0318dae9.png)

Select **Create volume group**

Name the volume group **VG-LastName**. In the example screenshots, that becomes **VG-Sharpe**.

![Debian installer screen for entering the volume group name, shown as VG-Sharpe in the example.](assets/images/file-62bbd0e5d9df0.png)

![Debian installer screen for selecting the physical disk to include in the volume group.](assets/images/file-62bbd125c6f57.png)

Use `Tab` to move around and `Space` to select. Make sure you select the one drive available: `/dev/sda`.

![Debian installer confirmation screen before writing the LVM partitioning changes to disk.](assets/images/file-62bbd1b34de00.png)

Select **Yes**.

Even though you started from `/dev/sda`, the installer creates a partition first, so the resulting volume group lives on `/dev/sda1`.

![Debian installer LVM configuration details showing the resulting VG-Sharpe group on /dev/sda1.](assets/images/file-63bea7e182739.png)

To confirm, select **Display configuration details** from the main LVM configuration page.

![Debian installer LVM summary screen with the Create logical volume option selected.](assets/images/file-62bbd20d999e9.png)

Select **Create logical volume**

![Debian installer screen for selecting the volume group that will hold the new logical volume.](assets/images/file-62bbd2f32cc69.png)

For the next three logical volumes, keep selecting the same volume group: **VG-LastName**.

![Debian installer prompt for naming the lv-swap logical volume.](assets/images/file-62bbd34a5d44a.png)

Create `lv-swap` with a size of **1G**.

![Debian installer prompt for entering the lv-swap logical volume size as 1G.](assets/images/file-62bbd3dae3259.png)

![Debian installer prompt for naming the lv-root logical volume.](assets/images/file-62bbd43158f1a.png)

![Debian installer prompt for entering the lv-root logical volume size as 2 GB.](assets/images/file-62bbd461d08e6.png)

Let `lv-root` be **2 GB**.

![Debian installer prompt for naming the lv-home logical volume.](assets/images/file-62bbd4b578e78.png)

![Debian installer prompt for giving lv-home the remaining free space in the volume group.](assets/images/file-62bbd4d7b9bb0.png)

Let `lv-home` use the remaining free space in **VG-LastName**.

![Debian installer LVM summary showing lv-swap, lv-root, and lv-home created in the same volume group.](assets/images/file-62bbd553a4ef1.png)

Select **Finish**.

![Debian installer partition summary after the logical volumes have been created.](assets/images/file-62bbd5e3cb343.png)

Your summary should look like this.

![Debian installer partition summary with filesystem and swap assignments for the logical volumes.](assets/images/file-63beaa867b9ae.png)

Set the filesystem types and mount points for **#1** and **#2**. Set **#3** as swap.

![Debian installer confirmation screen for writing the final partition and filesystem changes to disk.](assets/images/file-62bbd832df8b6.png)

## Screenshot 2

Ask the person who knows the root password to log in as **root** and run:

```bash
lvdisplay | less
```

Capture the details for:

- `lv-swap`
- `lv-home`
- `lv-root`

![lvdisplay output showing the details of the lv-swap logical volume in VG-Sharpe.](assets/images/file-62bbdeb48e3c7.png)

![lvdisplay output showing the details of the lv-home logical volume in VG-Sharpe.](assets/images/file-62bbdf346b73f.png)

---
[Prev](03_starting-debian-installer.md) | [Home](README.md)
