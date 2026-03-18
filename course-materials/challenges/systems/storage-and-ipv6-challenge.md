# Storage and IPv6 Challenge

- Filename: `Storage and IPv6 Challenge.docx`
- Subject: `systems`
- Type: `challenge`
- Reusable: `yes`
- Source file: [Source copy](../../sources/Storage%20and%20IPv6%20Challenge.docx)
- Submission template: [Storage and IPv6 Challenge Submission Template](../../templates/systems/storage-and-ipv6-challenge-submission-template.md)

## Summary

This reusable challenge combines enterprise storage configuration and network-verification tasks into one multi-part assessment. It requires five screenshots across four technical areas: a physical RAID design decision using the Intel RAID controller simulator, a destructive TrueNAS hot-spare and rebuild exercise, an iSCSI SAN target presented to Windows Server, a Wireshark investigation of Cloudflare WARP DNS-over-HTTPS traffic, and an IPv6 verification task using whois to prove the VPN-side address belongs to Cloudflare. The storage half emphasizes RAID tradeoffs, rebuild behavior, hot spares, SAN versus NAS concepts, iSCSI naming, and Windows mounting. The network half emphasizes packet capture, protocol identification, destination validation, public registration checks, and IPv6 visibility.

## Key Details

- The first section is a physical RAID scenario using the Intel RAID controller simulator, with requirements around redundancy, automatic rebuild behavior, avoiding write penalties, and balancing redundancy with performance.
- Screenshot 1 requires creating a single RAID volume named `FirstName-challenge` and justifying in one sentence why that RAID choice is the best fit for the database workload.
- The NAS component requires TrueNAS with hostname `Lastname-NAS`, using any RAID type plus a hot spare in the pool.
- The TrueNAS task deliberately tests failure handling by removing a drive, observing a degraded pool, then manually replacing and rebuilding.
- Screenshot 2 must show the hostname, the drive replacement, and the rebuild process in one image.
- The SAN portion requires creating an iSCSI target whose IQN includes `FirstName-challenge-target`, backed by a 42 GB volume labeled `best-challenge-ever`, and mounted on Windows Server.
- Screenshot 3 must visibly prove the 42 GB size, the backing-volume label, and the IQN naming together.
- The Wireshark section focuses on Cloudflare WARP and DoH, asking for capture of outbound HTTP-over-TLS or TLS/443 traffic to Cloudflare-owned destination IPs in the range `162.159.36.1` to `162.159.46.1`.
- Screenshot 4 must prove the application traffic type, destination IP, ownership by Cloudflare, the required IP range, and the visible computer name.
- The IPv6 section requires identifying any IPv6 connection using the VPN-side inside address, then using whois to show the source IPv6 address belongs to Cloudflare.
- Screenshot 5 must show source and destination IPv6 addresses, the personalized computer name, and the whois registration proving Cloudflare ownership.
- The challenge assumes prior knowledge of RAID, TrueNAS, iSCSI, Wireshark, DoH, Cloudflare WARP, and IPv6 investigation.

## Tags

- `challenge`
- `raid`
- `truenas`
- `iscsi`
- `san`
- `wireshark`
- `cloudflare-warp`
- `ipv6`
