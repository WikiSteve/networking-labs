# LAB Client Server with Netcat

- Filename: `LAB Client Server with netcat.docx`
- Subject: `networking`
- Type: `lab`
- Reusable: `yes`
- Source file: [Source copy](../../sources/LAB%20Client%20Server%20with%20netcat.docx)

## Summary

This reusable hands-on networking lab teaches basic client-server TCP communication using Netcat, PuTTY, and Wireshark in a virtualized environment. The lab has learners install Nmap to obtain `ncat`, switch VMware Workstation networking from NAT to Bridged mode so each VM gets its own LAN IP, and then work in pairs where one machine listens on TCP port 4444 and the other connects as a client. After establishing the chat session, the lab uses Wireshark to inspect the traffic, filter on `tcp.port == 4444`, follow the TCP stream, and observe both the three-way handshake and the plaintext application-layer conversation. It then adds PuTTY as an alternate TCP client, mainly to reinforce that insecure plaintext communication is easy to observe.

## Key Details

- The lab objective covers Netcat and PuTTY client-server setup, Wireshark inspection, bridged networking, and plaintext visibility.
- Readers install Nmap on Windows to obtain `ncat`, then verify the install with `ncat --version`.
- A core setup step is switching VMware Workstation networking from NAT to Bridged mode.
- Learners run `ipconfig` and share IPv4 addresses with a partner, making the activity pair-based.
- The server side listens with `ncat -lvp 4444`.
- The client side connects with `ncat <partner IP> 4444`.
- Wireshark instructions include filtering on `tcp.port == 4444` and using Follow TCP Stream.
- The lab explicitly calls out the TCP three-way handshake: SYN, SYN-ACK, ACK.
- A second connection method uses PuTTY in Telnet or Raw mode to connect to the same Netcat listener.
- The wrap-up asks learners to explain NAT versus Bridged mode, how Netcat simplifies client-server setup, what appears at the application layer, and why secure protocols should be preferred.
- The final deliverable is an in-person checkoff after successful connection, message exchange, and Wireshark capture.

## Tags

- `netcat`
- `wireshark`
- `putty`
- `tcp`
- `client-server`
- `vmware-workstation`
- `bridged-networking`
- `networking-lab`
