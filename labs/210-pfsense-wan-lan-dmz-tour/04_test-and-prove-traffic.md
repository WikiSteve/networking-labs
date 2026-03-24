# Test and Prove Traffic

## Step 6. Test `outside -> DMZ`

On the `outside` VM, run:

```bash
curl http://192.168.50.1
```

Validate:

- the request goes to the pfSense `WAN` IP
- the returned page is `Hey I'm DMZ`

Why this matters:

- this proves the port forward works
- this proves pfSense `WAN` port `80` is intentionally exposed to the `dmz` web service

## **Screenshot 4: Outside Reaches the DMZ**
**Requirement:** Show the `outside` VM sending a `curl` request to `192.168.50.1` and receiving the `Hey I'm DMZ` page.

## Step 7. Test a Non-Forwarded `WAN` Port

On the `outside` VM, run:

```bash
curl -v --max-time 5 http://192.168.50.1:8080
```

Validate:

- the connection fails
- no page is returned

What `--max-time 5` means:

- it stops `curl` from hanging too long if the connection never completes
- the expected firewall-block result is usually a timeout or empty response
- if you get `Connection refused`, treat that as a misconfiguration and re-check the `WAN` rules and port forward

Why this matters:

- there is no port forward for `WAN` port `8080`
- this is the correct way to test a blocked non-forwarded service from `outside`
- do **not** test `curl http://10.0.1.10` from `outside`
- directly targeting `10.0.1.10` from the `outside` network would only prove the client has no route to that private network

## **Screenshot 5: Outside Cannot Reach a Non-Forwarded WAN Service**
**Requirement:** Show the `outside` VM attempting to reach `http://192.168.50.1:8080` and failing. The screenshot must include the failed `curl` output.

## Step 8. Test `inside -> outside`

On the `inside` VM, run:

```bash
curl http://192.168.50.10
```

Validate:

- the returned page is `Hey I'm Outside`
- outbound access from the LAN works

Why this matters:

- outbound access is different from inbound exposure
- the `inside` VM is not on the same LAN Segment as `outside`
- pfSense must route this traffic from `LAN` to `WAN`
- this prebuilt lab already includes the normal LAN allow behavior needed for this test
- the `inside` host can reach `outside` without the `inside` host being publicly exposed

## **Screenshot 6: Inside Reaches Outside**
**Requirement:** Show the `inside` VM sending a `curl` request to `192.168.50.10` and receiving the `Hey I'm Outside` page.

## Step 9. Prove the Allowed `outside -> DMZ` Connection in pfSense

On the `outside` VM, start this loop and leave it running:

```bash
while true; do curl -s http://192.168.50.1 > /dev/null; sleep 1; done
```

Now return to pfSense and open:

- `Diagnostics > States`

Filter the page for:

- `10.0.2.10`

Return to the pfSense **States** tab and refresh until you see the matching state entry.

You are looking for a state that proves:

- source `192.168.50.10`
- the `dmz` host `10.0.2.10`
- web traffic on port `80`
- the connection is active while your loop is running

Depending on the pfSense version, the state table may show this as one entry or as a state pair. The important evidence is that the active connection involves both the `outside` client and the `dmz` web server while the test is running.

When your screenshot is done, stop the loop on the `outside` VM with `Ctrl+C`.

Why this matters:

- the state entry proves pfSense tracked the session
- this is stronger proof than just “the page loaded”
- this shows the connection really entered on `WAN` and was redirected to the `dmz` host

## **Screenshot 7: pfSense State for the Allowed DMZ Connection**
**Requirement:** Show the pfSense **States** page with the active state entry for the `outside -> DMZ` connection visible.

## Step 10. Prove the Blocked Non-Forwarded `WAN` Attempt in pfSense

In this lab environment, the explicit `WAN` block rule for port `8080` has logging enabled.

On the `outside` VM, run the blocked test a few times:

```bash
for i in 1 2 3; do curl -sS --max-time 2 http://192.168.50.1:8080 > /dev/null; sleep 1; done
```

Now go to:

- `Status > System Logs > Firewall`

Refresh the log page and look for a blocked entry involving:

- source `192.168.50.10`
- destination `192.168.50.1`
- destination port `8080`
- interface `WAN`

If the page shows a **Display Filter** button, open it and filter by the source IP or destination port before refreshing.

If your build does not show that filter panel, use your browser page search for `192.168.50.10` or `8080`.

Why this matters:

- this proves pfSense saw the packet on `WAN`
- this proves pfSense blocked a service that was not explicitly exposed
- this is stronger than a client-side failure message by itself

## **Screenshot 8: pfSense Log for the Blocked WAN Attempt**
**Requirement:** Show the pfSense firewall log entry for the blocked attempt to reach `192.168.50.1:8080` from `192.168.50.10`.

## Step 11. Inspect Outbound NAT

In pfSense, go to:

- `Firewall > NAT > Outbound`

Validate:

- **Automatic outbound NAT rule generation** is enabled

Why this matters:

- this explains why the `inside` VM can reach the `outside` network through pfSense
- pfSense is handling outbound NAT for the internal network

## **Screenshot 9: Automatic Outbound NAT**
**Requirement:** Show the pfSense **Outbound NAT** page with **Automatic outbound NAT rule generation** visible.

## Step 12. Prove the `inside -> outside` Session in pfSense

On the `inside` VM, start this loop and leave it running:

```bash
while true; do curl -s http://192.168.50.10 > /dev/null; sleep 1; done
```

Now return to pfSense and open:

- `Diagnostics > States`

Filter the page for:

- `10.0.1.10`

Return to the pfSense **States** tab and refresh until you see the session.

You are looking for a state that proves:

- source `10.0.1.10`
- destination `192.168.50.10`
- traffic moving from `LAN` toward `WAN`

If the page also shows `192.168.50.1` as the WAN-side translated source, that is direct outbound NAT evidence. If it does not, the combination of this active state and the **Outbound NAT** page is still the proof set for this lab.

When your screenshot is done, stop the loop on the `inside` VM with `Ctrl+C`.

Why this matters:

- this shows pfSense handled the outbound session
- together with the Outbound NAT page, it explains why the LAN host can reach the WAN host

## **Screenshot 10: State for the Inside-to-Outside Session**
**Requirement:** Show the pfSense **States** page with the state entry for the `inside -> outside` session visible.

## Step 13. Explain What Happened

Be ready to explain these in plain language:

1. Why can `outside` reach the `DMZ` page?
2. Why can `outside` not reach a non-forwarded service on the `WAN` side?
3. Why can `inside` reach `outside`?
4. Which parts were NAT, and which parts were firewall filtering?

## References

The following pfSense documentation supports the concepts used in this lab:

- WAN vs LAN behavior: <https://docs.netgate.com/pfsense/en/latest/interfaces/wanvslan.html>
- Outbound NAT defaults: <https://docs.netgate.com/pfsense/en/latest/nat/outbound-nat.html>
- General NAT behavior: <https://docs.netgate.com/pfsense/en/latest/nat/>
- Testing port forwards from local networks: <https://docs.netgate.com/pfsense/en/latest/nat/accessing-port-forwards-from-local-networks.html>
- Viewing firewall states in the GUI: <https://docs.netgate.com/pfsense/en/latest/monitoring/status/firewall-states-gui.html>
- NAT port forward troubleshooting: <https://docs.netgate.com/pfsense/en/latest/troubleshooting/nat-port-forwards.html>

---
[Prev](03_inspect-wan-rules-and-nat.md) | [Home](README.md) | [Next](05_submission-guide.md)
