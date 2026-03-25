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
  read -p "Enter a host or IP: " TARGET
fi

echo "You entered: $TARGET"
```

Save the file.

## Make it executable

```bash
chmod +x hostcheck.sh
ls -l hostcheck.sh
```

The long listing should now show execute bits in the mode string.

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

## Why this matters

- `TARGET="$1"` captures the first argument if one was provided
- `-z` checks whether the variable is empty
- `read -p` lets the script ask the user for input only when it needs it
- quotes around `"$TARGET"` protect the variable if spaces or odd characters ever appear

## **Screenshot 2: Executable Script with Prompt and Argument Modes**
**Requirement:** In one screenshot, show all three of these:

- `ls -l hostcheck.sh` with the execute bit visible
- `./hostcheck.sh` prompting for input and showing the value you entered
- `./hostcheck.sh 1.1.1.1` running without a prompt

---
[Prev](01_why-the-first-hostcheck-broke.md) | [Home](README.md) | [Next](03_add-dns-route-and-ping-checks.md)
