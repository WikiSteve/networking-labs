# Give clients their LAN settings

[← Verify the Minion uplink](./03-verify-minion-uplink.md) · [Lab overview](./README.md) · [Verify the wired Partner PC →](./05-verify-wired-partner.md)

1. With Student Router Adapter 2 still disconnected, open **Network → Interfaces → lan → Edit → DHCP Server**. Under **General Setup**, confirm **Ignore interface** is checked and **Force** is clear. Under **IPv6 Settings**, confirm **RA-Service** is disabled. Apply any change before continuing.
2. Your bench switch should have only the two bench cables. Connect the Router PC’s Intel jack to one access port and the Partner PC to another access port on the same VLAN. On your Router PC, open **VM → Settings → Network Adapter 2**, verify **Custom: VMnet10**, then select **Connected**. Leave **Connect at power on** clear.
3. On the Partner PC, open **Network Connections** and identify the Ethernet adapter on the bench cable. Under its **Properties → Internet Protocol Version 4 (TCP/IPv4) → Properties**, select **Obtain an IP address automatically** and **Obtain DNS server address automatically**. Keep IPv6 enabled. Run:

   ```text
   ipconfig /all
   ```

   Find the dedicated Ethernet adapter. Before you start the lab DHCP service, expect no lease or an address starting with `169.254.`. An IPv6 link-local address starting with `fe80:` is normal. If you see an assigned address or a default gateway on this link, ask your instructor to help trace the cables before continuing.
4. On the Router PC, recheck **Adapter 2 → Custom: VMnet10** and **VMnet10 → Intel I210-T1**. In LuCI, return to **lan → Edit → DHCP Server → General Setup**. Clear **Ignore interface**. Keep **Dynamic DHCP** checked and the lease time at **2h**.
5. Under **IPv4 Settings**, set **DHCPv4 Service** to **enabled**, **Start** to **100**, and **Limit** to **50**. Under **IPv6 Settings**, set **RA-Service** to **server mode**. Leave **DHCPv6-Service** and **NDP-Proxy** disabled. Click **Save**, then **Save & Apply**. DHCP gives clients their IPv4 configuration. Router Advertisements let clients learn their IPv6 prefix and route.

## **Screenshot 3: Show the LAN DHCP settings**

**Requirement:** After saving and applying the configuration, reopen **lan → Edit → DHCP Server → IPv4 Settings**. Show **DHCPv4 Service** set to **enabled**, **Start** set to **100**, and **Limit** set to **50**.

![Saved DHCPv4 settings showing enabled, Start 100 and Limit 50](./evidence/03-dhcp.png)

[← Verify the Minion uplink](./03-verify-minion-uplink.md) · [Lab overview](./README.md) · [Verify the wired Partner PC →](./05-verify-wired-partner.md)
