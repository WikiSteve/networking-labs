# Linux Networking

- Filename: `Linux Networking.pptx`
- Subject: `systems`
- Type: `lecture`
- Reusable: `yes`
- Source file: [Source copy](../../sources/Linux%20Networking.pptx)

## Summary

This reusable lecture deck introduces Linux networking administration by framing the shift from the deprecated `net-tools` utilities to the modern `iproute2` toolkit, while also using that transition to teach Debian path behavior, binary locations, and interface naming. The instructional core compares familiar legacy commands like `ifconfig`, `route`, `arp`, and `netstat` with their modern replacements, especially `ip` and `ss`, and explains that `net-tools` is deprecated even though it can still be installed. The deck then uses a practical Debian quirk, regular users lacking `/usr/sbin` in their `PATH`, to teach why `ifconfig` may exist but not run unless called with an absolute path, which becomes a springboard into the Filesystem Hierarchy Standard and shell-profile path logic.

## Key Details

- Starts by contrasting old `net-tools` commands such as `ifconfig`, `route`, `arp`, and `netstat` with modern replacements in `iproute2` and `ss`.
- Explicitly states that `net-tools` has been deprecated, though it can still be installed for legacy use.
- Uses a Debian exercise to check whether `net-tools` is installed, locate `ifconfig` with `whereis`, and run it using the absolute path because `/usr/sbin` is not in the normal user `PATH`.
- Uses that path problem to teach `PATH` behavior, including the point that on Debian only root typically gets `/usr/sbin` by default.
- Introduces the Filesystem Hierarchy Standard through common binary locations such as `/bin`, `/sbin`, `/usr/bin`, and `/usr/sbin`.
- Includes a shell-profile challenge that asks readers to adjust an `if` statement so both root and their own account get access to `/usr/sbin`.
- Explains why `iproute2` exists, tying it to Linux kernel networking redesign after version 2.2 and the need for advanced networking features.
- Connects Linux networking to concepts often associated with Cisco courses, including OSPF, BGP, QoS, port bonding, STP, and VPNs.
- Explains that many networking changes made with either `net-tools` or `iproute2` are real-time only and disappear on reboot unless stored in configuration files.
- Ends with lab directions to make a `sudoers` change, use `net-tools` in bridged mode, and use `iproute2` in NAT mode.
- Explains old versus predictable interface names, contrasting `eth0` and `eth1` with names like `ens33`.
- Uses the VMware example of `ens33` to keep the deck grounded in virtualized classroom environments.

## Tags

- `linux-networking`
- `iproute2`
- `net-tools`
- `ss`
- `path`
- `filesystem-hierarchy-standard`
- `interface-naming`
- `debian`
