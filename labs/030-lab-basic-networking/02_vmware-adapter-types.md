# VMware Adapter types

There are several adapters available for use in Workstation that you may use in your virtual environment.  Make sure to review the link below **Selecting the Network Connection Type for a Virtual Machine.**

[Selecting the Network Connection Type for a Virtual Machine](https://docs.vmware.com/en/VMware-Workstation-Pro/16.0/com.vmware.ws.using.doc/GUID-3B504F2F-7A0B-415F-AE01-62363A95D052.html)

---
### 🧠 Knowledge Check: VMware Adapter Types

**Scenario 1: Direct Access**
> [!NOTE]
> **Question:** Which networking mode allows your virtual machine to act as a full member of your physical home network, obtaining its own IP address directly from your home router?
> 
> - [ ] **A.** NAT
> - [ ] **B.** Bridged
> - [ ] **C.** Host-only

<details>
<summary>👉 <b>Check your answer</b></summary>

**Correct Option: B**

**Feedback:** In **Bridged** mode, the VM's virtual NIC is "bridged" directly to your physical NIC, making it appear as a separate physical computer on your home network.
</details>

**Scenario 2: VMware Managed**
> [!NOTE]
> **Question:** You want VMware to act as a "middleman" that handles all routing, DNS, and DHCP services for your VM. Which mode should you select?
> 
> - [ ] **A.** NAT
> - [ ] **B.** Bridged
> - [ ] **C.** Host-only

<details>
<summary>👉 <b>Check your answer</b></summary>

**Correct Option: A**

**Feedback:** **NAT** (Network Address Translation) is the default mode. VMware creates a private internal network and "naps" the traffic to your host's IP to get out to the internet.
</details>

**Scenario 3: Connectivity vs. Isolation**
> [!NOTE]
> **Statement:** If you set your VM to **Host-only** mode, you can still SSH into the VM from your physical host, but the VM itself will have no access to the public internet.
> 
> - [ ] True
> - [ ] False

<details>
<summary>👉 <b>Reveal answer</b></summary>

**Correct:** True

**Feedback:** **Host-only** provides a private link between the host and the VM. It is perfect for local testing when you want to ensure the VM stays isolated from the outside world.
</details>

---

---
[Prev](01_evaluation.md) | [Home](README.md) | [Next](03_live-tools-net-tools.md)
