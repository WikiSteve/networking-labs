# Verify the wired Partner PC

[← Give clients their LAN settings](./04-enable-lan-addressing.md) · [Lab overview](./README.md) · [Connect both phones →](./06-connect-both-phones.md)

1. On a physical Partner PC, leave only its Intel cable to the isolated switch connected. Temporarily turn off Wi-Fi and unplug its other Ethernet cables. For the one-workstation option, confirm that the Windows partner VM has just one connected adapter, set to **Custom: VMnet10**. This tests the virtual lab connection. VMware may forward traffic on the same host, so a successful check there does not establish that traffic crossed the physical switch. Leave the Router PC’s upstream connection in place.
2. In Command Prompt, run `ipconfig /all` and find the same dedicated adapter. Expect an IPv4 address from `192.168.77.100` to `192.168.77.149`. The IPv4 default gateway and DHCP server should be `192.168.77.1`. Look for a separate IPv6 address, usually starting with `fd`, in addition to the link-local address. The IPv6 default gateway itself can start with `fe80:` because the router is on the same link.
3. Open a private browser window and go to `http://minion.lab/`. If the Minion page appears, the wired web check passed. Keep the address bar visible for Screenshot 4. In this lab, OpenWrt gives Minion an IPv6 address.

If the browser cannot resolve the name, run `nslookup minion.lab 192.168.77.1` in Command Prompt to ask OpenWrt directly. A correct answer shows that DNS works. Look for the lab portal address `fd00:1ab:5::102`. Loading the page is the separate web check. If you have an IPv4 lease but the page fails, check the same adapter for a non-link-local IPv6 address and IPv6 default gateway, then check the private Minion-WAN segment and the Student Router’s **wwan6** interface. If the portal opens but the adapter values are wrong, isolate the intended connection, reload the page, and check again.

If Windows shows **Destination port unreachable** when you ping Minion, continue with the browser check. See [why the Minion page can load when ping fails](./09-troubleshooting.md#minion-opens-but-ping-reports-destination-port-unreachable).

To verify automatic IPv4 and DNS on a physical Partner PC, open the Intel adapter’s **Properties**, select **Internet Protocol Version 4 (TCP/IPv4)**, and click **Properties**. Both settings should say **automatically**.

![Windows IPv4 Properties with automatic IP and DNS selected.](./evidence/wired-ipv4-auto.png)

Windows IPv4 Properties with automatic IP and DNS selected.

If the adapter shows a `169.254.x.x` address, [follow the DHCP checks](./09-troubleshooting.md#the-partner-pc-still-has-a-169254-address) before continuing.

## **Screenshot 4: Prove the partner’s wired connection**

**Requirement:** Show the Partner PC’s wired adapter name, IPv4 lease, IPv6 address, default gateways and DHCP server beside the Minion portal at `http://minion.lab/`. In the slide notes, record whether Minion opened with only the wired bench connection active.

![Partner PC’s Intel Ethernet configuration beside the Minion portal](./evidence/04-wired.png)

The rehearsal used a temporary host route to keep remote management connected while verifying the bench path. That route was removed. For your capture, isolate the Partner PC as described above. Restore the Partner PC connections you temporarily turned off after taking Screenshot 4.

## Optional Windows check · See the HTTP status

Windows 11 includes `curl.exe`. Run it in Command Prompt to view the web response over IPv6.

```text
curl.exe -6 -I http://minion.lab/
```

The `-6` option uses IPv6. The capital `-I` shows the response headers. Look for **200 OK**.

![lab Partner PC resolves minion.lab and receives HTTP 200 OK from an IPv6-only curl request.](./evidence/wired-optional-http.png)

Optional command-line example. The IPv6 web request returned 200 OK.

[← Give clients their LAN settings](./04-enable-lan-addressing.md) · [Lab overview](./README.md) · [Connect both phones →](./06-connect-both-phones.md)
