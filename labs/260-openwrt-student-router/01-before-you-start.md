# Before you start

[Lab overview](./README.md) · [Verify the VMware networks →](./02-verify-vmware-networks.md)

Your pair will build a private network and open the Minion lab portal from a wired PC and two phones. The Student Router VM gives your devices addresses and runs your team's Wi-Fi. The Minion Bridge VM gives that router a path to the portal. Each of the six required screenshots has a worked bench example.

[Download the PowerPoint submission template](https://github.com/WikiSteve/networking-labs/releases/download/openwrt-student-router-lab/OpenWrt-Student-Router-Lab-Submission-Template.pptx). Keep one copy per pair and add each capture when its numbered box appears.

## Pick your two PCs

- **Router PC.** Run both OpenWrt VMs in VMware Workstation here and open LuCI in this PC's browser. Keep the upstream cable on Realtek and leave the separate Intel I210-T1 bench jack unplugged until Step 3.
- **Partner PC.** Use its dedicated Ethernet connection as the wired test client. You don't need to open VMware on this PC.
- **One workstation?** Keep both OpenWrt VMs on it and follow the [one-workstation bench setup](./04-enable-lan-addressing.md#one-workstation-with-a-windows-partner-vm) in Step 3.

Use one isolated switch, two Ethernet patch cables, two phones, and a supported USB Wi-Fi adapter. The worked example uses a Catalyst 1300 and TP-Link Archer T4U v3. In Step 3, you'll use two same-VLAN access ports on the isolated switch and check that it has no uplink.

## Get the two VMs ready

The Minion Bridge VM needs a web server reachable on the Router PC's upstream network. Before you start, have your instructor follow the [portal setup guide](./PORTAL-SETUP.md).

If you can identify both as the copies your pair set up, skip the download and extraction and go to [Step 1](./02-verify-vmware-networks.md). If you only see tabs left by another pair, open fresh copies from your own folder.

1. [Download OpenWrt Student VMs.zip](https://github.com/WikiSteve/networking-labs/releases/download/openwrt-student-router-lab/OpenWrt-Student-VMs.zip) on the Router PC. In File Explorer, right-click the ZIP, choose **Extract All**, and extract to **Downloads → OpenWrt Student VMs**.
2. Open the extracted folder. Turn on **View → Show → File name extensions** in File Explorer. The `.vmx` is the VM file you open. The `.vmdk` is its virtual disk. Keep each disk beside its corresponding VM file.
3. Use **File → Open** twice in VMware Workstation. Open `Minion Bridge/Minion-Bridge.vmx` and `OpenWrt Student/OpenWrt-Student.vmx`.
4. Check that **Minion Bridge** and **OpenWrt Student Router** both appear. Leave them powered off while you [verify the adapter settings](./02-verify-vmware-networks.md#verify-the-two-vms-adapters).

## Follow a portal request

| Link | What it does |
|---|---|
| Wired Partner PC → isolated switch → Intel I210-T1 → Student Router | Carries Ethernet from the partner into the router's private LAN through VMnet10. |
| Two phones → team Wi-Fi → Archer T4U → Student Router | Connects the phones to the same LAN over Wi-Fi. |
| Student Router → Minion-WAN → Minion Bridge | Connects the router's WAN to the Bridge over a private VMware LAN segment. |
| Minion Bridge → VMware NAT (VMnet8) → upstream → Minion portal | Relays the portal request to the lab web server. |

The Router PC's browser reaches LuCI at `http://192.168.220.2/` over VMnet1. That management connection stays inside the Router PC. In the partner test, you'll check that the Student Router gives Windows an IPv4 address and that Windows reaches `http://minion.lab/` over IPv6.

[Lab overview](./README.md) · [Verify the VMware networks →](./02-verify-vmware-networks.md)
