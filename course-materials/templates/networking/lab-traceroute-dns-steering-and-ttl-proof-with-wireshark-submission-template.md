# LAB Traceroute, DNS Steering, and TTL Proof with Wireshark Submission Template

- Filename: `LAB Traceroute, DNS steering, and TTL proof with Wireshark Submission Template.pptx`
- Subject: `networking`
- Type: `submission-template`
- Reusable: `yes`
- Source file: [Source copy](../../sources/LAB%20Traceroute%2C%20DNS%20steering%2C%20and%20TTL%20proof%20with%20Wireshark%20Submission%20Template.pptx)
- Instructions: [LAB Traceroute and Path Selection](../../labs/networking/lab-traceroute-and-path-selection.md)

## Summary

This reusable submission template defines the four exact screenshots required for a packet-analysis lab on DNS steering, traceroute, TTL behavior, and routing context. It does not teach the commands or concepts directly. Instead, it requires `dig` output comparing resolvers, packet evidence showing traceroute probe type, TTL plus ICMP Time Exceeded proof in Wireshark, and Hurricane Electric ASN or neighbor context for a public hop. Its purpose is to standardize what proof of completion must look like for the lab.

## Key Details

- The file is explicitly a submission template rather than an instructional walkthrough.
- It requires four screenshots in total.
- Screenshot 1 is `dig` output tied to the DNS resolver comparison task.
- Screenshot 2 is probe evidence showing whether traceroute used UDP, ICMP, or TCP SYN probes.
- Screenshot 3 is TTL proof paired with Wireshark evidence showing TTL stepping and ICMP Time Exceeded behavior.
- Screenshot 4 is Hurricane Electric routing context showing ASN information and neighbors.
- The template is reusable because it is generic, structured, and not tied to learner-specific feedback.
- It pairs directly with the lab guide and gives a clean grading target without repeating the full instructions.

## Tags

- `submission-template`
- `traceroute`
- `wireshark`
- `dns`
- `ttl`
- `bgp`
- `asn`
- `packet-analysis`
