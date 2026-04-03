# Network prep

![Addressing worksheet for the NAT segment showing the required .200 server and .201 client host assignments.](assets/images/file-62d831f225546.png)

Configure both computers to match the topology diagram using static IP assignments. On Debian, you can configure static IPs by editing **`/etc/network/interfaces`** or using the **`ip`** command. Set the server interface to **`192.168.90.200`** and the client interface to **`192.168.90.201`**. Set the client's default gateway to point to the server (**`192.168.90.200`**).

The computers should be able to ping each other. The client computer, once finished, should **NOT** be able to reach the internet anymore.

![Client ping by hostname confirming the server resolves correctly and the default route points to the server.](assets/images/file-62d83ce350881.png)

## **Screenshot 3: Topology Verification**
**Requirement:** Prove everything has been setup correctly. You must be able to ping the server by hostname, and the default route must point to the server.

---
[Prev](04_renaming-linux-machines.md) | [Home](README.md) | [Next](06_routing.md)
