# Why the First Hostcheck Broke

At the end of Part 1, you saw a `hostcheck` idea that worked when everything happened in the current shell. The problem appeared when you saved that logic in a script and executed it later.

This page shows exactly what broke and why the real fix is to move the `ping` into the script itself.

## Create a working folder

Open a terminal and create a clean folder for this lab.

```bash
mkdir -p ~/bash-healthcheck-lab
cd ~/bash-healthcheck-lab
```

## Create the broken example

Create a file named `badhostcheck.sh`.

```bash
nano badhostcheck.sh
```

Paste this content:

```bash
#!/bin/bash

if [ $? -eq 0 ]; then
  echo "UP"
else
  echo "DOWN"
fi
```

Save the file.

This script is intentionally wrong. It checks `$?`, but it never ran the command that produced that exit code.

## Demonstrate the problem

Run a ping that should fail. The documentation address `192.0.2.1` is useful for this kind of test.

```bash
ping -c 1 -W 1 192.0.2.1 >/dev/null 2>&1
echo $?
bash badhostcheck.sh
```

If your VM is working normally on NAT, the ping should fail and `echo $?` should print a non-zero value. The saved script still prints `UP` because `bash badhostcheck.sh` started a new shell process.

Example:

```text
$ ping -c 1 -W 1 192.0.2.1 >/dev/null 2>&1
$ echo $?
1
$ bash badhostcheck.sh
UP
```

## Compare it to sourcing

Run the failed ping again, then source the file instead of executing it.

```bash
ping -c 1 -W 1 192.0.2.1 >/dev/null 2>&1
. ./badhostcheck.sh
```

This time the file runs in your current shell, so it can still see the exit code from the ping you just ran.

Example:

```text
$ ping -c 1 -W 1 192.0.2.1 >/dev/null 2>&1
$ . ./badhostcheck.sh
DOWN
```

## What you should learn from this

The point of this page is not that you should solve everything with `source`.

The point is:

- a saved script does not automatically inherit the caller's previous exit code in a useful way
- sourcing runs in the current shell, but that is not the right design for a reusable host-check script
- the real fix is to run the `ping` inside the script and let the script return its own exit code

`badhostcheck.sh` was only a demo. The real script starts on the next page.

## **Screenshot 1: Broken Script vs Sourced Script**
**Requirement:** In one screenshot, show all three of these:

- a failed `ping -c 1 -W 1 192.0.2.1 >/dev/null 2>&1`
- `echo $?` showing a non-zero value and `bash badhostcheck.sh` printing `UP`
- `. ./badhostcheck.sh` printing `DOWN`

---
[Home](README.md) | [Next](02_build-the-real-script.md)
