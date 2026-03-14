# iSCSI for Windows Server

> **Before you start:** Download the [iSCSI for Windows Server Submission Template](<./assets/iSCSI for Windows Server SUBMISSION TEMPLATE.pptx>). Add each required screenshot directly into this file as you complete the lab, then submit the completed template for grading.

## Goal
Practice basic SAN concepts by creating storage on `lastname-SAN`, publishing it through the Windows Server iSCSI Target role, and connecting to it from `lastname-FS`.

## Prereqs
- Two Windows Server VMs named `lastname-SAN` and `lastname-FS`
- Network connectivity between the two servers
- `lastname-SAN` at `192.168.100.10`
- `lastname-FS` at `192.168.100.20`
- VMware access so you can add a new virtual disk to `lastname-SAN`

## Deliverables
- Complete the four required screenshots
- Use the submission template your instructor provides for this lab
- Show the storage tiers, completed iSCSI target, successful initiator connection, and final files placed on the mounted iSCSI volumes

## Pages
- [Understanding iSCSI and SAN Connectivity](01_understanding-iscsi-and-san-connectivity.md)
- [Navigating iSCSI Addresses and LUNs](02_navigating-iscsi-addresses-and-luns.md)
- [Ensuring Security in iSCSI SANs](03_ensuring-security-in-iscsi-sans.md)
- [Submission Requirements for the iSCSI SAN Lab](04_submission-requirements-for-the-iscsi-san-lab.md)
- [Preparing Storage Volumes](05_preparing-storage-volumes.md)
- [Setting Up the iSCSI Target on `lastname-SAN`](06_setting-up-the-iscsi-target-on-lastname-san.md)

## Accessibility

- [Screenshot alt text and OCR transcript data](assets/screenshot-ocr.json)
