# Ensuring Security in iSCSI SANs

iSCSI runs over normal IP networking, so access control still matters.

## IP address ACLs

Access control lists can restrict which initiators are allowed to connect to a target. In this lab, the target is limited to the file server system you authorize.

## CHAP and Reverse CHAP

- **CHAP** authenticates the initiator to the target
- **Reverse CHAP** authenticates the target back to the initiator

These options are common in production iSCSI deployments, even though this lab focuses mainly on the connection workflow rather than hardening every security setting.

## Converged networking note

iSCSI is also a good example of storage traffic moving over standard Ethernet rather than a separate storage fabric. That is part of why SAN and general network traffic are often discussed together in modern infrastructure.

---
[Prev](02_navigating-iscsi-addresses-and-luns.md) | [Home](README.md) | [Next](04_submission-requirements-for-the-iscsi-san-lab.md)
