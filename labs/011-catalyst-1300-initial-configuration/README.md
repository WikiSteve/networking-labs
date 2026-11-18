# Cisco Catalyst 1300 Lab 1 — Initial Configuration

> **Before you start:** Download the [submission template](https://raw.githubusercontent.com/WikiSteve/networking-labs/refs/heads/main/labs/011-catalyst-1300-initial-configuration/Cisco%20Catalyst%201300%20Initial%20Configuration%20SUBMISSION%20TEMPLATE.pptx). Add each required screenshot as you complete the lab, then submit the completed template for grading.

[Download the interactive HTML lab](./index.html) · On the file page, click **Download raw file**, then open the saved HTML in your browser. Save the PowerPoint beside it if you want the template available offline.

## Before you start

You need a Catalyst 1300, an Ethernet cable, a Windows VM, a browser and PuTTY. Use the VM for the browser, ping and PuTTY so all three tests use the same connection.

**Keep the lab switch isolated.** Connect only to your own lab switch. Several switches may start with the same IP address. Keep this switch off the classroom network and other groups’ switches.

### Three screenshots to submit

1.  [Web GUI with your configured hostname](#screenshot-1-web-gui-hostname)
2.  [Successful ping from the VM to the switch](#screenshot-2-successful-vm-to-switch-ping)
3.  [PuTTY SSH, your hostname and version output](#screenshot-3-putty-ssh-and-switch-version)

[Lab 2](../012-catalyst-1300-vlan-routing/README.md) starts from this setup. Keep your assigned hostname and management address available for the next lab.

## 1. Connect and sign in

1.  Connect your computer’s wired Ethernet port to the lab switch. In your VM settings, bridge the VM’s lab adapter to that physical Ethernet port. Select the wired port explicitly if your virtualization software offers a choice.
2.  In Windows, press **Windows+R**, type `ncpa.cpl` and press **Enter**. This opens Network Connections.
3.  Right-click the lab adapter, choose **Properties**, select **Internet Protocol Version 4 (TCP/IPv4)**, then choose **Properties**. Select **Use the following IP address**.

### Seeing a 169.254 address?

After connecting the cable and setting the VM bridge, open Command Prompt in the VM and run:

    ipconfig

Find the Ethernet adapter connected to your switch. If Windows is set to obtain an address automatically, you might see this:

    Ethernet adapter Ethernet:

       Autoconfiguration IPv4 Address. . : 169.254.42.17
       Subnet Mask . . . . . . . . . . . : 255.255.0.0

Windows picked its own `169.254` address after it received no address from DHCP, the service that normally hands out IP settings. There’s no DHCP server handing out addresses on this isolated lab link. Your last two numbers may differ. If you see **Media disconnected**, check the cable, the switch port’s link light and the VM’s wired bridge first.

After applying the manual settings below, run `ipconfig` again and look for this on the same adapter:

    Ethernet adapter Ethernet:

       IPv4 Address. . . . . . . . . . . : 192.168.1.10
       Subnet Mask . . . . . . . . . . . : 255.255.255.0

With this mask, `192.168.1.10` and the switch’s `192.168.1.254` are on the same subnet, so they can talk over the Ethernet link without a gateway. Opening the switch page checks whether the management service is reachable. If Windows marks your address **Duplicate**, check for another VM or device using `192.168.1.10` on the same lab link.

| Setting                 | Value                    |
|-------------------------|--------------------------|
| IPv4 address            | `192.168.1.10`           |
| Subnet mask             | `255.255.255.0` (/24)    |
| Default gateway and DNS | Leave blank for this lab |

Apply the settings. In the VM browser, open `http://192.168.1.254`. On a factory-default lab switch, sign in with `cisco` as both username and password if prompted. Set the administrator username to `admin` and use the classroom password supplied by your instructor. Use that account to sign in again. If the switch rejects the password or already has an account configured, ask your instructor before changing settings.

**Cisco video · Day Zero Setup Using the Web UI**

Cisco demonstrates the initial setup wizard. Use the written addresses and settings above for this lab.

[Watch on Cisco](https://video.cisco.com/detail/video/6330931546112)

**If the GUI doesn’t open**

Check the Ethernet link light, the wired bridge selection and the VM IP and mask. Confirm that only your lab adapter has a path to this subnet. If the address still doesn’t answer, ask whether the switch’s management IP was changed. Stop and ask before resetting shared hardware.

## 2. Set the hostname

### Screenshot 1: Web GUI hostname

**Requirement:** Show the logged-in Web GUI on the hostname settings page with your configured hostname visible.

1.  In the Web GUI, open **Administration → System Settings**.
2.  Under **Host Name**, choose **User Defined**. Use your first initial followed by your last name and end with `r1` after a hyphen. For example, `ssharpe-r1`.
3.  Click **Apply**. Confirm the configured name is visible. Use the GUI’s **Save** control to save the configuration to startup configuration.

**Apply** makes a change active now. **Save** makes it survive a restart.

## 3. Test connectivity with ping

### Screenshot 2: Successful VM-to-switch ping

**Requirement:** Show the ping command and successful replies from `192.168.1.254` in the VM.

Open Command Prompt in the VM and run:

    ping 192.168.1.254

### Example output

    Reply from 192.168.1.254: bytes=32 time<1ms TTL=64
    …
        Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)

Check the address after **Reply from**. It should be `192.168.1.254`. The time and TTL can differ. An actual reply shows that the VM sent a request and the switch sent a reply back. If you see a timeout or **Destination host unreachable**, check the adapter, cable, IP and mask, then try again. A reachable switch can still have SSH disabled.

## 4. Enable SSH and connect with PuTTY

### Screenshot 3: PuTTY SSH and switch version

**Requirement:** Show the successful PuTTY SSH session, your hostname at the CLI prompt, and the output of `show version`. Keep passwords out of the screenshot.

1.  In the Web GUI, switch to **Advanced Mode** if necessary. Open **Security → TCP/UDP Services**, enable **SSH Service**, then click **Apply** and save the configuration.
2.  Open PuTTY in the VM and use these settings:

| Location                                | Value           |
|-----------------------------------------|-----------------|
| Session → Host Name                     | `192.168.1.254` |
| Session → Port / connection type        | `22` / SSH      |
| Connection → Data → Auto-login username | `admin`         |

Return to **Session** and select **Open**. On the first connection to your isolated lab switch, choose **Accept** if PuTTY asks whether to remember the switch’s public host key. If PuTTY later says the key changed, a different switch may be using the same IP address, or your switch may have generated a new key after a reset. Sign in with the administrator password. PuTTY may display nothing while you type it.

### Check which switch you reached

At the switch prompt, run:

    show version

### Example output excerpt

    ssharpe-r1# show version
    SW version 3.131
    …

The example uses Cisco’s documented output format. Check that the hostname at the prompt is yours and find the software version line. Your version and the additional fields may differ. If the prompt ends in `>` and the command is unavailable, type `enable` to request privileged mode, then try again. Ask your instructor if your account cannot enter that mode.

**If PuTTY won’t connect**

Check ping first. If ping works and PuTTY reports a refused or timed-out connection, check the SSH service in the GUI, then confirm the PuTTY address, port 22 and SSH connection type. If PuTTY opens a login prompt, the network path and SSH service are working. Check the account or password if sign-in fails.

**Cisco video · Using PuTTY to Access the CLI**

The video uses a Cisco Business switch. Follow this lab’s Catalyst 1300 address and SSH settings.

[Watch on Cisco](https://video.cisco.com/detail/video/6304396209001)

**Cisco video · Common CLI Commands**

Watch for the switch prompt and the distinction between viewing and changing settings.

[Watch on Cisco](https://video.cisco.com/detail/video/6347762586112)

## 5. Submit and save

Submit the completed PowerPoint with your three screenshots in order:

1.  [Web GUI showing your configured hostname](#screenshot-1-web-gui-hostname)
2.  [Successful VM-to-switch ping](#screenshot-2-successful-vm-to-switch-ping)
3.  [PuTTY SSH showing your hostname and `show version`](#screenshot-3-putty-ssh-and-switch-version)

**Before you leave:** Save the switch configuration in the GUI so it survives a reboot. Leave the management IP and SSH working for Lab 2. Follow the instructor’s directions for shared equipment.

**Optional · Try the console**

If you have a compatible console cable, connect directly to the switch and try PuTTY in **Serial** mode. Ask your instructor which cable and serial settings your switch uses. No console screenshot is required.
