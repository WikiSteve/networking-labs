# pfSense WAN, LAN, DMZ, and Management Tour

> **Before you start:** Download the [pfSense WAN, LAN, DMZ, and Management Tour Lab Submission Template](<./assets/pfSense WAN, LAN, DMZ, and Management Tour Lab SUBMISSION TEMPLATE.pptx>). Add each required screenshot directly into this file as you complete the lab, then submit the completed template for grading.

## Goal

Explore a prebuilt pfSense firewall and prove:

- why `outside` can reach the `DMZ` web server
- why `outside` cannot reach a service that was not forwarded
- why `inside` can reach `outside`
- where NAT and firewall filtering show up in pfSense

## Prereqs

- basic IPv4 addressing and default gateways
- basic web and port concepts
- basic VMware Workstation use
- basic idea of what a firewall does

## Deliverables

- Screenshot 1 through Screenshot 10 as listed in the lab pages
- correct interface names, IP addresses, and traffic results in the required screenshots
- correct pfSense rule, NAT, log, and state evidence in the required screenshots

## Pages

- [01 Overview and VMware Prep](01_overview-and-vmware-prep.md)
- [02 Verify Hosts and Open pfSense](02_verify-hosts-and-open-pfsense.md)
- [03 Inspect WAN Rules and NAT](03_inspect-wan-rules-and-nat.md)
- [04 Test and Prove Traffic](04_test-and-prove-traffic.md)
- [05 Submission Guide](05_submission-guide.md)
