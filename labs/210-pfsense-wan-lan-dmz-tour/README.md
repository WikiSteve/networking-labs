# pfSense WAN, LAN, DMZ, and Management Lab

> **Before you start:** Download the [pfSense WAN, LAN, DMZ, and Management Lab Submission Template](<./assets/pfSense WAN, LAN, DMZ, and Management Lab SUBMISSION TEMPLATE.pptx>). Add each required screenshot directly into this file as you complete the lab, then submit the completed template for grading.

## Goal

Build a four-interface pfSense firewall in VMware Workstation and prove:

- how `WAN`, `LAN`, `DMZ`, and `MGMT` should be used
- why `outside` can reach the public `DMZ` service on port `80`
- why `outside` cannot reach the internal-only `DMZ` service on port `8080`
- why `inside` can reach the `DMZ` internal service and the `outside` web page
- why the pfSense GUI should be reachable from `MGMT`, not from `inside` or `outside`

## Prereqs

- basic VMware Workstation use
- basic Debian command-line use
- basic IPv4 addressing and default gateways
- basic DHCP, NAT, and port-forwarding concepts
- ability to clone a VM and change a hostname
- the course pfSense installer ISO: [netgate-installer-v1.1.1-RELEASE-amd64.iso](https://nscc-my.sharepoint.com/:u:/r/personal/w0305390_campus_nscc_ca/Documents/ISOs/netgate-installer-v1.1.1-RELEASE-amd64.iso?csf=1&web=1&e=bAXpWe)

## Deliverables

- Screenshot 1 through Screenshot 6 as listed in the lab pages
- correct MAC-address mapping and interface naming
- correct interface IPs, DHCP scopes, and `DMZ` reservation
- correct traffic results for the public service, blocked service, and internal-only service

## Pages

- [01 Overview and VMware Prep](01_overview-and-vmware-prep.md)
- [02 Install pfSense and Reach the GUI](02_verify-hosts-and-open-pfsense.md)
- [03 Configure pfSense in the GUI](03_inspect-wan-rules-and-nat.md)
- [04 Test and Prove Traffic](04_test-and-prove-traffic.md)
- [05 Submission Guide](05_submission-guide.md)

## Accessibility

- [Screenshot alt text and OCR transcript data](assets/screenshot-ocr.json)
