# Inspect WAN Rules and NAT

## Step 4. Inspect the `WAN` Rules

In pfSense, go to:

- `Firewall > Rules > WAN`

Look for:

- the rule that permits forwarded web traffic from `WAN` to the `dmz` host
- the explicit `WAN` block rule for port `8080` with logging enabled

Why this matters:

- a `WAN` rule controls traffic coming from `outside`
- the allow rule is tied to the port forward you will inspect in the next step
- the block rule is what makes the later firewall-log proof reliable

Important:

- the allow rule was created automatically when the NAT Port Forward was built
- pfSense uses the NAT entry to translate the traffic
- pfSense uses the linked `WAN` rule to permit that translated traffic

## **Screenshot 2: WAN Rules for the DMZ and Blocked 8080**
**Requirement:** Show the `WAN` rules page with both of these visible:

- the rule that allows forwarded web traffic to the `dmz` host
- the explicit logged block rule for `WAN` port `8080`

## Step 5. Inspect the NAT Port Forward

In pfSense, go to:

- `Firewall > NAT > Port Forward`

Find the rule that forwards web traffic from the pfSense `WAN` address to the `dmz` host.

Identify:

- the interface
- the destination address
- the destination port
- the redirect target IP
- the redirect target port

Validate:

- the forward sends `WAN` port `80` to `10.0.2.10:80`
- there is **not** a second web port forward exposing another internal service

Why this matters:

- the outside machine is not connecting directly to `10.0.2.10`
- pfSense is translating that connection and sending it to the `dmz` host

## **Screenshot 3: NAT Port Forward to the DMZ**
**Requirement:** Show the port forward that sends incoming web traffic on the `WAN` side to the `dmz` host.

---
[Prev](02_verify-hosts-and-open-pfsense.md) | [Home](README.md) | [Next](04_test-and-prove-traffic.md)
