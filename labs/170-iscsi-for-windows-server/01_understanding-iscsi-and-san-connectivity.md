# Understanding iSCSI and SAN Connectivity

## What is a SAN?

A Storage Area Network (SAN) is a dedicated network that provides block storage to servers. The operating system treats that storage as if it were a locally attached disk.

## Why use iSCSI?

iSCSI carries SCSI storage traffic over standard IP networks. That makes it practical for lab environments because it avoids dedicated Fibre Channel hardware.

Key points:

- iSCSI uses Ethernet and normal IP networking
- the client machine is the **initiator**
- the storage server is the **target**
- the storage exposed by the target is presented as one or more **LUNs**

## What this lab is doing

In this lab:

1. `lastname-SAN` acts as the iSCSI target server
2. `lastname-FS` acts as the iSCSI initiator
3. storage is created on `lastname-SAN`
4. that storage is published over iSCSI
5. `lastname-FS` connects to it and formats the new disks

---
[Home](README.md) | [Next](02_navigating-iscsi-addresses-and-luns.md)
