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

## Final Check

Before you upload the file, make sure you can explain:

- why `WAN` had to use VMware `NAT`
- why `MGMT` belongs on VMware `host-only`
- why the public `DMZ` page worked from `outside`
- why the internal-only `DMZ` page did not work from `outside`
- why the pfSense GUI should be reachable only from `MGMT`

---
[Prev](04_test-and-prove-traffic.md) | [Home](README.md)
