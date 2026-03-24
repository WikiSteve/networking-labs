# Verify Hosts and Open pfSense

## Step 1. Start the VMs and Verify the Debian Hosts

Power on:

- `pfSense`
- `outside`
- `inside`
- `dmz`

Use the VMware Workstation console to access:

- `outside`
- `inside`
- `dmz`

Open the console tab for each VM in VMware Workstation.

You will need the Debian username and password that came with your lab package. If you do not have those credentials yet, stop here and get them before continuing.

On `outside`, run:

```bash
hostname
ip -4 addr show
ip route show default
curl http://192.168.50.10
```

On `inside`, run:

```bash
hostname
ip -4 addr show
ip route show default
curl http://10.0.1.10
```

On `dmz`, run:

```bash
hostname
ip -4 addr show
ip route show default
curl http://10.0.2.10
```

Validate:

- `outside` shows address `192.168.50.10/24`
- `inside` shows address `10.0.1.10/24`
- `dmz` shows address `10.0.2.10/24`
- `outside` shows default gateway `192.168.50.1`
- `inside` shows default gateway `10.0.1.1`
- `dmz` shows default gateway `10.0.2.1`
- each VM shows the correct local Nginx page

Why this matters:

- this confirms that each VM is on the expected network
- this confirms that each VM has the expected static IP and gateway
- this confirms that Nginx is running before you test traffic between zones

## Step 2. Open the pfSense Web Interface from Your Host Computer

On your host computer, open a web browser.

Browse to:

```text
https://172.16.99.254
```

You will likely see a certificate warning because pfSense uses a self-signed certificate by default.

Proceed past the warning and log in with the pfSense credentials provided with your lab files.

Common browser behavior:

- Chrome or Edge: click **Advanced**, then continue to the site
- Firefox: click **Advanced**, then **Accept the Risk and Continue**
- if Chrome does not show a clear continue link, click the page and type `thisisunsafe`

Common default credentials for a fresh pfSense install are:

- username: `admin`
- password: `pfsense`

If your lab package includes different credentials, use the lab credentials instead.

If the page does not open:

- confirm your host computer has a `VMnet2` adapter in `172.16.99.0/24`
- confirm pfSense `MGMT` is attached to `VMnet2`
- confirm pfSense is powered on
- confirm you typed `https://172.16.99.254`

Why this matters:

- pfSense management is happening on the dedicated `MGMT` network
- the firewall web interface is not being managed from `WAN`

## Step 3. Identify `WAN`, `LAN`, `DMZ`, and `MGMT`

In pfSense, start with:

- `Status > Interfaces`

If your build does not show that exact menu path, use the pfSense search box and search for `Interfaces`.

Find:

- which interface is `WAN`
- which interface is `LAN`
- which interface is `DMZ`
- which interface is `MGMT`
- the IP address on each one

If one of the interfaces still shows a generic name such as `OPT1` or `OPT2`, also inspect:

- `Interfaces > Assignments`

Use that page only to confirm which VMware NIC is mapped to which pfSense interface name.

Validate:

- `WAN` is on `192.168.50.0/24`
- `LAN` is on `10.0.1.0/24`
- `DMZ` is on `10.0.2.0/24`
- `MGMT` is on `172.16.99.0/24`

## **Screenshot 1: pfSense Interfaces**
**Requirement:** Show the pfSense interface view with `WAN`, `LAN`, `DMZ`, and `MGMT` visible and their IP addresses readable.

---
[Prev](01_overview-and-vmware-prep.md) | [Home](README.md) | [Next](03_inspect-wan-rules-and-nat.md)
