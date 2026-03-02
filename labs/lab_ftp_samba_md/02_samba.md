# samba

![Screenshot](./assets/images/file-5f2ff8729807f.png)

*A file and printer sharing daemon that is fully Active Directory aware!*

Start by installing samba using apt-get (package name is samba)

We need a base directory for our shares plus a subdirectory your_username. Create one off of root **mkdir -p /share/your_username**
> **Note:** `your_username` is first initial + last name.

Create the group supersecret and add your_username to this group.  Add your_username to the sambashare group

addgroup supersecret

usermod -aG supersecret your_username

usermod -aG sambashare your_username

---

Make the following changes to /share

![Screenshot](./assets/images/Pasted%20image%2020260228164506.png)

**Screenshot 4:** Showing the correct permissions on /share/your_username

### Knowledge Check

What command using octal sets your_username directory to drwxrwx---?

<details>
<summary>Answer</summary>

`chmod 770 your_username`

</details>

### Knowledge Check

What command changes your_username group ownership to supersecret?

<details>
<summary>Answer</summary>

`chgrp supersecret your_username`

</details>

---

Open /etc/samba/smb.conf and review some of the available settings.

At the bottom of the file, create a new share named [TUX-RW] with the following values:

comment = your_username  

path = /share/your_username  

read only = no  

browsable = yes  

valid users = @supersecret  

create mask = 0770  

directory mask = 0770

Duplicate this share information but name it TUX-RO (*You do not need to create a new subfolder,  

just set the share name as indicated and the set the “read only” flag to yes*)

After make sure to restart the samba service: **service smbd restart**

---

**Screenshot 5:** your two shares created from smb.conf

![Screenshot](./assets/images/file-5f3007b4a3c41.png)

---

Next try to connect. We will first try to map TUX-RW to the P drive.

![Screenshot](./assets/images/file-5f30087ae7183.png)

Set a password now for your_username that Samba can use.

![Screenshot](./assets/images/file-5f3008f39ced8.png)

SUCCESS!

![Screenshot](./assets/images/file-5f30095171fae.png)

---

**Screenshot 6:** Show the two connected shares

![Screenshot](./assets/images/file-5f300a5a0e591.png)

Map P to TUX-RW

Map Q to TUX-RO

---

**Screenshot 7:** Using the follow methods show that the shares have different write permissions.

![Screenshot](./assets/images/file-5f300b3986add.png)

[Prev: vsftpd](01_vsftpd.md) | [Home](README.md)
