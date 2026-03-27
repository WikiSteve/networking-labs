# Test and Prove Traffic

## Step 14. Verify the Local Pages First

Before you test traffic between zones, make sure each VM serves the page you expect locally.

On `outside`, run:

```bash
hostname
ip -4 addr show
curl http://127.0.0.1
```

On `inside`, run:

```bash
hostname
ip -4 addr show
curl http://127.0.0.1
```

On `dmz`, run:

```bash
hostname
ip -4 addr show
curl http://127.0.0.1
curl http://127.0.0.1:8080
```

Validate:

- `outside` returns `I am outside`
- `inside` returns `I am inside`
- `dmz` returns `I am dmz`
- `dmz` port `8080` returns `This is the secret internal service. Outside is not invited.`

Record:

- the current `outside` IP address
- the current pfSense `WAN` IP address from `Status > Interfaces`

You will use those two values in the required screenshots below.

> [!NOTE]
> You need two different IP addresses for the next tests:
>
> - the `outside` VM's own IP address
> - the pfSense `WAN` IP
>
> These are **not** the same thing. When you test `outside -> WAN`, use the
> pfSense `WAN` IP as the target.

## Step 15. Prove the Public `DMZ` Service and the Blocked `8080` Service from `outside`

On the `outside` VM, run:

```bash
curl http://<PFSENSE_WAN_IP>
curl -v --max-time 5 http://<PFSENSE_WAN_IP>:8080
```

Replace `<PFSENSE_WAN_IP>` with the current pfSense `WAN` IP you recorded.

Do **not** use the `outside` VM's own IP in these commands.

This is the same public-vs-blocked path shown in the page 03 **WAN inbound decision** diagram:

- `outside -> WAN:80` should forward to the public `DMZ` page
- `outside -> WAN:8080` should fail

Expected results:

- port `80` returns `I am dmz`
- port `8080` fails
- depending on how the rule is handled, you may see either a timeout or a connection failure message; both are acceptable failed outcomes here

This proves:

- the public `WAN` port forward works
- the internal-only `DMZ` service is not exposed on `WAN`

## **Screenshot 4: Outside Reaches WAN Port 80 but Not WAN Port 8080**
**Requirement:** In one screenshot, show the `outside` VM successfully reaching the current pfSense `WAN` IP on port `80` and failing to reach that same `WAN` IP on port `8080`.

## Step 16. Prove the Internal-Only `DMZ` Service from `inside`

On the `inside` VM, run:

```bash
curl http://10.20.20.100:8080
```

Expected result:

- the page returns `This is the secret internal service. Outside is not invited.`

Expected behavior note:

- `inside -> 10.20.20.100:80` should also work
- do not submit a screenshot for that extra check

Why this works:

- pfSense creates a default `LAN` rule that allows traffic from `LAN` to any destination
- `inside` is on `LAN`, so it is allowed to start a connection to the `DMZ`
- this is expected behavior in this lab

If you wanted to stop `inside -> DMZ`, you would need an explicit `LAN` rule to block it.

## **Screenshot 5: Inside Reaches the DMZ Internal Service on Port 8080**
**Requirement:** Show the `inside` VM reaching `10.20.20.100:8080` and receiving the internal-only page.

## Step 17. Prove `inside -> outside`

On the `inside` VM, run:

```bash
curl http://<OUTSIDE_VM_IP>
```

Replace `<OUTSIDE_VM_IP>` with the `outside` VM IP you recorded in Step 14.

Expected result:

- the page returns `I am outside`

Why this matters:

- `inside` can go outbound through pfSense toward `WAN`
- outbound access is not the same thing as exposing `inside` to the public `WAN`

## **Screenshot 6: Inside Reaches Outside**
**Requirement:** Show the `inside` VM reaching the current `outside` VM IP and receiving the `I am outside` page.

## Final Check: Traffic Behaviour

Before you submit, make sure you can explain:

1. Why did `outside` reach the `DMZ` page on port `80`?
2. Why did `outside` fail on port `8080`?
3. Why did `inside` reach the internal-only `DMZ` service?
4. Why did `inside` still reach the `outside` page?
5. Why is the pfSense GUI safer on `MGMT` than on `LAN`?

---
[Prev](03_inspect-wan-rules-and-nat.md) | [Home](README.md) | [Next](05_submission-guide.md)
