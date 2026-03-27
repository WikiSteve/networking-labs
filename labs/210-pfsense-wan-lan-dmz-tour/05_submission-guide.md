# Submission Guide

## What to Submit

Submit the completed PowerPoint template with:

- Screenshot 1: MAC Address Mapping Table
- Screenshot 2: pfSense Interface Names and IP Addresses
- Screenshot 3: GUI Access Before and After Hardening
- Screenshot 4: Outside Reaches WAN Port 80 but Not WAN Port 8080
- Screenshot 5: Inside Reaches the DMZ Internal Service on Port 8080
- Screenshot 6: Inside Reaches Outside

## Before You Submit

Make sure:

- each screenshot is on the correct slide
- each screenshot is readable at normal zoom
- the required IP addresses, hostnames, and command results are visible
- successful and failed tests are easy to tell apart
- Screenshots 4-6 show the actual `curl` commands and their results, not just a browser window or a cropped success message

## Final Check: Design Decisions

Before you upload the file, make sure you can explain:

- why `WAN` had to use VMware `NAT`
- why `MGMT` belongs on VMware `host-only`
- why the public `DMZ` page worked from `outside`
- why the internal-only `DMZ` page did not work from `outside`
- why the pfSense GUI should be reachable only from `MGMT`

Quick screenshot check:

- Screenshot 3 shows the before-and-after `outside -> https://<WAN_IP>` hardening proof in the same terminal window
- Screenshot 4 shows the success on `WAN:80` and the failure on `WAN:8080`
- Screenshot 5 shows the internal-only text from `10.20.20.100:8080`
- Screenshot 6 shows the `inside -> outside` `curl` and the returned `I am outside` text

---
[Prev](04_test-and-prove-traffic.md) | [Home](README.md) | [Next](06_troubleshooting.md)
