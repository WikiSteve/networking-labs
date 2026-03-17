# LAB LVM Setup

- Filename: `LAB LVM Setup.docx`
- Subject: `systems`
- Type: `lab`
- Reusable: `yes`
- Source file: [Source copy](../../sources/LAB%20LVM%20Setup.docx)

## Summary

This reusable Linux storage lab teaches Logical Volume Manager setup during Debian installation and then extends into a challenge on growing storage with an additional disk. The main activity walks through creating a new partition table, carving out a 20 GB LVM physical volume, building a volume group named with the learner's last name, and creating three logical volumes for root, home, and swap with specified sizes and mount points. It then has learners verify the configuration from the installed system using `pvdisplay`, `vgdisplay`, and `lvdisplay`, with sample outputs included. The second half adds a new disk at `/dev/sdb`, extends the existing volume group, grows the root logical volume, and resizes the filesystem.

## Key Details

- The lab begins in the Debian Installer partitioning section and requires creating a new partition table.
- Learners create a 20 GB primary partition and mark it as a physical volume for LVM.
- The required volume group name is `LastNameVG`.
- Inside that volume group, the lab creates `firstname-root`, `firstname-home`, and `firstname-swap`.
- The filesystem assignments are explicit: Ext4 for `/`, Ext4 for `/home`, and swap area for swap.
- After installation, verification uses `sudo pvdisplay`, `sudo vgdisplay`, and `sudo lvdisplay`.
- Sample outputs are included so learners can compare expected PV, VG, and LV state.
- The challenge section assumes a second drive at `/dev/sdb` and initializes it with `sudo pvcreate /dev/sdb`.
- The new disk is added with `sudo vgextend LastNameVG /dev/sdb`.
- Root expansion uses `lvextend` followed by `resize2fs`.
- Final verification uses `lvdisplay` and `df -h /`.
- Deliverables for the challenge include snapshots of `vgdisplay`, `lvdisplay`, and `df -h`.

## Tags

- `lvm`
- `debian-installer`
- `partitioning`
- `pvcreate`
- `vgextend`
- `lvextend`
- `resize2fs`
- `linux-storage`

