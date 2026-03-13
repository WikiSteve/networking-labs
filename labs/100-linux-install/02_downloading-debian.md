# Downloading Debian

Linux is distributed in many ways:

1. Full ISO images that include most packages and are usually several gigabytes in size.
2. Net install images, which include just enough to start the installation and then pull the rest from the internet.
3. Prebuilt images such as Docker containers or ready-made virtual machines.

This lab uses option 2: a Debian net install ISO.

[Installing Debian via the Internet](https://www.debian.org/distrib/netinst#smallcd)

![Debian download page showing the processor architecture choices, with AMD64 highlighted as the correct netinst download.](assets/images/file-62bb7334e8d60.png)

Follow the link above, select **AMD64**, and download the Debian netinst ISO.

> [!NOTE]
> The original source material used **debian-11.3.0-amd64-netinst.iso**. If the current Debian release is newer, that is fine.

## Configuring Virtual Machine

![Illustration introducing the virtual machine hardware configuration section.](assets/images/file-62bb76d007d48.png)

Configuring Virtual Machine hardware

![VMware Workstation window before creating a new virtual machine.](assets/images/file-62bb788f02f7e.png)

Create a new VM

![VMware New Virtual Machine Wizard welcome screen asking which configuration type to use.](assets/images/file-62bb78f447e9a.png)

Create a new VM

![VMware wizard screen for choosing the virtual machine hardware compatibility level.](assets/images/file-62bb79324afbf.png)

![VMware wizard guest operating system installation screen with the Debian ISO selected.](assets/images/file-62bb79ebd87c8.png)

Select the installer ISO and let VMware detect the Debian version automatically.

> [!NOTE]
> It is usually best to choose the option to install the operating system later, because VMware may otherwise try to perform an unattended install.

Create a new VM

![VMware wizard screen for selecting the guest operating system family and version.](assets/images/file-62bb7a9d2f074.png)

![VMware wizard screen for entering the virtual machine name SSharpe-Debian.](assets/images/file-62bb7b627caa9.png)

Name the machine **before** selecting a location on your hard drive.

Use **first initial + last name + `-Debian`** for the VM name. In the example screenshots, Steve Sharpe becomes **SSharpe-Debian**.

Create a new VM

![Browse for Virtual Machine Location window showing the legacy 22S Securing Linux folder from the original source material.](assets/images/file-62bb7c5fdeadc.png)

Store the VM in the directory where you keep your virtual machines. Create a clearly named subfolder so the Debian VM stays organized.

> [!WARNING]
> Several screenshots in this section still show the old folder name **22S Securing Linux** from the original source material. Treat that as a legacy example only and use your own organized folder name instead.

![VMware wizard summary of the virtual machine name and storage location, still showing the old 22S Securing Linux example path.](assets/images/file-62bb7ce42c795.png)

Create a new VM

![VMware processor configuration screen set to a single processor and single core.](assets/images/file-62bb9a51760f5.png)

Leave the VM configured with a single CPU and a single core.

Later labs can add more cores hot while the **VM is running**.

![Illustration accompanying the note that processor cores can be added later while the virtual machine is running.](assets/images/file-62bb9af481dff.jpg)

Create a new VM

![VMware wizard memory allocation screen for the new Debian virtual machine.](assets/images/file-62bba845d8ea6.png)

![VMware network type screen with NAT networking selected.](assets/images/file-62bba878a0687.png)

Create a new VM

![VMware I/O controller selection screen for choosing the SCSI controller type.](assets/images/file-62bba8c44e0b8.png)

Paravirtual drivers are part of the kernel now, which take much less CPU cycles when being used.

Create a new VM

![VMware disk type screen used to choose SCSI instead of NVMe for simpler device names.](assets/images/file-62bbaa4c3d9e1.png)

Just like paravirtualized drivers, NVMe is faster and takes less CPU. However, select SCSI because we will be working with disks and for the first few weeks we need the disks to be called something simple like `sda`, `sdb`, and so on. Feel free to reinstall with NVMe once you are confident in what you are doing.

![Illustration accompanying the explanation of why the lab uses SCSI disks instead of NVMe.](assets/images/file-62bbab14b8156.png)

Create a new VM

![VMware disk selection screen for creating a new virtual disk.](assets/images/file-62bbabf89a1ab.png)

![VMware disk size screen with a 20 GB disk and the option to split the virtual disk into multiple files.](assets/images/file-62bbac2781a7b.png)

Split the virtual disk into multiple files for two practical reasons:

1. On a spinning disk, smaller files are easier for the host OS to defragment than one huge monolithic file.
2. If you back up to older FAT32 media, you are less likely to hit the maximum file size limit.

Create a new VM

![VMware Ready to Create Virtual Machine summary showing the Debian VM name, location, memory, disk size, and NAT networking.](assets/images/file-62bbad30a642b.png)

Click **Customize Hardware**.

Create a new VM

![VMware Customize Hardware window listing the virtual hardware devices for the new VM.](assets/images/file-62bbadd2a4ea8.png)

Remove: Sound Card, Printer and USB Controller

Create a new VM

![VMware display settings screen with Accelerate 3D graphics unchecked.](assets/images/file-62bbae73b131b.png)

Confirm Accelerate 3D graphics is **unchecked**

Confirm VM configuration

![VMware virtual machine details page showing the final hardware profile and legacy 22S Securing Linux path.](assets/images/file-62bbafe35bd2a.png)

Only the listed hardware should be present. Nothing else.

Get organized!

![VMware Workstation menu path for displaying the VM Library through View, Customize, and Library.](assets/images/file-62bbb263c45ff.png)

Display the VM Library by going to View > Customize > Library

Get organized!

![VMware Workstation with the library pane visible and the SSharpe-Debian VM listed on the left.](assets/images/file-62bbb2f82b2c2.png)

You should now see your VM on the left. In the example screenshots, that VM is named **SSharpe-Debian**.

![VMware library view showing the context menu option to create a new folder under My Computer.](assets/images/file-62bbb47dc53c1.png)

Right-click **My Computer** and select **New Folder**.

Create a folder name that keeps your virtual machines organized. The screenshots still show the legacy example **22S Securing Linux**, but you should use a folder name that makes sense for your own setup.

Get organized!

![VMware library with the SSharpe-Debian VM moved into the old 22S Securing Linux folder.](assets/images/file-62bbb547667ce.png)

Drag your new VM into the folder you just created. Any new VMs you use for this course can be stored in the same location to keep everything organized.

## Screenshot 1

Your completed hardware profile. Make sure you have configured everything shown in the steps above.

![Completed VMware hardware profile for the Debian virtual machine, including NAT networking and the attached installer ISO.](assets/images/file-62bbbcef2c467.png)

---
[Prev](01_evaluation.md) | [Home](README.md) | [Next](03_starting-debian-installer.md)
