# nftables

This note groups the current nftables rewrite set and its legacy source material in one place. It serves as a consolidated transition note: the new draft files are the future direction, while the older files remain useful as source material and historical context.

## New Draft Replacements

### LAB Host Firewall with nftables

- Status: `new draft`
- Type: `lab handout`
- Role in stack: replacement for the host-policy parts of the old iptables material
- Source file: [Source copy](../../sources/LAB%20Host%20Firewall%20with%20nftables.docx)
- Supersedes: `iptables lab 2.docx` and the DMZ host `OUTPUT` example from `iptables lab 1.docx`
- Readiness: `near-ready draft`

Notes:

- Debian-focused host firewall lab.
- Rules run on `Inside1` itself, not on the router.
- Teaches `nftables` through `output`-chain policy, destination blocking, ICMP blocking, and a final default-drop output ruleset.
- The scope is cleaner than the legacy material because endpoint filtering is isolated from transit policy.

### LAB Transit Firewall and Router Policy with nftables

- Status: `new draft`
- Type: `lab handout`
- Role in stack: replacement for the router and transit parts of the old iptables material
- Source file: [Source copy](../../sources/LAB%20Transit%20Firewall%20and%20Router%20Policy%20with%20nftables.docx)
- Supersedes: `iptables lab 1.docx` FORWARD-chain teaching and some challenge logic from the older labs
- Readiness: `good draft`

Notes:

- Debian-focused transit firewall and router lab.
- Rules run on the firewall container, not the endpoints.
- Teaches `forward` policy, default drop, `ct state established,related`, inside-to-outside allow rules, and selective access from Inside1 to the DMZ.
- It cleanly separates forwarded traffic from locally generated traffic.

### NAT_and_PAT_reimagined_nftables

- Status: `new draft`
- Type: `lecture deck`
- Role in stack: modern replacement for the old NAT/PAT deck
- Source file: [Source copy](../../sources/NAT_and_PAT_reimagined_nftables.pptx)
- Supersedes: `NAT met PAT.pptx`
- Readiness: `draft, needs final polish`

Notes:

- Shorter NAT/PAT lecture deck aligned to `nftables`, containerlab, and modern Linux labs.
- Keeps the packet-path and netfilter story while moving away from legacy command syntax as the main teaching language.
- Covers NAT/PAT relevance, source NAT versus masquerade, DNAT and publishing, stateful filtering, legacy `iptables` comparison, and a containerlab-friendly lab sequence.
- Still appears to carry some older addressing in examples, so it is not fully normalized yet.

## Legacy Source Files

### NAT met PAT

- Status: `old source`
- Type: `lecture deck`
- Keep reason: strong conceptual source deck for NAT/PAT
- Source file: [Source copy](../../sources/NAT%20met%20PAT.pptx)

Notes:

- Original NAT/PAT lecture deck with good conceptual coverage.
- Explicitly iptables-centered and tied to older syntax and platform assumptions.
- Best kept as source material rather than the future-facing version.

### Lab Assignment: Exploring the basics of NAT

- Status: `old source`
- Type: `lab handout`
- Keep reason: rewrite target for the future NAT and port-publishing nftables lab
- Source file: [Source copy](../../sources/Lab%20Assignment_%20Exploring%20the%20basics%20of%20NAT.docx)

Notes:

- Full NAT lab built around a firewall plus inside, outside, DMZ, and cloud hosts.
- Mixes firewalling, forwarding, source NAT, and DNAT publishing in one older lab shell.
- Strong raw material, but not future-facing as-is.

### iptables lab 1

- Status: `old source`
- Type: `lab handout`
- Keep reason: concept source for `INPUT`, `FORWARD`, and `OUTPUT`
- Source file: [Source copy](../../sources/iptables%20lab%201.docx)

Notes:

- Basic chain lab covering `INPUT`, `FORWARD`, and `OUTPUT`.
- Useful concept ancestor, but structurally mixed because it blends router policy and host policy.
- Superseded by the separate host and transit nftables drafts.

### iptables lab 2

- Status: `old source`
- Type: `lab handout`
- Keep reason: cleanest old source for the host firewall rewrite
- Source file: [Source copy](../../sources/iptables%20lab%202.docx)

Notes:

- Port-filtering lab focused on `Inside1`.
- Really an endpoint firewall lab, but the older stack did not frame it that clearly.
- Mostly replaced by `LAB Host Firewall with nftables.docx`.

## Summary

- Old files: keep as source material and history.
- New files: keep as drafts that define the new direction.
- Gap still remaining: a dedicated NAT and port-publishing lab with `nftables` has not fully replaced the legacy NAT lab yet.
