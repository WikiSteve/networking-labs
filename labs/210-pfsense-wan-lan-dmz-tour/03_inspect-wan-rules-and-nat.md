# Configure pfSense in the GUI

## Step 9. Rename the Interfaces and Finish the IP Plan

If you forget which VMware network or LAN Segment belongs to each pfSense interface, jump back to the topology map in page 01.

Use the diagram below for a different purpose:

- this one is the address and service reference
- it is here to help while you set interface IPs, DHCP, the `DMZ` reservation, and the public-vs-internal service behavior
- it is not the same as the page 01 connection map

![Address and service reference diagram showing pfSense with WAN from NAT, LAN 10.10.10.200/24 to the inside client DHCP range, DMZ 10.20.20.200/24 to the dmz host reservation 10.20.20.100 with port 80 public and port 8080 internal only, and MGMT on the host-only network to the host computer.](assets/images/pfsense-addressing-services.png)

Diagram source: [Mermaid](assets/images/pfsense-addressing-services.mmd)

In the pfSense GUI, use:

- `Interfaces > Assignments`
- the individual interface pages under `Interfaces`

If your extra interfaces still show up as `OPT1` and `OPT2`, rename them now:

- `OPT1 -> DMZ`
- `OPT2 -> MGMT`

On the `DMZ` and `MGMT` interface pages, make sure each interface is enabled.

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

> [!CAUTION]
> **Do this or your `WAN` tests can silently fail.**
>
> VMware `NAT` uses a private RFC1918 subnet, and your pfSense `WAN` interface
> and `outside` VM both sit on that private subnet.
>
> If you leave `Block private networks and loopback addresses` enabled,
> pfSense can drop `outside -> WAN` traffic before your port forward or block
> rule is ever evaluated. Your rules can look correct and still do nothing.
>
> Disable it on `WAN`, then save and apply the change.

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
- `DMZ DHCP = 10.20.20.101 - 10.20.20.149`

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

Before you change the GUI listen interface, take a VMware snapshot of the pfSense VM.

Why:

- this is the riskiest configuration step in the lab
- if you make a mistake, you can revert to a known working state instead of rebuilding the firewall from the beginning

Before you move the GUI to `MGMT`, create the `MGMT` firewall rule that will let your host computer reach it.

In pfSense, open:

- `Firewall > Rules > MGMT`

Add a pass rule with these values:

- action: `Pass`
- protocol: `TCP`
- source: `MGMT net`
- destination: `MGMT address`
- destination port: `HTTPS`

Save and apply the rule.

Why this matters:

- `MGMT` is an OPT-style interface
- new OPT-style interfaces do not get open firewall rules by default
- if you move the GUI to `MGMT` first and do not add this rule, you can lock yourself out

Before you harden the GUI, move to the `inside` VM and open one terminal window.

In that same terminal, run:

```bash
hostname
curl -kI https://10.10.10.200
```

You should see HTTP headers.

Leave this terminal open. Do **not** clear it.

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
- keep both results visible in the same terminal window for Screenshot 3

From your host computer, confirm the GUI still opens on:

```text
https://<MGMT_IP>
```

## **Screenshot 3: GUI Access Before and After Hardening**
**Requirement:** In one screenshot, show the `inside` VM hostname, one successful `curl -kI https://10.10.10.200` result before hardening, and one failed attempt after the GUI is restricted to `MGMT` only. Keep both results visible in the same terminal window.

---
[Prev](02_verify-hosts-and-open-pfsense.md) | [Home](README.md) | [Next](04_test-and-prove-traffic.md)
