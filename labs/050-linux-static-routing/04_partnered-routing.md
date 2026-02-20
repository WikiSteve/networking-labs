# Partnered routing

### **Task 1: Configuring VMware in Bridged Mode**

- Open VMware Workstation and select your Debian VM.
- Access the VM's settings and navigate to **Network Adapter**.
- Set the network mode to **Bridged** and ensure **Connect at power on** is checked.
- Start your VM and ensure it obtains an IP address from the school's DHCP pool.

### **Task 2: Setting Up the Tunnel Adapter**

- Open a terminal on your Debian VM.
- Refer to the provided spreadsheet to determine your assigned tunnel adapter address.
- Configure your tunnel adapter with the assigned address:
  ```bash
  sudo ip tuntap add mode tun tun0
  sudo ip addr add [Your Assigned Address] dev tun0
  sudo ip link set tun0 up
  ```

### **Task 3: Establishing Static Routes**

- Exchange IP addresses with your partner. These should be the addresses assigned by the school's DHCP server.
- Set up a static route to your partner's assigned network:
  **`sudo ip route add [Partner's Assigned Network] via [Partner's DHCP IP]`**

### **Submission Guidelines**

- Ensure your VM's hostname is set in the format of your first initial followed by your last name, and then `-Debian` (e.g., `dduck-Debian`).
- Initiate a traceroute from your VM to your partner's VM:
  **`traceroute [Partner's Tunnel Adapter IP]`**
  Capture a screenshot of the traceroute result.
- Establish an SSH session to your partner's VM:
  **`ssh [username]@[Partner's Tunnel Adapter IP]`**
- Once logged in, run the **`w`** command. Capture a screenshot showing the source IP as the other partner's assigned network.

---
[Prev](03_routing.md) | [Home](README.md)
