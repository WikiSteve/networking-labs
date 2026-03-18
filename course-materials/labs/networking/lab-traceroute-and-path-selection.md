# LAB Traceroute and Path Selection

- Filename: `LAB Traceroute and path selection.docx`
- Subject: `networking`
- Type: `lab`
- Reusable: `yes`
- Source file: [Source copy](../../sources/LAB%20Traceroute%20and%20path%20selection.docx)
- Submission template: [LAB Traceroute, DNS steering, and TTL proof with Wireshark Submission Template](../../templates/networking/lab-traceroute-dns-steering-and-ttl-proof-with-wireshark-submission-template.md)

## Summary

This reusable networking lab teaches traceroute from a packet-evidence perspective rather than by blind trust in tool output. Learners use Linux tools and Wireshark to prove how traceroute works through TTL expiration and ICMP Time Exceeded, compare DNS answers from different resolvers, distinguish UDP, ICMP, and TCP-based traceroute probes, and connect hop-level routing to real BGP and ASN relationships using Hurricane Electric's toolkit. The structure is strongly evidence-driven: learners capture packets, filter traffic by destination IP, expose TTL as a column, identify probe types by packet features, and explain path differences using routing policy rather than vague "internet magic."

## Key Details

- The lab goal is to prove with packets how traceroute works and why DNS answers for large sites vary between resolvers.
- It is designed for one 2-hour class and uses Linux, Wireshark, `dig`, `ping`, and `traceroute`.
- Setup includes installing `traceroute`, `dnsutils`, and `wireshark`.
- Part 1 compares DNS results for `google.com` using the default resolver, `1.1.1.1`, and `8.8.8.8`.
- The DNS section explains multiple A records, resolver-dependent answers, and why nearby users may see different first IPs.
- Part 2 runs traceroute three ways: UDP, ICMP, and TCP SYN to port 443.
- Wireshark filtering is used to prove which probe type was used by each traceroute run.
- Learners expose the TTL field as a visible column and use `icmp.type == 11` to prove Time Exceeded behavior.
- The lab explains what `* * *` hops can mean and why increasing TTL reveals one more hop at a time.
- A Linux versus Windows section compares `traceroute` and `tracert` defaults.
- The final routing section uses Hurricane Electric's BGP Toolkit to identify the ASN, organization, and peers or upstreams for a public hop.
- The grading checklist is built around four screenshot deliverables with caption prompts.

## Tags

- `traceroute`
- `wireshark`
- `dns-steering`
- `ttl`
- `icmp`
- `bgp`
- `asn`
- `networking-lab`
