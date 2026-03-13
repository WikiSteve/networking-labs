# Snapshots

In this section we will use the LVM snapshot feature to recover `quotes.txt` from the `vi-tutorials` directory in your home folder. Make sure that directory and file still exist before you start.

Using snapshots requires free space in the volume group. Verify that with:

```bash
sudo vgdisplay
```

![`sudo vgdisplay` output showing the volume group with plenty of free space available for snapshots.](assets/images/file-62ceca6aa60fc.png)

You should have lots of free space available. In the screenshot example there are about 80 GiB free.

![Listing in the tutorial directory showing that `quotes.txt` still exists before the snapshot is created.](assets/images/file-62ced14d6bf8c.png)

Once you confirm the file is present, create a snapshot:

```bash
sudo lvcreate -L 10MB -s -n home_snap /dev/VG-Sharpe/lv-home
```

Here:

- `-L 10MB` sets the snapshot size
- `-s` means this logical volume is a snapshot
- `-n home_snap` names the snapshot

![`sudo lvcreate -L 10MB -s -n home_snap /dev/VG-Sharpe/lv-home` output showing the snapshot creation and rounding up to a full physical extent.](assets/images/file-62ced290ccb1e.png)

The message about rounding up to `12.00 MiB` means LVM allocates storage in whole extents, not arbitrary byte counts.

The snapshot is now just another logical volume. You can see it with:

```bash
sudo lvs
```

![`sudo lvs` output showing the new `home_snap` logical volume alongside the original logical volumes.](assets/images/file-62ced3a84a928.png)

After the snapshot exists, delete `quotes.txt` from your normal home directory.

Next, create a mount point such as `/mnt/home_snap` and mount the snapshot there:

```bash
sudo mkdir -p /mnt/home_snap
```

```bash
sudo mount /dev/VG-Sharpe/home_snap /mnt/home_snap
```

If you prefer, you can `cd /mnt` first and then mount it using the relative target `home_snap/`, which is what the screenshot shows.

![Mounting the `home_snap` logical volume under `/mnt/home_snap/` after creating the snapshot.](assets/images/file-62ced5aecfdbe.png)

![Directory listing inside the mounted snapshot showing the original `quotes.txt` content still available there.](assets/images/file-62ced6d3d3fbc.png)

To actually recover the file, copy `quotes.txt` back from the mounted snapshot into your normal home directory after verifying it is present.

## Screenshot 5

Take one clear screenshot proving that `quotes.txt` still exists inside the mounted snapshot and does not exist in your normal home directory anymore.

---
[Prev](05_removing-old-drive.md) | [Home](README.md)
