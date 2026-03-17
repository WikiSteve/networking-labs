# Routing Assignment

- Filename: `Routing assignment.docx`
- Subject: `networking`
- Type: `lab`
- Reusable: `yes`
- Source file: [Source copy](../../sources/Routing%20assignment.docx)
- Submission template: [Static Routing Submission Template](../../templates/networking/static-routing-submission-template.md)

## Summary

This reusable static-routing and multi-network lab teaches how to build a small routed virtual network using Windows, Debian, and a web server VM across separate LAN segments. It provides five `/24` practice networks, then walks through creating two LAN segments in the virtualization platform, assigning adapters so Debian acts as a multi-homed router, configuring static IPs on each machine, enabling IPv4 forwarding on Debian with `sysctl`, and testing connectivity and isolation between segments. The document also includes both temporary and permanent Linux network configuration examples, plus a static route example using `ip route add` and an `/etc/network/interfaces` block with `up route add` and `down route del` commands.

## Key Details

- Defines five example routed networks from `192.168.10.0/24` through `192.168.50.0/24`.
- Step 1 has learners configure the Virtual Network Editor and create two LAN segments.
- Step 2 uses three VMs: Windows 10, Debian, and a web server.
- Debian is configured with three interfaces: Windows-side LAN, web-server LAN, and bridged college network using DHCP.
- Windows receives an address on the first LAN segment, while Debian and the web server receive static IPs.
- Routing is enabled on Debian with `sysctl -w net.ipv4.ip_forward=1`.
- The lab includes expected connectivity behavior for Windows, Debian, and the web server.
- A temporary Linux IP assignment example uses `ip addr add`.
- A permanent configuration example uses `/etc/network/interfaces` with static values and route add/delete hooks.
- A modern route example uses `ip route add 192.168.50.0/24 via 192.168.20.254`.
- The exercise reinforces the idea of a next hop and route persistence.
- The file is reusable as a practical VM networking and Linux routing guide.

## Tags

- `static-routing`
- `linux-routing`
- `ip-forwarding`
- `vmware-networking`
- `virtual-network-editor`
- `ip-route`
- `debian-router`
- `web-server`
