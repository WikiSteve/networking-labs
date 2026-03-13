# Services: svchost.exe

## SVCHOST.EXE

Note that there are several instances of a process named **svchost.exe** as child processes of **wininit.exe** and **services.exe**.

Move the mouse pointer over each **svchost.exe** process to display its intended purpose

The first instance provides Distributed COM (DCOM), Plug and Play, and hosts **WmiPrvSE.exe**.

The second instance supports Endpoint Mapper services for Remote Procedure Call (RPC).

Right click and in **Properties** view the **Services, Threads and TCP/IP** tabs

Move down the list to observe the many services being hosted by the different instances of this process:

DHCP, NetBIOS, DNS, Windows Firewall

---
[Prev](05_malware-tini.md) | [Home](README.md) | [Next](07_services-lsass.md)
