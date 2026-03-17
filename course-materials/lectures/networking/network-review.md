# Network Review

- Filename: `Network Review.pptx`
- Subject: `networking`
- Type: `lecture`
- Reusable: `yes`
- Source file: [Source copy](../../sources/Network%20Review.pptx)

## Summary

This reusable review lecture deck revisits foundational networking concepts needed before firewalling and packet-filtering work, especially TCP behavior, connection-oriented versus connectionless protocols, stateful versus stateless networking, and port usage. It explains the TCP three-way handshake with SYN, SYN-ACK, and ACK, then uses that as the bridge to discuss why TCP is stateful and why UDP is not. The deck compares connection-oriented and connectionless protocols, gives practical use cases such as web traffic, DNS, streaming, VoIP, gaming, and file transfer, and then explicitly ties the idea of state to firewalls and `iptables`, making it a conceptual on-ramp to later filtering and NAT content.

## Key Details

- Covers the TCP three-way handshake step by step with SYN, SYN-ACK, and ACK.
- Compares connection-oriented and connectionless protocols using examples such as TCP, FTP, HTTP, UDP, and ICMP.
- Emphasizes the tradeoff between reliability and ordered delivery versus speed and lower overhead.
- Uses practical examples like HTTP or HTTPS, DNS, video calls, and file transfers.
- Introduces stateful versus stateless networking as preparation for firewall and `iptables` concepts.
- Explains stateful firewalls as devices that remember active connections and recognize valid return traffic.
- Explains stateless firewalls as packet filters that treat each packet independently.
- Reviews ports and protocols as communication endpoints plus rules governing communication.
- Notes that TCP and UDP can share the same port number on the same machine.
- Uses DNS on port 53 as a practical example of a service commonly using both TCP and UDP.
- Reviews well-known ports versus ephemeral ports and the use of temporary client source ports.
- Connects source and destination ports back to stateful firewalling and return-traffic matching.

## Tags

- `network-review`
- `tcp`
- `udp`
- `three-way-handshake`
- `stateful-firewall`
- `stateless-firewall`
- `ports`
- `ephemeral-ports`
