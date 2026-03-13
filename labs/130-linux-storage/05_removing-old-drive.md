# Removing Old Drive

> [!WARNING]
> Fully back up your virtual machine by copying the VM directory to external storage and testing that backup. By continuing, you accept that a mistake here could require rebuilding the VM from an earlier lab.

Now that the data has been moved off the old drive, we want to remove it. If you remove it immediately, the VM will not boot, because the GRUB bootloader still resides on the original `sda` disk.

We need to write a new GRUB bootloader to `nvme0n1`, not to `nvme0n1p1`.

Run:

```bash
sudo dpkg-reconfigure grub-pc
```

![`dpkg-reconfigure grub-pc` asking for the Linux command-line settings during the GRUB reconfiguration process.](assets/images/file-62cec213f4067.png)

Leave the Linux command line blank and press Enter.

![GRUB configuration prompt for the default Linux command line, left blank.](assets/images/file-62cec25f7bf9c.png)

Leave the default Linux command line blank as well and press Enter again.

![GRUB package screen explaining the automatic installation of GRUB to selected devices.](assets/images/file-62cec2c252da2.png)

Read the screen and press **OK**.

![GRUB install-device selection screen showing both the NVMe disk and the old SATA disk as choices.](assets/images/file-62cec35a7374e.png)

Use the arrow keys and space bar to select and unselect entries, and Tab to move to the **OK** button.

Select `/dev/nvme0n1`, unselect `/dev/sda`, and then press **OK**.

![GRUB reconfiguration output after selecting the NVMe disk and deselecting the old SATA disk.](assets/images/file-62cec4087be66.png)

When it finishes, shut the VM down completely with `sudo poweroff`.

![VMware settings view showing the VM after shutdown, ready for removal of the old SATA disk.](assets/images/file-62cec49416a83.png)

Remove the old 20 GB drive. You should now have only the 100 GB NVMe drive. Start the VM again and connect with PuTTY using your private key.

![PuTTY session connected to the Debian VM after the old SATA drive has been removed.](assets/images/file-62cec5fa198d3.png)

## Screenshot 4

Capture a PuTTY screenshot with the relevant output highlighted. There should be no `sda` device remaining, only the NVMe storage.

---
[Prev](04_moving-extents.md) | [Home](README.md) | [Next](06_snapshots.md)
