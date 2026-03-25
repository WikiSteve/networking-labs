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

Examples:

- if the host-only network is `172.16.99.0/24`, use `172.16.99.200`
- if the host-only network is `192.168.239.0/24`, use `192.168.239.200`

Do not use VMware-reserved addresses such as:

- `.1`
- `.254`

You can finish the `DMZ` IP, DHCP scopes, reservation, port forward, interface renaming, and GUI hardening in the web interface.

## Step 8. Open the pfSense GUI from Your Host Computer

On your host computer, open a web browser and browse to:

```text
https://<MGMT_IP>
```

Replace `<MGMT_IP>` with the `MGMT` address you chose, such as:

```text
https://172.16.99.200
```

You will likely get a certificate warning because pfSense uses a self-signed certificate by default.

Proceed past the warning and log in.

Common default credentials for a fresh pfSense install are:

- username: `admin`
- password: `pfsense`

If your course package gives you different credentials, use those instead.

If the GUI does not open:

- confirm the pfSense `MGMT` adapter is on the VMware `host-only` network
- confirm your host computer has an IP on that same `host-only` network
- confirm you used `.200` on the correct subnet
- confirm pfSense is fully booted

There is no required screenshot on this page beyond the MAC-address table.

---
[Prev](01_overview-and-vmware-prep.md) | [Home](README.md) | [Next](03_inspect-wan-rules-and-nat.md)
