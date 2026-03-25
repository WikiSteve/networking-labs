# Configure pfSense in the GUI

## Step 9. Rename the Interfaces and Finish the IP Plan

In the pfSense GUI, use:

- `Interfaces > Assignments`
- the individual interface pages under `Interfaces`

If your extra interfaces still show up as `OPT1` and `OPT2`, rename them now:

- `OPT1 -> DMZ`
- `OPT2 -> MGMT`

Make sure you end up with these logical interface names:

- `WAN`
- `LAN`
- `DMZ`
- `MGMT`

Use these final addresses:

- `LAN = 10.10.10.200/24`
- `DMZ = 10.20.20.200/24`
- `MGMT = <host-only subnet>.200/24`
- `WAN = DHCP`

On the `WAN` interface page, disable:

- `Block private networks and loopback addresses`

Why:

- VMware `NAT` uses a private RFC1918 subnet
- your `outside` client is also on that private VMware `NAT` subnet
- if you leave that pfSense `WAN` setting enabled, the `outside -> WAN` tests can fail before your port forward or block rule is even considered

When this is done, use:

- `Status > Interfaces`

Record the current `WAN` IP. You will need it later when you test traffic from `outside`.

## **Screenshot 2: pfSense Interface Names and IP Addresses**
**Requirement:** Show `Status > Interfaces` with `WAN`, `LAN`, `DMZ`, and `MGMT` visible and their IP addresses readable.

## Step 10. Enable DHCP on `LAN` and `DMZ`

In pfSense, open:

- `Services > DHCP Server > LAN`
- `Services > DHCP Server > DMZ`

Use these exact ranges:

- `LAN DHCP = 10.10.10.100 - 10.10.10.149`
- `DMZ DHCP = 10.20.20.100 - 10.20.20.149`

## Step 11. Create the `DMZ` Reservation

On the `dmz` Debian VM, find the MAC address of the active NIC:

```bash
ip -br link
```

Ignore `lo`.

Use that MAC address to create a DHCP reservation in pfSense for the `dmz` host:

- IP address: `10.20.20.100`

After the reservation is in place, renew the `dmz` lease or reboot the VM.

If you want to renew from the shell instead of rebooting:

```bash
sudo dhclient -r
sudo dhclient
```

Do the same on `inside` if it still does not have a `10.10.10.x` address.

Validate:

- `inside` gets an address in `10.10.10.100 - 10.10.10.149`
- `dmz` gets `10.20.20.100`

## Step 12. Create the Public `WAN` Port Forward and the Blocked `WAN` Rule

For this lab, leave:

- `Firewall > NAT > Outbound`

on its default automatic mode.

In pfSense, create a port forward on:

- interface: `WAN`
- protocol: `TCP`
- destination: `WAN address`
- destination port: `80`
- redirect target IP: `10.20.20.100`
- redirect target port: `80`

When pfSense offers to create the associated filter rule, allow it.

Then add an explicit `WAN` block rule for:

- protocol: `TCP`
- destination port: `8080`
- logging enabled

This gives you a clean public-vs-internal-only proof later:

- `outside -> WAN:80` should work
- `outside -> WAN:8080` should fail

## Step 13. Harden the GUI to `MGMT` Only

Before you harden the GUI, move to the `inside` VM and test the current `LAN` GUI response:

```bash
curl -kI https://10.10.10.200
```

If that command does not return headers before hardening, stop and re-check:

- `LAN` is enabled
- `LAN` is really `10.10.10.200`
- the web interface is still listening on the default interfaces

Now go back to pfSense and open:

- `System > Advanced > Admin Access`

Set the webConfigurator listen interface so the GUI is reachable only on:

- `MGMT`

Save the change.

Then return to `inside` and run the same command again:

```bash
curl -kI https://10.10.10.200
```

Expected result:

- before hardening, the command returned HTTP headers
- after hardening, the command should fail, return connection refused, or time out

From your host computer, confirm the GUI still opens on:

```text
https://<MGMT_IP>
```

## **Screenshot 3: GUI Access Before and After Hardening**
**Requirement:** In one screenshot, show the `inside` VM hostname, one successful `curl -kI https://10.10.10.200` result before hardening, and one failed attempt after the GUI is restricted to `MGMT` only.

---
[Prev](02_verify-hosts-and-open-pfsense.md) | [Home](README.md) | [Next](04_test-and-prove-traffic.md)
