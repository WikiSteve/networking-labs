# Legacy Networking

The base install of Debian does not have any network managers **by default**. You're free to install **any manager** of your choice, however. You'll encounter this on a few distributions, while others come bundled with Network Manager, Netplan, or other tools.

For this edition of Securing Linux, we'll just be looking at legacy networking; however, if you're up for the challenge, feel free to read about other managers.

All IP configurations are stored in **`/etc/network/interfaces`**. Start by taking a look at these:

![[assets/images/file-62d0338a165da.png]]

The first line reads `allow-hotplug`, which does two things:
- The system runs the directive below whenever the cable status changes (link up/down).
- It prevents the system from hanging while waiting for DHCP during startup.

The second line breakdown:
- `iface`: Defines the interface.
- `ens32`: The name of the interface.
- `inet`: Specifies IPv4 (`inet6` would be used for IPv6).
- `dhcp`: Specifies the configuration method.

We're going to set this to a static IP. I've blurred out the IP addresses but left everything else; make sure to use your spreadsheet to sub in the correct values. Set the **HOST** portion to **`.200`**.

![[assets/images/file-62d0362946ba0.png]]

Since we're not using DHCP, you'll need to set the nameserver (DNS) manually. Go to **`/etc/resolv.conf`** and update the record to the correct nameserver. If DNS fails upon restart, this will be your first place to check!

![[assets/images/file-62d037110dd5b.png]]

![[assets/images/file-62d037f91503f.png]]

If it doesn't work, re-enable hotplug (if you previously commented it out) and restart the VM.

## **Screenshot 2: Configuration Verification**
**Requirement:** Capture all three parts highlighted in red on a single screenshot. Restarting the service must produce zero errors.

![[assets/images/file-62d03a728b007.png]]

## **Screenshot 3: Connection Proof**
**Requirement:** Prove the connection works with PuTTY. Capture your server's IP and a successful ping.

---
[Prev](04_live-tools-iproute2.md) | [Home](README.md)
