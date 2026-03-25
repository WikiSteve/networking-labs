# Add DNS, Route, and Ping Checks

Now turn `hostcheck.sh` into a real diagnostic script.

The logic should happen in this order:

1. get a target
2. resolve it to an IPv4 address
3. confirm there is a route
4. ping it
5. return a useful exit code

## Replace the script with the full version

Open `hostcheck.sh` again.

```bash
nano hostcheck.sh
```

Replace the starter script with this version:

```bash
#!/bin/bash

# Exit codes:
# 0 = success
# 1 = no reply
# 2 = DNS lookup failed
# 3 = no route

TARGET="$1"

if [ -z "$TARGET" ]; then
  read -r -p "Enter a host or IP: " TARGET
fi

if [[ "$TARGET" =~ ^[0-9]{1,3}(\.[0-9]{1,3}){3}$ ]]; then
  IP="$TARGET"
else
  IP="$(getent ahostsv4 "$TARGET" | awk 'NR==1 {print $1}')"
fi

if [ -z "$IP" ]; then
  echo "DNS lookup failed for $TARGET. Check the hostname or DNS settings." >&2
  exit 2
fi

if ! ip route get "$IP" >/dev/null 2>&1; then
  echo "No route to $IP. Check your local IP settings or default gateway." >&2
  exit 3
fi

if ping -c 1 -W 1 "$IP" >/dev/null 2>&1; then
  echo "UP: $TARGET resolved to $IP and replied to ping."
  exit 0
else
  echo "No reply from $TARGET ($IP). The host may be down, filtered, or dropping ICMP." >&2
  exit 1
fi
```

Save the file.

If the target is already an IPv4 address, the script skips DNS lookup and uses that address directly. If the target is a hostname, the script resolves it with `getent ahostsv4`.

## Inspect name resolution manually

Before you test the script, look at the commands it depends on.

```bash
getent ahostsv4 one.one.one.one
ip route get 1.1.1.1
```

The first command should show one or more IPv4 addresses. The second should show the route your VM would use to reach `1.1.1.1`.

Example:

```text
$ getent ahostsv4 one.one.one.one
1.1.1.1         STREAM one.one.one.one
1.1.1.1         DGRAM
1.1.1.1         RAW

$ ip route get 1.1.1.1
1.1.1.1 via 172.16.171.2 dev ens33 src 172.16.171.144 uid 1000
```

Your interface name, gateway, and source IP will likely differ.

## Test the DNS failure path

Run the script with an invalid hostname and then print the exit code.

```bash
./hostcheck.sh definitely-not-a-real-hostname.invalid
echo $?
```

You should see a DNS failure message and exit code `2`.

Example:

```text
$ ./hostcheck.sh definitely-not-a-real-hostname.invalid
DNS lookup failed for definitely-not-a-real-hostname.invalid. Check the hostname or DNS settings.
$ echo $?
2
```

## Why the streams matter

This script writes success to `stdout` and problems to `stderr`.

That is why the error lines use:

```bash
>&2
```

You will use that distinction on the final page when you capture both streams with `2>&1 | tee`.

> [!IMPORTANT]
> On a correctly configured NAT VM, the `No route` branch may be hard to trigger during ordinary testing because the default route makes many destinations look reachable from a routing perspective. Keep the route check in the script anyway. Its purpose is to produce a better error if a machine truly has no route to the target.

## **Screenshot 3: DNS Failure and Route Inspection**
**Requirement:** In one screenshot, show all four of these:

- `getent ahostsv4 one.one.one.one` with an IPv4 address visible
- `ip route get 1.1.1.1`
- `./hostcheck.sh definitely-not-a-real-hostname.invalid`
- `echo $?` showing exit code `2`

---
[Prev](02_build-the-real-script.md) | [Home](README.md) | [Next](04_test-success-and-failure.md)
