# Install pfSense and Reach the GUI

## Step 4. Build the pfSense VM

Create the pfSense VM in VMware Workstation.

Use a simple FreeBSD-compatible guest profile, such as:

- latest FreeBSD `64-bit`

Use practical settings for this lab:

- `4` CPU cores
- `2 GB` RAM
- default virtual disk/controller options

Keep the hardware simple:

- do not rely on 3D graphics
- no extra hardware is needed for this lab beyond the network adapters and ISO

## Step 5. Add the Four NICs in the Correct Order

Before you install pfSense, add four NICs in this exact order:

1. VMware `NAT` network for `WAN`
2. LAN Segment `inside` for `LAN`
3. LAN Segment `dmz` for `DMZ`
4. VMware `host-only` network for `MGMT`

Start the VM once so VMware writes the MAC addresses, then shut it back down if needed.

Open **Settings** for the pfSense VM and record the MAC address for each adapter.

Make a simple table with columns like these:

- VMware adapter number
- VMware network or LAN Segment
- MAC address
- intended pfSense role

Your completed table should map all four adapters to these roles:

- `WAN`
- `LAN`
- `DMZ`
- `MGMT`

You will use this table during pfSense interface assignment.

## **Screenshot 1: MAC Address Mapping Table**
**Requirement:** Show your completed MAC-address mapping table with all four pfSense NICs mapped to `WAN`, `LAN`, `DMZ`, and `MGMT`.

## Step 6. Install pfSense CE

Download the course pfSense ISO if you do not already have it:

- [netgate-installer-v1.1.1-RELEASE-amd64.iso](https://nscc-my.sharepoint.com/:u:/g/personal/w0305390_campus_nscc_ca/IQDunpCC1QGuT7FF77ut-_rPAZnwMuk3eGjNFix-bCpAtrs)

Attach the pfSense ISO and boot the VM.

During the install:

- choose the Community Edition install path
- accept the normal defaults unless your screen clearly requires something different

The important part is the interface assignment after boot.

Match the console interface names such as `em0`, `em1`, `em2`, and `em3` to your MAC-address table.

Assign:

- `WAN`
- `LAN`
- `OPT1` for the future `DMZ`
- `OPT2` for the future `MGMT`

At the console, pfSense will not show friendly names such as `DMZ` and `MGMT` yet.

You will rename:

- `OPT1 -> DMZ`
- `OPT2 -> MGMT`

later in the GUI.

## Step 7. Do the Minimum Console Configuration

Use the pfSense console only enough to get the firewall online and reachable.

Configure these first:

- `WAN = DHCP`
- `LAN = 10.10.10.200/24`
- `OPT2 = <host-only subnet>.200/24` for the future `MGMT`

Use the current VMware `host-only` subnet you discovered in Step 0 of the lab.

If you are not sure what that subnet is anymore, stop and re-check the VMware `vmnet1` details before you guess.

Examples:

- if the host-only network is `172.16.99.0/24`, use `172.16.99.200`
- if the host-only network is `192.168.239.0/24`, use `192.168.239.200`

Do not use VMware-reserved addresses such as:

- `.1`
- `.254`

You can finish the `DMZ` IP, DHCP scopes, reservation, port forward, interface renaming, and GUI hardening in the web interface.

## Step 8. Open the pfSense GUI from Your Host Computer

On a fresh install, do **not** assume the first reachable GUI path is already `MGMT`.

For this lab, treat these as two different ideas:

- the **early fresh-install GUI path**
- the **final hardened management path**

On a fresh pfSense install, the web GUI is often still reachable on the broader default interface set.

In practice, that means your first successful browser path may be the current `WAN` address, not `MGMT` yet.

Later in the lab, you will deliberately harden the GUI so it is reachable only from `MGMT`.

Why this warning is here:

- `MGMT` starts life as an `OPT`-style interface
- students sometimes lose the GUI later by editing the wrong optional interface or changing the wrong field while renaming `OPT2 -> MGMT`
- if the GUI works now and later disappears, the problem is usually a later interface or GUI-hardening change, not the original install itself

On your host computer, open a web browser and browse to:

```text
https://<CURRENT_PFSENSE_GUI_IP>
```

On a fresh install, try these in this order:

- the current `WAN` IP if the host and pfSense share the VMware `NAT` network during setup
- the `MGMT` IP if you have already confirmed the `host-only` path is correct

Examples:

```text
https://172.16.171.129
https://172.16.99.200
```

You will likely get a certificate warning because pfSense uses a self-signed certificate by default.

Proceed past the warning and log in.

Common default credentials for a fresh pfSense install are:

- username: `admin`
- password: `pfsense`

If your course package gives you different credentials, use those instead.

If the GUI does not open:

- confirm which IP you are actually supposed to be testing first:
  - the current `WAN` IP on a fresh install
  - or the intended `MGMT` IP if you are specifically testing the host-only path
- confirm the pfSense `MGMT` adapter is on the VMware `host-only` network
- confirm your host computer has an IP on that same VMware `vmnet1` `host-only` network
- confirm you used `.200` on the correct subnet
- confirm pfSense is fully booted
- confirm your MAC-address mapping table still says the `host-only` NIC is the future `MGMT` interface

If ARP works but `ping` and `HTTPS` do not, do **not** assume pfSense is totally dead.

That usually means:

- the NIC is still present on the right layer-2 segment
- but the wrong interface has the IP
- or the intended `MGMT` interface lost its IP
- or you are no longer reaching the interface you think you are

Before you keep changing settings, jump to:

- [06 Troubleshooting](06_troubleshooting.md)

If all of those are correct and the GUI still does not open on `MGMT`, take a VMware snapshot and stop to ask for help before you keep changing settings.

Some pfSense builds are pickier than others about the initial management path before the GUI hardening step later in the lab.

There is no required screenshot on this page beyond the MAC-address table.

---
[Prev](01_overview-and-vmware-prep.md) | [Home](README.md) | [Next](03_inspect-wan-rules-and-nat.md)
