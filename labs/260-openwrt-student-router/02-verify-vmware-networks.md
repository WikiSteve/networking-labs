# Verify the VMware networks

[← Before you start](./01-before-you-start.md) · [Lab overview](./README.md) · [Verify the Minion uplink →](./03-verify-minion-uplink.md)

Open **Edit → Virtual Network Editor** on the Router PC. Select each network and check the settings below.

| Network | Expected setting | Purpose |
|---|---|---|
| VMnet0 | Bridged to the Realtek adapter | Upstream physical connection |
| VMnet10 | Bridged to Intel I210-T1 | Isolated physical bench |
| VMnet8 | NAT with local DHCP and IPv6 enabled | Minion Bridge upstream |
| VMnet1 | Host-only with a host virtual adapter on `192.168.220.0/24` | Router PC access to LuCI |

Keep the upstream cable on Realtek and leave the Intel bench cable unplugged until [Step 3](./04-enable-lan-addressing.md). Read the full **Bridged to** field for VMnet10. If it says **Automatic**, **Realtek**, or a different device, stop and ask your instructor to correct the mapping before connecting the bench. In **Network Connections**, open **Status → Details** on the Windows VMnet1 adapter and check for `192.168.220.1` with mask `255.255.255.0`. The router itself uses `192.168.220.2`.

## **Screenshot 1: Prove the dedicated bridge**

**Requirement:** Show VMware’s Virtual Network Editor with **VMnet10** selected and **Intel I210-T1** visible in **Bridged to**.

![Virtual Network Editor showing VMnet10 bridged to Intel I210-T1](./evidence/01-bridge.png)

Open **VM → Settings** for both VMs and check each adapter. Create the **Minion-WAN** LAN segment once if it is missing.

| VM | Adapter | Setting |
|---|---|---|
| Minion Bridge | 1 | NAT |
| Minion Bridge | 2 | LAN Segment **Minion-WAN** |
| OpenWrt Student Router | 1 | Host-only VMnet1 |
| OpenWrt Student Router | 2 | Custom VMnet10. Leave it disconnected and clear **Connect at power on**. |
| OpenWrt Student Router | 3 | LAN Segment **Minion-WAN** |

Keep **Connect at power on** checked for the NAT, host-only and LAN segment adapters.

[← Before you start](./01-before-you-start.md) · [Lab overview](./README.md) · [Verify the Minion uplink →](./03-verify-minion-uplink.md)
