# Test Success and Failure

With the full script in place, test the two most common outcomes:

- a host replies
- a host does not reply

## Test a reachable target

Use `localhost` for a stable success test.

```bash
./hostcheck.sh localhost
echo $?
```

You should see an `UP:` message and exit code `0`.

## Test a no-reply target

Now test an address that should not answer ping.

```bash
./hostcheck.sh 192.0.2.1
echo $?
```

On a normal NAT-connected VM, this should produce a no-reply message and exit code `1`.

If your VM gives a route error instead, verify that the VM is actually on NAT and that it has a working default route.

## Why these exit codes matter

Your script is now returning:

- `0` when a target is reachable
- `1` when the host did not reply
- `2` when DNS failed
- `3` when no route exists

That means another script, a monitoring job, or a human tester can tell the difference between failure types without reading the whole script.

## **Screenshot 4: Reachable Target Returns UP**
**Requirement:** In one screenshot, show both of these:

- `./hostcheck.sh localhost`
- `echo $?` showing exit code `0`

## **Screenshot 5: No Reply Returns Exit Code 1**
**Requirement:** In one screenshot, show both of these:

- `./hostcheck.sh 192.0.2.1`
- `echo $?` showing exit code `1`

---
[Prev](03_add-dns-route-and-ping-checks.md) | [Home](README.md) | [Next](05_test-and-log-multiple-targets.md)
