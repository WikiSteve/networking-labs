# Overview and VMware Prep

## Overview

In this lab, you will explore a prebuilt pfSense firewall with four interfaces:

- `WAN`
- `LAN`
- `DMZ`
- `MGMT`

You will use:

- your **host computer's web browser** for the pfSense web interface
- three **headless Debian** VMs for traffic testing

This lab is about understanding and proving the traffic flow, not about building the appliance from nothing.

## Learning Goals

By the end of this lab, you should be able to:

- identify the `WAN`, `LAN`, `DMZ`, and `MGMT` interfaces in pfSense
- explain the difference between a firewall rule and NAT / port forwarding
- prove why `outside` can reach the `DMZ` service
- prove why `outside` cannot reach a service that was not forwarded
- prove why `inside` can reach `outside`
- use pfSense rules, logs, NAT, and states as evidence

## What pfSense Is

pfSense is a firewall and router platform with a web interface.

For this lab, think of pfSense as the device in the middle that decides:

- what traffic is allowed
- what traffic is blocked
- what traffic is translated with NAT

## Key Ideas Before You Start

### `WAN`

`WAN` is the outside-facing network.

In this lab, the `outside` Debian VM lives on the WAN-side network.

### `LAN`

`LAN` is the internal network.

In this lab, the `inside` Debian VM lives on the LAN network.

### `DMZ`

A `DMZ` is a separate network used for systems that may need to be reachable from the outside.

In this lab, the `dmz` Debian VM hosts the web page that the outside machine will reach through a port forward.

### `MGMT`

`MGMT` is the management network.

In this lab, the `MGMT` interface exists so you can use your **host computer** to manage pfSense through a VMware host-only network instead of adding a separate GUI VM.

### Firewall Rule vs NAT

These are not the same thing.

- A firewall rule decides whether traffic is allowed or denied.
- NAT changes addresses or ports so the traffic reaches the correct internal host.

For this lab, `outside -> DMZ` works because pfSense uses:

- a `WAN` port forward
- and the matching rule that permits that forwarded traffic

### Important Rule Direction Idea

pfSense rules are evaluated on the interface where the traffic enters the firewall.

That means:

- traffic from `outside` enters on `WAN`, so `WAN` rules matter
- traffic from `inside` enters on `LAN`, so `LAN` rules matter

### State Table

pfSense is stateful.

That means pfSense keeps track of active connections. The **States** page helps prove what was allowed and how pfSense handled the session.

## Topology

| Device | Network | Example IP | Role |
| --- | --- | --- | --- |
| `pfSense WAN` | `192.168.50.0/24` | `192.168.50.1` | outside-facing interface |
| `pfSense LAN` | `10.0.1.0/24` | `10.0.1.1` | inside gateway |
| `pfSense DMZ` | `10.0.2.0/24` | `10.0.2.1` | DMZ gateway |
| `pfSense MGMT` | `172.16.99.0/24` | `172.16.99.254` | management interface |
| `outside` | `192.168.50.0/24` | `192.168.50.10` | external client |
| `inside` | `10.0.1.0/24` | `10.0.1.10` | internal server |
| `dmz` | `10.0.2.0/24` | `10.0.2.10` | DMZ web server |
| `host computer` | `172.16.99.0/24` | host adapter on `VMnet2` | pfSense management browser |

Each Debian VM hosts a tiny Nginx page:

- `outside`: `Hey I'm Outside`
- `inside`: `Hey I'm Inside`
- `dmz`: `Hey I'm DMZ`

For this lab, the Debian VMs use **static IPv4 addressing**:

- `outside`: `192.168.50.10/24`, gateway `192.168.50.1`
- `inside`: `10.0.1.10/24`, gateway `10.0.1.1`
- `dmz`: `10.0.2.10/24`, gateway `10.0.2.1`

## Before You Begin

For this lab, the environment is already built.

You do **not** need to:

- install pfSense
- assign interfaces from scratch
- build the Linux VMs from scratch
- install `nginx`

Your job is to inspect the setup, test the traffic flow, and explain the results.

## Step 0. Verify the VMware Networks Before You Boot the VMs

Open VMware Workstation and confirm the required virtual networks exist.

### LAN Segments

You need three LAN Segments:

- `outside`
- `inside`
- `dmz`

These are separate Layer 2 networks. There is no direct path between them unless pfSense routes the traffic.

If one of these LAN Segments does not exist yet:

1. Open a VM's **Settings** window.
2. Select **Network Adapter**.
3. Choose **LAN Segment...**
4. Create the missing segment name.
5. Repeat until `outside`, `inside`, and `dmz` all exist.

Use the exact same segment names on every VM.

LAN Segment names are case-sensitive. `Outside` and `outside` are two different networks.

### Host-Only Management Network

You also need VMware **`VMnet2`** for pfSense management.

In VMware Workstation, open:

- `Edit > Virtual Network Editor`

Confirm `VMnet2` is:

- a **Host-only** network
- on subnet `172.16.99.0/24`
- not using VMware DHCP for this lab

Now confirm your host computer has a VMware adapter on `VMnet2`.

The host adapter must have an address in `172.16.99.0/24`.

Typical example:

- host computer on `VMnet2`: `172.16.99.1`
- pfSense `MGMT`: `172.16.99.254`

If your host computer is not on that subnet, you will not be able to open the pfSense web interface in Step 2.

Quick host checks:

- Windows: `ipconfig`
- Linux: `ip -4 addr`

Look for the VMware `VMnet2` adapter and confirm it has an IPv4 address in `172.16.99.0/24`.

### Verify the VM Adapter Mapping

Before powering on the VMs, verify the adapter assignments in VMware Workstation:

1. Right-click a VM and open **Settings**.
2. Select **Network Adapter**.
3. Confirm it is connected to the correct LAN Segment or VMware network.

Expected mapping:

- `outside` VM and pfSense `WAN`: the `outside` LAN Segment
- `inside` VM and pfSense `LAN`: the `inside` LAN Segment
- `dmz` VM and pfSense `DMZ`: the `dmz` LAN Segment
- pfSense `MGMT`: `VMnet2`

You must verify this on every VM. Creating a segment name once does not automatically reattach the other VMs.

Why this matters:

- if a LAN Segment is missing, the VM cannot land on the correct network
- if `VMnet2` is wrong, the pfSense web interface will be unreachable from your host computer
- if a VM is attached to the wrong network, every later test becomes misleading

## pfSense Download

This lab uses a prebuilt pfSense firewall.

You do **not** need to install pfSense from scratch for this lab.

If you need the pfSense image for later practice, download it here:

- pfSense: <https://nscc-my.sharepoint.com/:u:/g/personal/w0305390_campus_nscc_ca/IQDunpCC1QGuT7FF77ut-_rPAZnwMuk3eGjNFix-bCpAtrs>

## Access Story

This is the traffic story you should learn:

- your host computer can manage pfSense through the `MGMT` network
- `outside` can reach the `DMZ` web page through the pfSense `WAN` address
- `outside` cannot reach a service that was **not** explicitly forwarded
- `inside` can reach the `outside` web page

Keep that story in mind as you work.

## Important Testing Note

Do **not** test the DMZ port forward from `inside`.

Test it from the `outside` VM.

By default, pfSense does not redirect internal clients back through a `WAN` port forward unless NAT reflection or split DNS is configured.

For this lab:

- `outside` reaches the DMZ page through the pfSense `WAN` address
- `inside` reaches the `dmz` host by its private `DMZ` address only if needed

This avoids a common NAT reflection problem.

---
[Home](README.md) | [Next](02_verify-hosts-and-open-pfsense.md)
