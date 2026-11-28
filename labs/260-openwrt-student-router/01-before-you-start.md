# Before you start

[Lab overview](./README.md) · [Verify the VMware networks →](./02-verify-vmware-networks.md)

- Use two Windows PCs, VMware Workstation on the **Router PC**, an isolated switch, two Ethernet cables, two phones and a supported USB Wi-Fi adapter. The worked example uses a Catalyst 1300 and a TP-Link Archer T4U v3.
- The Router PC uses one Ethernet adapter for its upstream lab network and a separate Intel I210-T1 for your isolated bench. The **Partner PC** uses its own dedicated Ethernet connection to the bench.
- The Minion Bridge VM needs a portal server reachable on the upstream network. Have your instructor follow the [portal setup guide](./PORTAL-SETUP.md) before starting. Once that setup is complete, lab clients browse to `http://minion.lab/`.
- Extract the VM ZIP. In VMware Workstation, choose **File → Open** for `Minion Bridge/Minion-Bridge.vmx` and `OpenWrt Student/OpenWrt-Student.vmx`. Keep the virtual disks with their corresponding VM files. Leave both VMs powered off while you check their settings.

[Lab overview](./README.md) · [Verify the VMware networks →](./02-verify-vmware-networks.md)
