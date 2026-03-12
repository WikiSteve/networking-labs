# House Keeping

## Renaming machines

There are a few steps to renaming a computer.  We will cover the following files

/etc/hostname <--- where the actual hostname resides

/etc/hosts <-- the hostname requires an entry when the system tries to resolve its own name

We should always keep our hostname consistent with the VMware VM name

**Step 1**

Open /etc/hostname   (**sudo vi /etc/hostname**)

![vi editing /etc/hostname with the current client hostname before renaming the CA VM.](./assets/images/file-5f31d8096558b.png)

My current hostname is `your_username-client`. I'm going to change it to `your_username-CA`, then exit and save changes with `:wq` (Enter).

![vi showing the updated hostname set to the CA name and the :wq save-and-quit command.](./assets/images/file-5f31d86a409e6.png)

**Step 2**

Your system needs to resolve its own hostname. Similar to the hosts file in Windows, Linux also has one located at `/etc/hosts`.

Open the file

![/etc/hosts open in the editor with localhost and host-specific name entries.](./assets/images/file-5f31d903cda2b_slide3_flat.png)

**Step 3 - Update VMware VM name**

![VMware Workstation window showing the VM selected before opening its settings.](./assets/images/file-5f31da2be4a2f_slide4_flat.png)

Select VM > Settings

![VMware Workstation virtual machine settings window open while renaming a VM.](./assets/images/Pasted%20image%2020260302114228.png)

![VMware Workstation inventory showing the certificate authority VM name after renaming.](./assets/images/file-5f31db23d7274_slide6_flat.png)

![VMware Workstation inventory showing the LAMP server VM renamed to its new label.](./assets/images/file-5f31dbeadca60_slide6_flat.png)

Now finally reboot after changing the VMware name

![Terminal reboot attempt showing sudo unable to resolve the old hostname before the restart.](./assets/images/file-5f31db85d2e1f_slide6_flat.png)

This is because our hostname and the entry and /etc/hosts do not match.  This will be resolved after restart.

## Networking

## Networking and Access Setup

The next steps are required:

1) Set a static IP for both the LAMP server and the CA. Record those IPs. See Lab 3 on setting static IP addresses.
2) Configure the hosts file so we can refer to each VM by name instead of IP address.
3) Exchange SSH keypairs between machines.
4) Disable the requirement to enter a password when using `sudo`.

2) Configure the hosts file so we can refer to each VM by name instead of IP address

![ifconfig output on the LAMP server showing its static IPv4 address.](./assets/images/file-5f31dffb08236_slide2_flat.png)

The static IP to my LAMP server is 192.168.90.10.  Go to your opposite machine which is your CA

On your CA open /etc/hosts and add an entry that maps your LAMP server to IP address as shown below

![/etc/hosts edited on the CA machine to map the LAMP hostname to its static IP address.](./assets/images/file-5f31e3b9f1071_slide2_flat.png)

Test that the entry was successful by ping by hostname instead of IP

![ping by hostname succeeding against the LAMP server after the hosts file update.](./assets/images/file-5f31e40275acf.png)

Repeat this process for the opposite server so you can ping both VMs by hostname instead of IP only.

3) Exchange ssh keypairs between machines

We will be using secure copy. This step is not required; however, it's always nice to save typing. When done, we will be able to copy between Linux VMs without typing our password.

![ssh-keygen generating a public and private key pair on the CA machine.](./assets/images/file-5f31e1e10c2f2_slide4_flat.png)

Make sure that both machines have a private and public keypair. The quickest way is to use the `ssh-keygen` script.

Last step is to use the `ssh-copy-id` script, which will securely copy our public key to the opposite computer.
![Terminal running ssh-copy-id to the LAMP host and prompting to confirm the host fingerprint.](./assets/images/Pasted%20image%2020260302114904.png)

Verify that this worked and that the hostname has changed to the target computer.

![SSH login to the LAMP server succeeding by hostname and showing the Ubuntu banner.](./assets/images/file-5f31e47161c6e_slide6_flat.png)

Repeat this process on the other VM

4) Disable the requirement to enter a password when using sudo

![visudo or sudoers content showing the sudo group configuration where NOPASSWD is added.](./assets/images/file-5f31e57310ab4_slide7_flat.png)

Use `visudo` to edit sudoers safely. Add `NOPASSWD:` before the `ALL` statement for the sudo group. A space is optional (`NOPASSWD:ALL` and `NOPASSWD: ALL` both work).

Repeat this on any computer where you want to bypass the password prompt when using `sudo`.

DO NOT DO THIS IN PRODUCTION.

[Prev](01_introduction.md) | [Home](README.md) | [Next](03_preparing-lamp.md)
