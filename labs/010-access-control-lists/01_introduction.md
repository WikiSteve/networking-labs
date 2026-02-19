# Introduction

## Lab Prerequisites

**Before you begin, make sure to download the submission template.**

Before starting this lab, students must complete the following:

1.

**Catalyst 1300 Tour Guide**:

  - A hands-on walkthrough of the Catalyst 1300 switch, covering essential configuration and management tasks.

1.

**VLANs and Trunking**:

  - Students should have a strong understanding of VLAN creation, assignment, and trunking concepts.

  - Knowledge of native VLANs and VLAN tagging is essential.

1.

**ACL Fundamentals**:

  - Completion of Packet Tracer activities for numbered and named ACLs.

  - Familiarity with ACL syntax, structure, and use cases for IPv4. We will introduce IPv6

## Lab Goals

This lab provides practical experience with Access Control Lists (ACLs) and their applications in network security and traffic management. The specific objectives are:

1.

**Secure Management Access Using Extended ACLs**

  - **Restrict Management Protocols on Interface Ports:**

    - Block access to device management protocols (SSH, HTTP, HTTPS) on all physical interface ports.

  - **Permit Management Access via Loopback Interface:**

    - Configure the network to allow management access exclusively through the loopback interface.

  - **Understand ACLs for Control and Security:**

    - Learn how extended ACLs can enhance security by controlling management traffic.

1.

**Configure Standard ACLs for NAT Traffic Matching**

  - **Define "Interesting" Traffic for NAT:**

    - Use standard ACLs to specify which traffic should be considered for Network Address Translation (NAT).

  - **Apply ACLs in NAT Configuration:**

    - Integrate the ACLs with NAT settings to ensure only matched traffic is translated.

  - **Gain Insights into ACL and NAT Integration:**

    - Understand the role of ACLs in controlling NAT processes and optimizing network performance.

1.

**Implement ACLs for VLAN-Based Traffic Control**

  - **Allow Full Internet Access on VLAN 42:**

    - Ensure devices on VLAN 42 have unrestricted access to the internet.

  - **Restrict Access to Specific Resources on VLAN 1:**

    - Configure ACLs to prevent devices on VLAN 1 from accessing Facebook resources.

  - **Enforce Network Policies with ACLs:**

    - Learn how to use ACLs to implement network policies and control inter-VLAN traffic effectively.
---

[Home](README.md) | [Next](02_secure-management.md)
