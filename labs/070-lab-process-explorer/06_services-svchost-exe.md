# Services: svchost.exe

## SVCHOST.EXE

Note that there a several instances of a process named **svchost.exe** as child processes of **winnit.exe & services.exe**

Move the mouse pointer over each **svchost.exe** process to display its intended purpose

The first instance provided Distributed Communications (Dcom), Plug & Play and hosts **WmiPrvSE.exe**

The second instance supports End point mapper services for Remote Procedure Calls (RPC)

Right click and in **Properties** view the **Services, Threads and TCP/IP** tabs

Move down the list to observe the many services being hosted by the different instances of this process:

DCHP, NetBIOS, DNS, Windows Firewall

---
[Prev](05_malware-tini.md) | [Home](README.md) | [Next](07_services-lsass.md)
