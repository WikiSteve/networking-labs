# Publish Samba shares

[← Join Windows](./03-join-windows.md) · [Lab overview](./README.md) · [Set Windows permissions →](./05-set-windows-permissions.md)

Back on Debian, make two folders and add a small file to each.

```bash
sudo mkdir -p /srv/samba/bulletin /srv/samba/drafts
echo 'Event starts at 10 AM.' | sudo tee /srv/samba/bulletin/event.txt
echo 'Draft schedule for editors.' | sudo tee /srv/samba/drafts/draft.txt
```

Open `/etc/samba/smb.conf` with `sudo nano /etc/samba/smb.conf`. Add these sections at the bottom. Keep the existing domain configuration and built-in shares.

```ini
[Bulletin]
    path = /srv/samba/bulletin
    valid users = "@LAB\Editors" "@LAB\Reviewers"
    read only = yes

[Drafts]
    path = /srv/samba/drafts
    valid users = "@LAB\Editors"
    read only = yes
```

The `@` marks a group name. Use one backslash between `LAB` and each group name. `valid users` controls who can open each share. Both shares are read-only.

```bash
sudo testparm -s
sudo systemctl restart samba-ad-dc
```

`-s` makes `testparm` print the verified configuration without asking you to press Enter. Check for **Loaded services file OK** and both share names before restarting. The domain controller hosts these two read-only practice shares.

[← Join Windows](./03-join-windows.md) · [Lab overview](./README.md) · [Set Windows permissions →](./05-set-windows-permissions.md)
