# vsftpd

Configuring vsftpd

*Very Secure FTP daemon*

NOTE: Make sure to clear your screen for every screenshot

Install the package using apt-get, the package name is vsftpd then enable it on system startup with **systemctl enable vsftpd.**

Before getting started make sure to backup the configuration in case you need to revert back

cp /etc/vsftpd.conf /etc/vsftpd.conf.original

## **Screenshot 1: Directory listing show the backup file including the date created**

---

Open the vsftpd.conf and uncomment the line that reads "write\_enable=YES".  Save and restart the vsftpd daemon.

![vsftpd.conf showing write_enable set to YES.](./assets/images/file-5f2f6cb4e1d86.png)

Restart the vsftpd service with **systemctl restart vsftpd** then verify ftp works from your host to the VM.

![Windows FTP session successfully logging in as steve and listing the home directory contents.](./assets/images/file-5f2f6de43f71f.png)

---

Using your FTP client of choice verify that this **regular user** has the ability to traverse, read and write files throughout the filesystem.  In this example I uploaded ReadMe.txt sitting on my Desktop.

![Windows FTP session uploading ReadMe.txt and browsing /tmp as the regular steve user.](./assets/images/file-5f2f70d315667.png)

---

Open the vsftpd.conf file

![vsftpd.conf excerpt with chroot_local_user set to YES.](./assets/images/Pasted%20image%2020260228162621.png)

### Reconnect

![Windows FTP login showing the writable-root-inside-chroot warning and the connection being closed.](./assets/images/Pasted%20image%2020260228162725.png)


---

What it is telling us, as a warning that we've enabled chroot which is something we would enable for a highly restrictive user that this particular account has *write access to their home directory*.

![Directory listing of /home showing the steve home directory still writable before permissions are tightened.](./assets/images/Pasted%20image%2020260228162859.png)
write removed
![chmod command removing write permissions from steve's home directory and a long listing confirming the new mode.](./assets/images/file-5f2f7421a8da1.png)

---

Success!

![Windows FTP login succeeding again after write permissions are removed from the home directory.](./assets/images/file-5f2f747355c16.png)

---

Try to leave your home directory.

![FTP session showing the chroot jail in effect, with cd / staying inside the jailed view and cd /tmp failing.](./assets/images/file-5f2f74edc9289.png)

---

Effectively what we've done is a common UNIX technique known as the [root jail](https://en.wikipedia.org/wiki/Chroot)

![Decorative black-and-white jail photo illustrating the chroot jail concept.](./assets/images/file-5f2f76ea23340.jpg)

There may be paying customers that should be able to write to their home directories, therefore you can add the allow\_writeable\_chroot=YES directive which will enforce both the root jail but also allow the user to add files to their home directory.

---

![vsftpd.conf excerpt with chroot_list_enable and chroot_list_file uncommented.](./assets/images/Pasted%20image%2020260228163913.png)

Using the adduser script create a user named testuser.  Create the file /etc/vsftpd.chroot\_list and add testuser to this file.

Once completed restart the ftp service.

---

## **Screenshot 2: Show both connections (steve user, testuser) and their different access abilities.**

![Side-by-side Windows FTP sessions showing steve blocked from /tmp while testuser can access and list it.](./assets/images/file-5f2f817b66c01.png)

What happens? Why does this occur?

---

**Enabling TLS for FTP**  

Create a new RSA key using openSSL

**openssl req -x509 -nodes -keyout /etc/ssl/private/vsSSharpe.key -out /etc/ssl/private/vsSSharpe.pem -days 365 -newkey rsa:4096**

![openssl req command generating a self-signed TLS certificate and private key for vsftpd.](./assets/images/file-5f2f8891aaec5.png)


---

Make the following changes to vsftpd.conf

![vsftpd.conf TLS settings showing the certificate path, key path, ssl_enable, and related protocol options.](./assets/images/file-5f2f8a75d1981.png)

Non-encrypted connections forbidden.

![Plain FTP login rejected with a message that non-anonymous sessions must use encryption.](./assets/images/file-5f2f8bb7f3177.png)

---

Download [Filezilla](https://filezilla-project.org)

![FileZilla Site Manager configured to require explicit FTP over TLS for the vsftpd server.](./assets/images/Pasted%20image%2020260228164115.png)

---

## **Screenshot 3: Certificate as displayed by FileZilla**

![FileZilla certificate dialog showing the unknown server certificate details for the FTP service.](./assets/images/file-5f2f8d1833d63.png)

---

So I see there is an FTP group but we didn't use it? True! We need to [enable it in PAM](https://serverfault.com/questions/931127/ftp-pam-setup-for-vsftpd) as a requirement

See Ubuntu's guide on vsftpd for more [configuration examples.](https://help.ubuntu.com/community/vsftpd)

[Home](README.md) | [Next: samba](02_samba.md)
