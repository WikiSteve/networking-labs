# Before you start

[Lab overview](./README.md) · [Create the domain →](./02-create-the-domain.md)

## Name your VMs before configuration

Use your first name on all three VMs and your last name in the AD domain. Use letters A–Z and omit spaces and punctuation. If needed, shorten the first name to 11 letters so `-W11` fits the Windows computer name limit. This guide uses Maya Lee as its example. The computers are `maya-dc`, `MAYA-FS`, and `MAYA-W11`, and the domain is `lee-lab.internal`. Substitute your own names in the setup, DNS lookups, and share paths.

On Debian, set the hostname before provisioning Samba. Replace `maya` with your first name.

```bash
sudo hostnamectl set-hostname maya-dc
```

On Windows 11, use **Settings → System → About → Rename this PC** and set the `-W11` name. On Windows Server, use **Server Manager → Local Server**, click the current computer name, then choose **Computer Name → Change** and set the `-FS` name. Restart both before joining the domain.

| VM                                                  | Name       | Role                                                        |
|-----------------------------------------------------|------------|-------------------------------------------------------------|
| Fresh Debian 13 (Trixie)                            | `maya-dc`  | Samba domain controller, DNS, and two small practice shares |
| Windows Server 2022 or 2025 with Desktop Experience | `MAYA-FS`  | Domain member and Windows file server                       |
| Windows 11 Education                                | `MAYA-W11` | Domain member and test client                               |

Use your own VMs on one shared private NAT network. In VirtualBox, choose NAT Network for all three VMs and select the same network. Check that the VM clocks agree before joining. Avoid bridging the lab to the campus network. The 40-minute target starts after VM and package preparation. Check that the three VMs can reach each other and give Debian a stable IPv4 address. Write down the Debian address and the current DNS server for Internet lookups. Use local administrator accounts on Windows for setup. The Windows Server VM starts as a standalone server.

On Debian, install these packages before timing the lab:

```bash
sudo apt update
sudo apt install samba-ad-dc krb5-user bind9-dnsutils
```

Press Enter to accept the defaults if Kerberos setup asks for a realm or servers. You will replace its configuration during the lab.

[Lab overview](./README.md) · [Create the domain →](./02-create-the-domain.md)
