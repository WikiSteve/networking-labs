# Install Your Key on Both Linux Systems

Once the public key is on GitHub, you can import it onto each Linux system.

## Ubuntu workflow

On Ubuntu, the import helper is often already available:

```bash
ssh-import-id gh:your-github-username
```

If it succeeds, your public key is added to `~/.ssh/authorized_keys`.

## CentOS or RHEL workflow

On older CentOS or RHEL systems, `ssh-import-id` may not already be installed. If the command is available, use the same import:

```bash
ssh-import-id gh:your-github-username
```

If it is not available, you can still install your key manually by pulling the public keys from GitHub:

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
curl https://github.com/your-github-username.keys >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

If you use the manual method more than once, check `~/.ssh/authorized_keys` so you do not keep appending duplicate keys.

## Verify the result

After importing, check that the `.ssh` directory and `authorized_keys` file exist:

```bash
ls -al ~/.ssh
cat ~/.ssh/authorized_keys
```

You should see your uploaded public key in the file.

## Why this matters

At this point, each Linux system knows your public key. The next step is to make PuTTY present the matching private key when you connect.

---
[Prev](03_publish-your-public-key-to-github.md) | [Home](README.md) | [Next](05_configure-putty-to-use-your-private-key.md)
