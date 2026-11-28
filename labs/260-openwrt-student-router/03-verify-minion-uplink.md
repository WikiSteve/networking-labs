# Verify the Minion uplink

[← Verify the VMware networks](./02-verify-vmware-networks.md) · [Lab overview](./README.md) · [Give clients their LAN settings →](./04-enable-lan-addressing.md)

1. Start **Minion Bridge** and wait for its console prompt. After your instructor has configured the relay, test it from that VM.

   ```sh
   http_proxy='http://[fd00:1ab:5::102]' wget -O /dev/null http://minion.lab/
   ```

   The `http_proxy` setting directs this one download through the Bridge’s relay. The brackets enclose its IPv6 address. The capital `-O` sends output to `/dev/null` so you can repeat the check without saving a file. Expect the download to complete. If it fails, recheck the Bridge’s NAT adapter and VMnet8 DHCP.

2. Leave the Bridge running and start **OpenWrt Student Router**. Open `http://192.168.220.2/` on the Router PC. The prebuilt image uses `root` with an empty password for the first LuCI login. Set your router password using LuCI’s password prompt. In **System → System**, save a hostname such as `openwrt-steve` using your own first name.
3. Open **Network → Interfaces**. Find **wwan** on device **eth2** and look for **wwan6** with an IPv6 address in `fd88:77:1::/64`.
4. In the Student Router console, run the checks below. Stop ping with **Ctrl+C** after you see replies. The second command saves the page to a named temporary file so you can repeat it.

   ```sh
   ping minion.lab
   wget -O /tmp/minion.html http://minion.lab/
   ```

   Wait for both checks to pass before turning on LAN services. If there is only a link-local address starting with `fe80:`, recheck the shared **Minion-WAN** segment and that the Bridge is running.

## **Screenshot 2: Prove the Minion uplink**

**Requirement:** Show LuCI **Network → Interfaces** with **wwan** on **eth2** and **wwan6** with an address in `fd88:77:1::/64`.

![OpenWrt interfaces showing the wired upstream connection and IPv6 prefix](./evidence/02-wan.png)

[← Verify the VMware networks](./02-verify-vmware-networks.md) · [Lab overview](./README.md) · [Give clients their LAN settings →](./04-enable-lan-addressing.md)
