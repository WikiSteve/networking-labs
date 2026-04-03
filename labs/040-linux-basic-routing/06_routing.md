# Routing

By default, the routing engine is disabled. We have to tell the system to route packets that it encounters on an interface.

To do this, a configuration bit needs to be enabled. Uncomment **`net.ipv4.ip_forward=1`** by removing the **`#`** in front of it in **`/etc/sysctl.conf`**.

![grep output in /etc/sysctl.conf showing the commented net.ipv4.ip_forward setting before it is enabled.](assets/images/file-62d83027a56d5.png)

After you've done this, reload the system control configuration:

```bash
sudo sysctl -p
```

![Terminal output confirming net.ipv4.ip_forward is enabled and sysctl settings are reloaded.](assets/images/file-62d830a7c0e5e.png)

![Packet capture view used to observe forwarding traffic and ICMP redirects during the routing test.](assets/images/file-62d8326c1e72f.png)

If you ping an external address like **`google.com`** from your client, it should work. However, the routing engine might send an ICMP redirect to tell the client to use the actual NAT gateway instead of the server. This setup demonstrates basic routing concepts, but a more realistic scenario will involve Network Address Translation (NAT) covered in a later lab.

To get the final screenshot, you need to "dodge" the ICMP redirect. If you sent a ping previously to one destination (e.g., **`google.com`**) and received a redirection, that route is now cached. You can prove your server is routing by targeting a completely different destination (e.g., **`yahoo.com`**) using **`traceroute`**. The screenshot must show that traffic passed through **your server** as the first hop.

![Traceroute output from the client demonstrating that web traffic passes through the server during the routing proof.](assets/images/file-62d8353d676da.png)

## **Screenshot 4: Routing Proof**
**Requirement:** Clearly indicate that your client's web traffic passed through the server.

---
[Prev](05_network-prep.md) | [Home](README.md)
