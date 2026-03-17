# Lab DHCP, ARP, DNS, and Static IP Setup

- Filename: `Lab DHCP, ARP, DNS, and Static IP Setup.docx`
- Subject: `networking`
- Type: `lab`
- Reusable: `yes`
- Source file: [Source copy](../../sources/Lab%20DHCP%2C%20ARP%2C%20DNS%2C%20and%20Static%20IP%20Setup.docx)

## Summary

This reusable networking lab teaches core IPv4 client networking through live packet capture, manual addressing, and protocol analysis in a bridged VMware Workstation environment. Learners switch a VM from NAT to Bridged mode, manually bind Bridged networking to the active physical adapter, and then use Wireshark to capture DHCP DORA traffic, ARP resolution, and DNS queries while also using Windows tools such as `ipconfig /all`, `ping`, and `nslookup`. The lab then walks through choosing a safe static IP address by checking for conflicts with both ICMP and ARP evidence, explains three distinct conflict-test outcomes, and has learners apply a static IPv4 configuration using the same subnet mask, gateway, and DNS settings as their DHCP lease.

## Key Details

- The lab starts with VMware Workstation setup: power off the VM, change networking from NAT to Bridged, and bind Bridged mode to the real active adapter.
- It explains why automatic Bridged selection is often wrong and can prevent proper LAN participation.
- Part 1 captures DHCP DORA traffic by disabling and re-enabling the Windows network adapter while Wireshark is running.
- The DHCP capture uses the `bootp` display filter because Wireshark groups DHCP under BOOTP.
- There is a live instructor checkpoint for identifying Discover, Offer, Request, and Acknowledge.
- The ARP section generates traffic by pinging an IP address not yet contacted and then locating ARP request and reply packets with the `arp` filter.
- `ipconfig /all` is used to collect the IPv4 address, subnet mask, default gateway, and DNS servers.
- For static IP selection, learners choose a nearby unused address and test it with `ping` while watching Wireshark with the filter `arp or icmp`.
- The lab documents three conflict-detection outcomes: successful ping, timeout with ARP reply, and destination host unreachable with no ARP reply.
- It explicitly frames this as a manual form of Duplicate Address Detection.
- Static IP configuration is done through IPv4 properties while reusing the same mask, gateway, and DNS values from DHCP.
- The DNS section uses `nslookup example.com` and the `dns` Wireshark filter, with an optional comparison of TCP versus UDP behavior based on captured traffic.

## Tags

- `dhcp`
- `arp`
- `dns`
- `static-ip`
- `wireshark`
- `vmware-workstation`
- `bridged-networking`
- `tcp-vs-udp`
