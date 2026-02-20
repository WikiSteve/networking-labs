# Legacy networking

The base install of Debian does not have any managers **by default**. You're free to install **any manager **of your choice however.

You'll encounter this on a few distributions and on others they'll come bundled with Network Manager, Netplan or any other manager.

For this edition of Securing Linux we'll just be looking at the legacy networking, however if you're up for the challenge read about the other managers.

All the IP configurations are stored in **`/etc/network/interfaces`**. Start by taking a look at these:

![[assets/images/file-62d0338a165da.png]]

The first line reads `allow-hotplug`, which does two things:
- The system should run the directive below whenever the cable status changes (plugged in, unplugged).
- It shouldn't hang and wait for DHCP during startup.

The second line breakdown:
- `iface` is interface
- `ens32` is the interface name
- `inet` is IPv4 (use `inet6` for IPv6)
- `dhcp` is the method

We're going to set this to a static IP. I've blurred out the IP addresses but left everything else; make sure to use your spreadsheet to sub in the correct values. Set the HOST portion to `.200`.

![[assets/images/file-62d0362946ba0.png]]

Since we're not using DHCP, you'll need to set the nameserver (DNS) manually. Go to **`/etc/resolv.conf`** and update the record to be the correct nameserver. If DNS fails upon restart, this will be your first place to check!

![[assets/images/file-62d037110dd5b.png]]

![[assets/images/file-62d037f91503f.png]]

If it doesn't work, re-enable hotplug (I previously commented it out) and restart the whole VM.

## **Screen shot 2 must contain all three parts highlighted in red on a single screenshot. Restarting the service must produce zero errors.**

![[assets/images/file-62d03a728b007.png]]

## **Screen shot 3 Prove connection works with PuTTY. Capture your servers IP and a successful ping.**

---
[Prev](04_live-tools-iproute2.md) | [Home](README.md)
