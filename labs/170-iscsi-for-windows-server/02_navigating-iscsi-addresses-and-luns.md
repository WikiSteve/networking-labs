# Navigating iSCSI Addresses and LUNs

## iSCSI address

An iSCSI endpoint is identified by an iSCSI Qualified Name, often shortened to **IQN**. The IQN uniquely identifies an initiator or target.

Example format:

- `iqn.2001-04.com.example:storage.disk1`

## LUNs

A Logical Unit Number (**LUN**) identifies a logical storage device presented by the target. One target can expose multiple LUNs.

In practical terms for this lab:

- the Windows Server iSCSI target will present storage to `lastname-FS`
- each virtual disk you publish through the target behaves like a separate storage object
- the initiator sees those disks and can initialize and format them

## Why this matters

The target name gets you to the correct iSCSI endpoint. The LUNs are the actual storage items you connect to and use.

---
[Prev](01_understanding-iscsi-and-san-connectivity.md) | [Home](README.md) | [Next](03_ensuring-security-in-iscsi-sans.md)
