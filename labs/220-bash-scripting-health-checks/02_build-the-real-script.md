# Build the Real Script

Now build the real `hostcheck.sh`.

This version should:

- accept a target as `$1`
- prompt with `read` if no target was passed
- run as an executable file instead of being sourced

## Create `hostcheck.sh`

Open the file in `nano`.

```bash
nano hostcheck.sh
```

Paste this starter version:

```bash
#!/bin/bash

TARGET="$1"

if [ -z "$TARGET" ]; then
  read -r -p "Enter a host or IP: " TARGET </dev/tty
fi

echo "You entered: $TARGET"
```

Save the file.

## Make it executable

```bash
chmod +x hostcheck.sh
ls -l hostcheck.sh
```

The long listing should now show:

- execute bits in the mode string
- your own username as the owner, not `root root`

If `ls -l hostcheck.sh` shows `root root`, stop and fix that before you continue.

One repair option is:

```bash
sudo chown "$USER":"$(id -gn)" hostcheck.sh
```

You should not need `sudo` for this lab in your home folder except to repair a file you already created as `root`.

## Test prompt mode

Run the script with no argument.

```bash
./hostcheck.sh
```

When prompted, enter:

```text
localhost
```

You should see:

```text
You entered: localhost
```

## Test argument mode

Now run the same script with an argument.

```bash
./hostcheck.sh 1.1.1.1
```

This time the script should not prompt because `$1` already supplied the target.

Example:

```text
$ ./hostcheck.sh 1.1.1.1
You entered: 1.1.1.1
```

## Why this matters

- `TARGET="$1"` captures the first argument if one was provided
- `-z` checks whether the variable is empty
- `read -r -p ... </dev/tty` lets the script ask the user for input only when it needs it, without treating backslashes specially
- reading from `/dev/tty` keeps prompt mode tied to the terminal, even if standard input is redirected later
- quotes around `"$TARGET"` protect the variable if spaces or odd characters ever appear

## **Screenshot 2: Executable Script with Prompt and Argument Modes**
**Requirement:** In one screenshot, show all three of these:

- `ls -l hostcheck.sh` with the execute bit visible
- `./hostcheck.sh` prompting for input and showing the value you entered
- `./hostcheck.sh 1.1.1.1` running without a prompt

---
[Prev](01_why-the-first-hostcheck-broke.md) | [Home](README.md) | [Next](03_add-dns-route-and-ping-checks.md)
