# Crypto Basics in Wireshark

- Filename: `Crypto basics in Wireshark.docx`
- Subject: `security`
- Type: `lab`
- Reusable: `yes`
- Source file: [Source copy](../../sources/Crypto%20basics%20in%20Wireshark.docx)

## Summary

This reusable networking and cryptography lab uses Wireshark to compare what is visible in unencrypted HTTP traffic versus encrypted HTTPS and to introduce handshake analysis across SSH, TLS, and WireGuard. The first section has learners capture HTTP traffic, identify the application protocol, extract the domain from the `Host` header, inspect full URL paths and plaintext payloads, and export transmitted image objects from Wireshark. The second section shifts to HTTPS and explains what changes under TLS, including filtering on `tls` or `ssl`, locating the domain through SNI in the Client Hello, and recognizing that URL paths and application data are no longer visible in plaintext. The document also includes a plain-language explanation of Diffie-Hellman inside the TLS 1.2 handshake and ends with comparative capture exercises for SSH, HTTPS, and WireGuard using Cloudflare WARP.

## Key Details

- The first section focuses on HTTP capture and analysis using the `http` display filter.
- Learners identify the domain from the `Host` header and the full URL path from the GET request line.
- The lab includes a visibility exercise on plaintext HTML or form data in HTTP captures.
- A separate HTTP exercise teaches exporting image objects through `File > Export Objects > HTTP`.
- Before the HTTPS section, the file explains TLS 1.2 Diffie-Hellman in plain language.
- The HTTPS section has learners filter on `tls` or `ssl`, verify TLS rather than HTTP, and find the domain via SNI in the Client Hello.
- It explicitly compares HTTP and HTTPS by showing that URL paths and payload data are encrypted under HTTPS.
- The last section compares handshake behavior across SSH, HTTPS or TLS, and WireGuard.
- The SSH exercise asks learners to document key exchange, algorithm negotiation, and session setup.
- The WireGuard section uses Cloudflare WARP and looks for UDP traffic, likely on port 51820.
- The lab is reusable as a protocol-analysis worksheet for encryption visibility and handshake comparison.

## Tags

- `wireshark`
- `http`
- `https`
- `tls`
- `diffie-hellman`
- `ssh`
- `wireguard`
- `protocol-analysis`
