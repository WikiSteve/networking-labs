# LAB Bootable ISO Drive

- Filename: `LAB Bootable ISO Drive.docx`
- Subject: `systems`
- Type: `lab`
- Reusable: `yes`
- Source file: [Source copy](../../sources/LAB%20Bootable%20ISO%20Drive.docx)
- Submission template: [Bootable ISO Submission Template](../../templates/systems/bootable-iso-submission-template.md)

## Summary

This reusable hands-on lab teaches how to download the full Debian installation ISO, create a bootable USB flash drive with Rufus on Windows, and verify that the drive is actually bootable by attaching it to a VMware Workstation virtual machine and booting the Debian installer through UEFI. The lab is procedural rather than theoretical. It covers downloading the complete Debian DVD image from the official Debian site, using Make Me Admin for local elevation, writing the ISO to USB in Rufus with the correct settings, optionally checking the USB for bad blocks, creating a Debian 12.x VM in VMware Workstation, switching the VM firmware from BIOS to UEFI, connecting the USB device to the running VM, and booting the installer from that USB media.

## Key Details

- The objective is to create a bootable Debian USB with Rufus and validate it inside VMware Workstation.
- Required resources include internet access, a USB flash drive with at least 4 GB, and VMware Workstation.
- The lab points to the official Debian download page and recommends the complete 64-bit DVD-1 installation image.
- It includes a Windows privilege-escalation step using Make Me Admin before download and install work.
- Rufus setup requires selecting the USB device, choosing the downloaded Debian ISO, and naming the volume using the `First Initial, Lastname-Debian` pattern.
- The instructions recommend one pass of bad-block checking because the USB drives are old and may be unreliable.
- When Rufus detects an ISOHybrid image, the instructions require `Write in ISO Image mode (recommended)`.
- If Syslinux downloads are requested, the learner is told to allow Rufus to fetch them.
- The VMware section uses a custom VM configured as Debian 12.x 64-bit with the same student naming pattern.
- A key technical requirement is changing VM firmware from BIOS to UEFI so the USB boots properly.
- The USB device must be attached to the guest while the VM is already running.
- Submission evidence requires two screenshots: one of Rufus image creation and one of Debian booted in VMware Workstation from that USB media.

## Tags

- `debian`
- `bootable-usb`
- `rufus`
- `vmware-workstation`
- `uefi`
- `iso`
- `lab`
- `installation-media`
