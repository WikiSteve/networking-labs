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

Example:

```text
$ ./hostcheck.sh localhost
UP: localhost resolved to 127.0.0.1 and replied to ping.
$ echo $?
0
```

## Test a no-reply target

Now test an address that should not answer ping.

```bash
./hostcheck.sh 192.0.2.1
echo $?
```

On a normal NAT-connected VM, this should produce a no-reply message and exit code `1`.

If your VM gives a route error instead, verify that the VM is actually on NAT and that it has a working default route.

Common result on a NAT-connected VM:

```text
$ ./hostcheck.sh 192.0.2.1
No reply from 192.0.2.1 (192.0.2.1). The host may be down, filtered, or dropping ICMP.
$ echo $?
1
```

Possible alternate result:

```text
$ ./hostcheck.sh 192.0.2.1
No route to 192.0.2.1. Check your local IP settings or default gateway.
$ echo $?
3
```

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

## **Screenshot 5: Failure Path Returns a Diagnostic Exit Code**
**Requirement:** In one screenshot, show both of these:

- `./hostcheck.sh 192.0.2.1`
- `echo $?` showing exit code `1` or `3`

Do not change your networking just to force one specific result. If your VM reaches the failure path and returns a meaningful non-zero diagnostic exit code, that is acceptable for grading.

---
[Prev](03_add-dns-route-and-ping-checks.md) | [Home](README.md) | [Next](05_test-and-log-multiple-targets.md)
