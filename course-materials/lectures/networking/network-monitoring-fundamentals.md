# Network Monitoring Fundamentals

- Filename: `Network Monitoring Fundamentals.pptx`
- Subject: `networking`
- Type: `lecture`
- Reusable: `yes`
- Source file: [Source copy](../../sources/Network%20Monitoring%20Fundamentals.pptx)

## Summary

This reusable lecture deck introduces the fundamentals of network monitoring and network management from an operations perspective. It defines core concepts such as network management, faults, availability, NMS, and baselining, then explains why organizations adopt monitoring in the first place, usually to detect outages faster, improve availability and performance, replace weak or expensive tooling, or recover from failures that existing systems missed. The deck treats baselining as the first essential step in any monitoring project, then organizes network management into the FCAPS model with special focus on fault management and performance management. It also explains practical monitoring methods such as ICMP ping, SNMP polling, topology maps, email or SMS alerts, MIB queries, user experience monitoring, and NetFlow-based traffic analysis.

## Key Details

- Defines core terms including network management, fault, availability, NMS, and baseline.
- Frames the motivation for monitoring around real operational pain points such as missed outages, high tool cost, weak performance, and availability issues.
- Explicitly notes what an NMS will not solve, including configuration knowledge gaps and unrelated operational problems.
- Treats baselining as Fundamental #1 and stresses the need for a starting point before making changes.
- Lists important baseline targets such as availability, application performance, network congestion, and user-reported issues.
- Introduces the FCAPS model: Fault, Configuration, Accounting, Performance, and Security.
- Describes fault-monitoring goals as reducing phone-call discovery and reacting faster to outages.
- Explains fault methods using ICMP echo requests, SNMP checks, email or SMS alerts, and topology maps.
- Names example fault-management tools including HP OpenView, Zenoss, and ipMonitor.
- Covers performance monitoring targets such as CPU, memory, disk, interface utilization, errors, and congestion.
- Explains performance methods using SNMP/MIB polling, user experience monitors, and NetFlow.
- Ends with five best practices focused on business goals, baselining, total cost of ownership, outside help when needed, and doing something rather than nothing.

## Tags

- `network-monitoring`
- `nms`
- `fcaps`
- `snmp`
- `netflow`
- `baselining`
- `fault-management`
- `performance-management`
