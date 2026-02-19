# DNS

## DNS Server for IPv4

### **Setting Up the Cisco 2811 DNS Server for IPv4**

**Objective**

Configure the Cisco 2811 to act as an authoritative DNS server for the `LastName.com` domain, resolving hostnames to IPv4 addresses. Additionally, clarify that while the `ipv6 host` command exists, it introduces bugs and will be avoided in favor of `ip host` (A records) for IPv4 resolution only.

### **Steps to Configure DNS**

**Enable the DNS Server**

Enter global configuration mode and enable the DNS server:

`LastNameR1(config)# ip dns server `

**Verify the Domain Name**

Confirm the domain name is already set to `LastName.com`, as configured earlier in this guide. To verify:

`LastNameR1# show running-config | b ip domain `

![Image](assets/images/file-673fd586346b8.png)

If the domain name is missing or needs correction:

`LastNameR1(config)# ip domain-name LastName.com `

**Add Host Mappings (A Records)**

Use the `ip host` command to create A records for hostname-to-IPv4 address mapping. Be sure to use **lowercase** for hostnames and domain names to ensure consistent resolution:

`LastNameR1(config)# ip host sharper1.LastName.com 10.10.10.2

LastNameR1(config)# ip host sharpesw1.LastName.com 10.10.10.1 `

**Avoid Using `ipv6 host`**

The `ipv6 host` command can map hostnames to IPv6 addresses locally, but the DNS server on the Cisco 2811 only supports A records for IPv4 resolution.

**Key Clarification:**

Using `ipv6 host` introduces significant bugs and unexpected behavior, particularly with DNS responses.

To maintain stability, stick to `ip host` mappings and avoid configuring `ipv6 host`.

AAAA records for IPv6 are not supported by the DNS server for external resolution.

IPv6 hostname mappings via `ipv6 host` are for internal use only, within the router’s CLI.

**Save Your Configurations Externally**

As per lab practices, do not save configurations to the router’s memory. Instead, copy the DNS-related configuration commands (like `ip dns server`, `ip domain-name`, and `ip host` entries) into a text editor for future reference.

## Configure the DHCP Pool to Use the Loopback Address for Internal DNS

**Step 1: Configure the DHCP Pool to Use the Loopback Address for Internal DNS**

**Access DHCP Pool Configuration**

Enter global configuration mode and access the existing DHCP pool:

```plaintext
LastNameR1# configure terminal
LastNameR1(config)# ip dhcp pool VLAN1_POOL
```

**Set the DNS Server**

Add the Cisco 2811's loopback IP address (`10.10.10.2`) as the DNS server for the DHCP pool:

`LastNameR1(dhcp-config)# dns-server 10.10.10.2`

**Verify the DHCP Pool Configuration**

Confirm the DNS server is correctly added:

```plaintext
LastNameR1# show running-config | section ip dhcp pool
```

![Image](assets/images/file-6740acfac7bf9.png)

## Set External DNS Servers

**Set External DNS Servers**

While still in global configuration mode, add Cloudflare and Google DNS as external resolvers:

`LastNameR1(config)# ip name-server 1.1.1.1

LastNameR1(config)# ip name-server 8.8.8.8`

**Verify the External DNS Server Configuration**

Check if the external DNS servers are correctly added:

`LastNameR1# show running-config | include ip name-server `

You should see:

`ip name-server 1.1.1.1

ip name-server 8.8.8.8`

**Step 4: Test DNS Resolution**

1.

**Test Internal DNS on the Router**

  - Verify internal name resolution works:

```plaintext
LastNameR1# ping LastNameR1.LastName.com
 LastNameR1# ping LastNameSW1.LastName.com
```

1.

**Test External DNS on the Router**

  - Verify external name resolution: `LastNameR1# ping google.com `

1.

**Test DHCP Clients**

  - **Windows Clients:**

    - Use `ipconfig /all` to confirm `10.10.10.2` is assigned as the DNS server.

  - **Linux Clients:**

    - On systems with Network Manager, use: `nmcli dev show `

    - For barebones Debian systems, check `/etc/resolv.conf`: `cat /etc/resolv.conf `

 Ensure `nameserver 10.10.10.2` is listed.

1.

**Test Name Resolution from Clients**

  - Test internal and external resolution:

```plaintext
ping LastNameR1.LastName.com
ping google.com
```

**Important Notes**

1.

**DNS Server Behavior:**

  - The Cisco 2811’s DNS server supports only **A records** for local name resolution.

  - Use external DNS servers (`1.1.1.1` and `8.8.8.8`) for resolving public domains.

1.

**Why Use a Loopback Address for Internal DNS?**

  - The loopback interface (`10.10.10.2`) ensures reliability. As long as the router is operational, the loopback address remains reachable.

1.

**Limitations of IPv6 DNS on the 2811:**

  - While `ipv6 host` commands allow local resolution for IPv6 addresses, they introduce bugs in the DNS server. For this lab, stick to A records for internal devices.

## Configuring the Catalyst 1300 to Use the Cisco 2811 as its DNS Server

To streamline DNS resolution in the lab, the Catalyst 1300 switch will be configured to use the Cisco 2811's loopback address (`10.10.10.2`) as its sole DNS server. The Cisco 2811 will handle both internal and external lookups.

**Steps to Set the Nameserver on the Catalyst 1300**

**Access Global Configuration Mode**

Log into the Catalyst 1300 and enter global configuration mode:

`LastNameSW1# configure terminal `

**Set the DNS Server**

Configure the Cisco 2811 loopback address as the primary and only DNS server:

`LastNameSW1(config)# ip name-server 10.10.10.2 `

**Verify the Configuration**

Check that the nameserver is correctly configured:

`LastNameSW1# show running-config | include ip name-server `

You should see:

`ip name-server 10.10.10.2 `

**Testing the Configuration**

1.

**Ping an Internal Host by Name**

 Verify that the Catalyst 1300 can resolve internal hostnames through the Cisco 2811:

 `LastNameSW1# ping LastNameR1.LastName.com `

1.

**Resolve an External Domain**

 Ensure that external lookups are also functional:

```plaintext
LastNameSW1# ping google.com
```

**Explanation**

-

**Centralized DNS:**

 By pointing the C1300 to the Cisco 2811 (`10.10.10.2`), all DNS resolution (internal and external) is handled by the 2811, providing consistency across the lab network.

-

**Simplified Configuration:**

 Using a single DNS server simplifies the setup and ensures the C1300 doesn't need to manage fallback DNS logic or external configurations.

Now the Catalyst 1300 is fully integrated with the lab's DNS system, allowing it to resolve internal and external names through the Cisco 2811.
---

[Prev](09_wan-connection.md) | [Home](README.md) | [Next](11_changelog.md)
