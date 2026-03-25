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
- the current pfSense `WAN` IP address

You will use those two values in the required screenshots below.

## Step 15. Prove the Public `DMZ` Service and the Blocked `8080` Service from `outside`

On the `outside` VM, run:

```bash
curl http://<PFSENSE_WAN_IP>
curl -v --max-time 5 http://<PFSENSE_WAN_IP>:8080
```

Replace `<PFSENSE_WAN_IP>` with the current pfSense `WAN` IP you recorded.

Expected results:

- port `80` returns `I am dmz`
- port `8080` fails

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

Why this matters:

- a higher-security-side client reaching a lower-security-side service is normal in many firewall designs
- this lab is not an ASA lab, but you should still recognize that this is expected behavior here

## **Screenshot 5: Inside Reaches the DMZ Internal Service on Port 8080**
**Requirement:** Show the `inside` VM reaching `10.20.20.100:8080` and receiving the internal-only page.

## Step 17. Prove `inside -> outside`

On the `inside` VM, run:

```bash
curl http://<OUTSIDE_VM_IP>
```

Replace `<OUTSIDE_VM_IP>` with the current `outside` VM IP you recorded earlier.

Expected result:

- the page returns `I am outside`

Why this matters:

- `inside` can go outbound through pfSense toward `WAN`
- outbound access is not the same thing as exposing `inside` to the public `WAN`

## **Screenshot 6: Inside Reaches Outside**
**Requirement:** Show the `inside` VM reaching the current `outside` VM IP and receiving the `I am outside` page.

## Final Check

Before you submit, make sure you can explain:

1. Why did `outside` reach the `DMZ` page on port `80`?
2. Why did `outside` fail on port `8080`?
3. Why did `inside` reach the internal-only `DMZ` service?
4. Why did `inside` still reach the `outside` page?
5. Why is the pfSense GUI safer on `MGMT` than on `LAN`?

---
[Prev](03_inspect-wan-rules-and-nat.md) | [Home](README.md) | [Next](05_submission-guide.md)
