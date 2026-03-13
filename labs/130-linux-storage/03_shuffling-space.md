# Shuffling Space

We are continuing from the earlier Linux lab where the system ran out of space while trying to install Firefox. There should have been just enough space left to install `xterm`.

![`df` output showing `lv-root` nearly full while `lv-home` has almost all of its space free.](assets/images/file-62cde5f281d03.png)

Save that screenshot. You will need it later.

The point of this exercise is that `lv-root` is full while `lv-home` is barely used. On a non-LVM system this kind of mistake would be awkward to fix. With LVM, we can shrink `lv-home` by 5 GB and grow `lv-root` by 5 GB.

We cannot simply start stealing extents blindly because the home logical volume already contains data. Linux spreads file data around the filesystem, so the end of the logical volume may still contain live blocks.

Because `/home` is not required for the system to keep running, we can unmount it safely. If this were the root filesystem, we would likely need to boot from other media first.

> [!NOTE]
> You cannot unmount a filesystem that is currently in use. If you are inside `/home` or one of its subdirectories, the unmount will fail. Exit any other terminals, move to `/`, and reboot if the target still reports as busy.

![Command output showing `sudo umount home` completing without an error.](assets/images/file-62cdf3abd1a8a.png)

If the unmount succeeds, `/home` should no longer appear in `df` output.

We want to shrink home by 5 GB:

- current size: 17 GB
- target size after shrinking: 12 GB

If you need a reminder about your logical volume device names, list them from `/dev/<your-volume-group>` as shown below.

![Listing of the logical-volume device paths inside `/dev/VG-Sharpe/`, including `lv-home`, `lv-root`, and `lv-snap`.](assets/images/file-62cdf6e637683.png)

I am completing the resize from inside that directory using relative paths.

Modern LVM can automatically run `resize2fs` when asked, so the next two screenshots are included only to show the older manual process.

For reference only, do not perform this step:

![`sudo e2fsck -f lv-home` output showing a successful filesystem check before a manual resize.](assets/images/file-62cdf80ab6ef7.png)

For reference only, do not perform this step either:

![Manual `resize2fs lv-home 12G` output showing the filesystem being shrunk to 12 GB.](assets/images/file-62cdf87aa670e.png)

Now we can do the real resize. Oddly enough, `lvresize` does not support the relative path here, so use the full path to `lv-home`.

We will use `lvresize -r` so LVM automatically runs `resize2fs` for us.

![`sudo lvresize --resizefs -L 12G /dev/VG-Sharpe/lv-home` output showing the logical volume and filesystem shrinking successfully.](assets/images/file-62ce09004ff80.png)

That reclaims 5 GB worth of extents.

![`sudo vgdisplay` output showing free extents available in the volume group after shrinking `lv-home`.](assets/images/file-62ce0e28663a0.png)

In the example there are now 1333 free extents, which is about 5.21 GiB. We can allocate those extents to root.

With `lvresize`:

- `-l` (lowercase L) means extents
- `-L` (uppercase L) means an explicit size such as `K`, `M`, or `G`

We will again let `lvresize` resize the filesystem automatically.

> [!NOTE]
> Online expansion is easy. Online shrinking is not. If you needed to shrink `lv-root`, you would normally boot from other media first.

![`sudo lvresize --resizefs -l +1333 /dev/VG-Sharpe/lv-root` output showing `lv-root` growing by the reclaimed extents.](assets/images/file-62ce13f17a343.png)

Success. If you now run `df -h`, root should have about 5 GB more space available. Remount home with `sudo mount -av`; `df` only shows mounted filesystems.

![Before-and-after `df` output comparing the sizes of `lv-root` and `lv-home` after the resize work is complete.](assets/images/file-62ce15134a24c.png)

## Screenshot 2

Using whatever editor you prefer, display the before and after clearly. Your root logical volume should increase by 5 GB and home should decrease by 5 GB by the same amount. Highlight `lv-root` and `lv-home` exactly as shown for both the before and after views.

---
[Prev](02_sudo-password.md) | [Home](README.md) | [Next](04_moving-extents.md)
