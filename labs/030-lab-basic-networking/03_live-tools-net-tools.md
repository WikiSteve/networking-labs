# Live tools: net-tools

There are two live sections: **`net-tools`** and **`iproute2`**. "Live" means you can see the status of the system and make non-permanent changes that are lost upon restart.

**`net-tools`** is deprecated; however, it's important to know its usage because many experienced administrators still "think, breathe, and speak" **`net-tools`**. They may look like a deer in headlights when you mention **`iproute2`**. Imagine how long it's taken the industry to migrate to IPv6—that is how long it's going to take **`net-tools`** veterans to retire.

> [!NOTE]
> Because some commands will intentionally disrupt your connection, I suggest connecting directly to the VMware console for the live tools sections, as your PuTTY connection may drop unexpectedly.

Start by installing **`net-tools`**:
**`sudo apt install net-tools`**

Begin a spreadsheet with the following columns:
- **IP address**
- **MAC address**
- **Vendor**
- **Network**
- **Description**

Set your VM to **bridged mode**. The behaviour you experience may differ depending on whether you are using a wired or wireless connection and your specific chipset (Broadcom, Realtek, Intel, etc.). This is because some drivers allow multiple MACs per connection and support MAC address cloning while others do not. Bridged works in both environments, but the results vary.

![[assets/images/file-62d00275d704f.png]]

Open the **Virtual Network Editor** by going edit > Virtual Network Editor in Workstation.

![[assets/images/file-62d0031cd0b6e.png]]

By default VMNet0, which is also set to bridge by default, is set to select the adapter automatically. It selects the interface that is up and has at least passed layer 1/2 connectivity. If you have multiple adapters in the up state, such as connected via wired and wireless, you may get unexpected behaviour. If you have a single active connection right now, leave it as automatic.

If you have both wired and wireless options, you could:
- Keep both active but manually switch between them in this console.
- Disconnect the one you don't want to use.

Knowing this information, you may close this window.

Start by looking at the interfaces you have available by issuing **`ifconfig`**. Because this file is not in the users path, you'll need to use **`sudo`**, even though just viewing this information isn't privileged.

![[assets/images/file-62d0087fab73e.png]]

You should recognize the adapter with 127.0.0.1, this is your loopback.  The adapter we're interested in however is the adapter that will look similar to ens32, yours may be different but as long as you're not looked at the loopback adapter we're good!

Highlighted is the adapter name ens32, the MAC address and IPv4 address. 

To make sure this is the correct address, just turn the interface OFF then back ON:

- Turning off: **`sudo ifdown [interface name]`**
- Turning on: **`sudo ifup [interface name]`**

Wait at least 60 seconds for ARP to age out. ARP cache life is configurable; on this system it's 60 seconds, and yours is likely the same. The screenshot below is the output of my current ARP cache timeout.

![[assets/images/file-62d009bd4c6dd.png]]

Once a whole minute or two goes by, run **`sudo arp -a`**. It should be blank!

![[assets/images/file-62d00a3062819.png]]

Now run a ping to `google.ca`. If you have one of those NICs that don't support cloning and multiple MACs, you'll get a flood of `DUP!` messages. To make the output more useful, I've limited the ping to 2; because the duplicate is on the same system and I have promiscuous mode enabled, my system detected a ton of duplicates.

**`ping -c 2 google.ca | head`**

![[assets/images/file-62d00e659d777.png]]

Because your ARP cache is aging, run **`sudo arp -a`** quick like a bunny.

![[assets/images/file-62d00f28e3132.png]]

In this example I have both my host at 192.168.2.134 & my router at 192.168.2.254.  This is because my Intel Wireless NIC does not support cloning so to get to Google I had to 'borrow' the hosts MAC to get out.  If your NIC supports cloning you likely will not see your host and just your router.

The MAC address in this example for 192.168.2.134 is 34:e1:2d:5f:05:50.  The first three pairs in red are the organizational unit (vendor) the last three pairs are unique for that vendor.  You can use just the red part, or paste the entire part into a database to discover the vendor.

Use the link below to discover the vendor to all the devices that showed up in arp.

Use this information to populate your spreadsheet.

[MAC OU lookup](https://aruljohn.com/mac.pl)

![[assets/images/file-62d0133673d74.png]]

I just happened to know that 192.168.2.254 is my router. Do not assume, let's find out.

Run both **`sudo route`** then **`sudo route -n`**.

The first one does a reverse DNS lookup using your home router for its name; in my case, it's `squrrelHQ.wikisteve.com`.
The second one tells route not to do reverse lookups.

![[assets/images/file-62d0148fce1c1.png]]

So we can tell this router provides NAT; this is our default gateway. On your spreadsheet, modify the description for the router to state that it performs NAT. The description should say **`router: NAT`**.

> [!NOTE]
> This part is not strictly a feature of **`net-tools`**, but is an essential part of our discovery phase.

Now let's see who handles DNS for your network. View your resolver configuration in **`/etc/resolv.conf`**:

**`cat /etc/resolv.conf`**

![[assets/images/file-62d0166fd5b85.png]]

If the nameserver portion is the same as your router, change your description now to **`router: NAT, DNS`**.

If it is NOT the same as your router, leave it as **`router: NAT`**, then add a new line with your nameserver IP. Leave the MAC address and Vendor columns blank and put **`DNS`** under the description.

Last, we need to see who handles your DHCP. Turn the interface off again and note which device your system is communicating with to obtain this lease.

![[assets/images/file-62d01825c639c.png]]

If the IP address is the same as the router, update the description to **`router: NAT, DNS, DHCP`** if it performs all three roles.

If the DHCP server is different, you're likely on a campus or corporate network. Due to the nature of DHCP relay, it may be on a different network. If it's on a **different network**, state the IP address and leave the MAC and vendor columns blank. If you're unsure, see if it appears in ARP; if it does, it's on your local network.

Next part is traceroute which also isn't part of net-tools but we're doing all the discovery needed while bridged. Remember your interface is down, bring it up first.

**`traceroute google.ca | head`**

![[assets/images/file-62d01b36e19c3.png]]

In my example I have two routers that are internal because both 192.168.2.0/24 and 192.168.1.0/24 are private IP addresses. If you're unsure what is a private IP address make sure to review them. If you have a single router just leave the description as router. If you have two determine which one is inside, and which is outside.

The first one will be inside which in my case is 192.168.2.254 is inside router and 192.168.1.1 is the outside router. We're not concerned about what services it has, just make a note of it in the spreadsheet, see the example below.

![[assets/images/file-62d01cce6ff6c.png]]

Lastly set a static IP address to anything you desire then test with your Windows 11 computer that you can reach it with PuTTY.

To set a static IP with net-tools is crazy easy with **`ifconfig [interface] IP/CIDR`**.

As an example if I want to set 192.168.2.202/24 it is **`sudo ifconfig ens32 192.168.2.202/24`**

![[assets/images/file-62d01de8f3498.png]]

Reboot the system before proceeding to the next step.

---
[Prev](02_vmware-adapter-types.md) | [Home](README.md) | [Next](04_live-tools-iproute2.md)
