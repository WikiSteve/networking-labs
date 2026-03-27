# Troubleshooting

Use this page when pfSense goes sideways during the lab.

The most common painful failure in this lab is:

- ARP works on the management subnet
- but `ping` and the web GUI do not

That does **not** automatically mean pfSense is dead.

It usually means one of these is true:

- the wrong pfSense interface has the `MGMT` IP
- the intended `MGMT` interface lost its IP
- the wrong optional interface was renamed
- the NIC-to-interface mapping no longer matches the student's table
- the GUI moved, but the expected firewall or listen path was not finished correctly

## Fast Rule

Before you keep clicking around in pfSense, stop and prove:

1. which NIC is really `MGMT`
2. which interface really has the `.200` host-only IP
3. whether that interface is enabled
4. whether the host computer is on the same host-only subnet
5. whether the GUI is actually listening where you think it is

## 5-Step “pfSense Went AWOL” Checklist

### 1. Go Back to the MAC Table

Open your Screenshot 1 mapping table.

Confirm which VMware adapter was supposed to be:

- `WAN`
- `LAN`
- `DMZ`
- `MGMT`

If you added, removed, or reordered NICs after that table was made, assume your interface mapping may now be wrong.

### 2. Check the pfSense Console First

From the pfSense console, verify:

- which interface currently has the host-only subnet IP ending in `.200`
- whether that interface is enabled and up
- whether the interface names still match your intended roles

If the host-only `.200` address is missing, blank, or sitting on the wrong interface, fix that first.

### 3. Check VMware Before You Blame pfSense

In VMware, confirm:

- the pfSense `MGMT` NIC is still attached to VMware `vmnet1` (`host-only`)
- your host computer still has an IP on that same `vmnet1` host-only subnet
- you did **not** accidentally move the `MGMT` NIC onto `NAT`, `inside`, or `dmz`

If VMware and pfSense disagree about which NIC is `MGMT`, your GUI path will be unreliable or dead.

### 4. If ARP Works but `ping` and `HTTPS` Fail, Interpret That Correctly

ARP only proves layer 2 reachability on the local segment.

It does **not** prove:

- that the right interface has the expected IP
- that pfSense is replying to ICMP on the interface you think it is
- that the GUI is listening on that interface
- that your interface mapping is still correct

So if ARP works but `ping` and the GUI fail, focus on:

- wrong interface assignment
- missing or wrong `MGMT` IP
- disabled `MGMT`
- later GUI-hardening/listen-interface mistakes

Do **not** waste time debugging WAN rules, NAT, or the `DMZ` web service first.

## High-Probability Mistakes in This Lab

### Mistake 1: Renaming the Wrong Optional Interface

Students often intend:

- `OPT1 -> DMZ`
- `OPT2 -> MGMT`

but the real problem is that they no longer know which optional interface belongs to which NIC.

If the MAC mapping is wrong, the rename can make the GUI path even more confusing.

### Mistake 2: Damaging `MGMT` While Renaming

While trying to rename `OPT2 -> MGMT`, students sometimes also:

- change the wrong interface page
- blank the IP
- disable the interface
- assume the rename step is also the place to reassign NICs

Rename first. Verify second. Change only what the lab asks for.

### Mistake 3: Treating Virtual Network Editor as the Place to Define Everything

Remember:

- VMware Virtual Network Editor manages `vmnet8` and `vmnet1`
- VMware LAN Segments provide `inside` and `dmz`
- pfSense defines the actual internal addressing and services

If you blur those layers together, you can easily chase the wrong problem.

## When to Snapshot and Stop

Take a VMware snapshot and stop changing things blindly if:

- the GUI worked once and then disappeared after interface edits
- ARP works but the host-only `.200` path no longer behaves predictably
- you are no longer sure which pfSense interface is really `MGMT`
- you have changed multiple interface pages and can no longer explain what is different

At that point, evidence is more valuable than more clicking.

## Traffic Test Failures (Steps 15-17)

If the pfSense GUI works but the proof commands in page 04 fail, use this shorter checklist before you start rewriting rules blindly.

### `outside -> WAN:80` does not show the public `DMZ` page

Check:

- the `WAN` port forward really points to `10.20.20.100:80`
- the matching `WAN` firewall rule exists
- the `dmz` VM still serves the page locally on port `80`

If the local `dmz` page is broken, fix the service before you debug pfSense.

### `inside -> 10.20.20.100:8080` fails

Check:

- the `dmz` VM still serves the internal-only page locally on port `8080`
- `inside` really has a `10.10.10.x` address from pfSense

Do **not** start by adding a new `LAN` rule. In this lab, the default `LAN` rule should already allow `inside -> DMZ`.

### `inside -> outside` fails

Check:

- `outside` still serves its page locally
- pfSense outbound NAT is still in automatic mode
- `inside` still has a working `LAN` lease and gateway from pfSense

This path is `LAN -> WAN`, so if it breaks, think outbound routing/NAT before you think `DMZ`.

---
[Prev](05_submission-guide.md) | [Home](README.md)
