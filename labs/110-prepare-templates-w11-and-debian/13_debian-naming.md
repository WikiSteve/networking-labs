# Debian Naming

## Hostname Configuration with FQDN Guide

**Purpose of the FQDN:**

The **Fully Qualified Domain Name (FQDN)** format helps you get comfortable with network naming conventions, even if this isn’t a routed environment. The FQDN format we’ll use is: `firstInitialLastName-clone.LastName.com`.

- For instance, if your name is Steve Sharpe, your FQDN will be `ssharpe-clone.sharpe.com`.

**Take a Snapshot First!**

Before diving in, take a snapshot of your VM. This gives you a quick way to recover if anything goes awry.

**Update the Hosts File First (Prevent Lockout):**

Open `/etc/hosts` **before** making any changes to `/etc/hostname` to ensure you don’t accidentally lock yourself out of `sudo`:

```bash
sudo nano /etc/hosts
```

In the hosts file, find the line with your **old hostname** (let’s say it’s `old-hostname`), and add a **new line** with your new FQDN and short hostname:

```text
127.200.200.200    old-hostname

127.200.200.200    firstInitialLastName-clone.LastName.com    firstInitialLastName-clone
```

For example, if your old hostname is `old-hostname` and you’re changing it to `ssharpe-clone.sharpe.com`, your entries should look like this:

```text
127.200.200.200    old-hostname

127.200.200.200    ssharpe-clone.sharpe.com    ssharpe-clone
```

Save and close (in nano, `Ctrl + X`, then `Y`, and `Enter`).

**Change the Hostname:**

- Now that you’ve updated `/etc/hosts` safely, open `/etc/hostname` to change the system’s hostname:

```bash
sudo nano /etc/hostname
```

Replace the old hostname with your new hostname in the format:

```text
firstInitialLastName-clone
```

- Example: `ssharpe-clone`.

- Save and close the file.

**Reboot and Check `sudo` Access:**

- Restart your VM to apply changes:

```bash
sudo reboot
```

After rebooting, check `sudo` by running:

```bash
sudo echo "not locked out!"
```

If it responds with "not locked out!" you’re good to go!

**Final Cleanup (Remove Old Hostname):**

- Once you’re sure everything is working, open `/etc/hosts` one last time and remove the line with the old hostname, keeping only the new FQDN line:

```text
127.200.200.200    ssharpe-clone.sharpe.com    ssharpe-clone
```

Then do a final check to confirm `sudo` is still accessible:

```bash
sudo echo "still not locked out!"
```

---
[Prev](12_debian-software.md) | [Home](README.md) | [Next](14_debian-time.md)
