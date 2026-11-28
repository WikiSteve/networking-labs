# Verify the wired Partner PC

[← Give clients their LAN settings](./04-enable-lan-addressing.md) · [Lab overview](./README.md) · [Connect both phones →](./06-connect-both-phones.md)

1. Use only the isolated bench link on the Partner PC for this check. Temporarily turn off its Wi-Fi and disconnect its other Ethernet cables. Keep the Router PC’s upstream connection in place.
2. In Command Prompt, run `ipconfig /all` and find the same dedicated adapter. Expect an IPv4 address from `192.168.77.100` to `192.168.77.149`. The IPv4 default gateway and DHCP server should be `192.168.77.1`. Look for an IPv6 address in addition to its link-local address and an IPv6 default gateway.
3. Open a private browser window and go to `http://minion.lab/`. If the Minion page appears, the wired web check passed. Keep the address bar visible for Screenshot 4. In this lab, OpenWrt gives Minion an IPv6 address.

If the browser cannot resolve the name, run `nslookup minion.lab 192.168.77.1` in Command Prompt to ask OpenWrt directly. A correct answer shows that DNS works. Loading the page is the separate web check.

If Windows shows **Destination port unreachable** when you ping Minion, continue with the browser check. See [why the Minion page can load when ping fails](./09-troubleshooting.md#minion-opens-but-ping-reports-destination-port-unreachable).

## **Screenshot 4: Prove the partner’s wired connection**

**Requirement:** Show the Partner PC’s wired adapter name, IPv4 lease, IPv6 address, default gateways and DHCP server beside the Minion portal at `http://minion.lab/`. In the slide notes, record whether Minion opened with only the wired bench connection active.

![Partner PC’s Intel Ethernet configuration beside the Minion portal](./evidence/04-wired.png)

## Optional Windows check · See the HTTP status

Windows 11 includes `curl.exe`. Run it in Command Prompt to view the web response over IPv6.

```text
curl.exe -6 -I http://minion.lab/
```

The `-6` option uses IPv6. The capital `-I` shows the response headers. Look for **200 OK**.

[← Give clients their LAN settings](./04-enable-lan-addressing.md) · [Lab overview](./README.md) · [Connect both phones →](./06-connect-both-phones.md)
