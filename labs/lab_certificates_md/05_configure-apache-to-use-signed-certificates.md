# Configure Apache to use signed certificates

We will be configuring Apache site files in `/etc/apache2/sites-available`.

Create an SSL site by copying `000-default.conf` to `000-default-ssl.conf`:

```bash
cp 000-default.conf 000-default-ssl.conf
```

Open `000-default-ssl.conf` in `vi`.

In the first line, change port `80` to `443`.

After `DocumentRoot`, add:

```apache
SSLEngine on
SSLCertificateFile /etc/ssl/certs/your_username-apache.your_username.local
SSLCertificateKeyFile /etc/ssl/private/your_username-apache.your_username.local.key
```

## **Screenshot 6: Show changes to 000-default-ssl.conf**

![000-default-ssl.conf showing the VirtualHost on port 443 with SSLEngine, certificate, and key directives added.](./assets/images/file-5f323d42a2bc7_slide2_flat.png)

Edit the Apache config file:

`/etc/apache2/apache2.conf`

Search for `Global configuration` and add:

```apache
ServerName localhost
```

![apache2.conf edited to add ServerName localhost under the Global configuration section.](./assets/images/file-5f3233f6524ee_slide3_flat.png)

Enable the new SSL site:

```bash
a2ensite 000-default-ssl.conf
```

![a2ensite enabling 000-default-ssl.conf and reporting that Apache should be reloaded.](./assets/images/file-5f32347bc8931_slide4_flat.png)

```bash
a2enmod ssl
```

![a2enmod ssl enabling the Apache SSL module and its dependencies.](./assets/images/file-5f3234c402a88_slide4_flat.png)

Restart Apache:

```bash
systemctl restart apache2
```

![systemctl restart apache2 completing without errors after enabling SSL.](./assets/images/file-5f32369fedc9c_slide5_flat.png)

Double-check Apache status:

```bash
systemctl status apache2
```

![systemctl status apache2 showing Apache running after the SSL configuration changes.](./assets/images/file-5f323733a0f39_slide5_flat.png)

You should now be able to browse to the HTTPS version of your default Apache page on your LAMP server, but there is still a certificate error in Windows.

## **Screenshot 7: Firefox with the certificate error going to the default page.**

![Firefox displaying a Potential Security Risk warning when visiting the HTTPS site before trusting the certificate authority.](./assets/images/file-5f323f52e3e3d.png)

Windows needs to trust the certificate authority. The certificate file is `/etc/ssl/certs/cacert.pem` on `your_username-CA`.

There are multiple ways to transfer the file, but we will use [FileZilla](https://filezilla-project.org/). Select `SFTP - SSH File Transfer Protocol`.
![FileZilla Site Manager configured to connect to the CA host with SFTP.](./assets/images/Pasted%20image%2020260304105309.png)

Accept the server fingerprint.

![FileZilla host key dialog asking whether to trust the SSH fingerprint of the CA server.](./assets/images/file-5f3241a9b0ad3_slide8_flat.png)

Remote server is on the right, your local system is on the left. In this example, the file is copied to the desktop. Double-click the file in the bottom-right panel to begin transfer.

![FileZilla connected to the CA server over SFTP with the remote file list visible.](./assets/images/file-5f32423406b41.png)

Step 1:

![Firefox toolbar menu button highlighted as the first step toward opening Preferences.](./assets/images/Pasted%20image%2020260302121139.png)

![Firefox application menu open with Preferences highlighted.](./assets/images/Pasted%20image%2020260302121227.png)

![Firefox Preferences open to Privacy & Security as the third step toward managing certificates.](./assets/images/file-5f32448368e6e_slide12_flat.png)

Scroll to the bottom and select **View Certificates**.

![Firefox certificate settings area with the View Certificates button highlighted.](./assets/images/file-5f3244d9288d2_slide13_flat.png)



![Firefox Certificate Manager on the Authorities tab with the Import button highlighted.](./assets/images/file-5f32453baeacb_slide14_flat.png)

![File picker dialog selecting cacert.pem for import into Firefox.](./assets/images/file-5f3245f61c67b_slide15_flat.png)

Select both trust options.

![Firefox Downloading Certificate dialog asking which trust purposes to enable for the imported CA.](./assets/images/file-5f32464e3b227_slide16_flat.png)



## **Screenshot 8: authorities showing your imported certificate**

![Firefox Certificate Manager Authorities tab showing the imported local certificate authority entry.](./assets/images/Pasted%20image%2020260302121500.png)

**Put an entry in the hosts file**

Because certificates prove domain ownership, we need to map `your_username-LAMP` to an IP address. We do not need a full DNS infrastructure for this lab; use the Windows hosts file.

Open `c:/windows/system32/drivers/etc/hosts` with Notepad **as Administrator**.

![Windows start menu search for Notepad with Run as administrator selected before editing the hosts file.](./assets/images/file-5f32499c4035d.png)

![Windows Explorer open to the System32 drivers etc folder that contains the hosts file.](./assets/images/file-5f324a43bbb4f_slide18_flat.png)

Add these two entries:

```text
192.168.90.10 www.your_username.local
192.168.90.10 your_username.local
```

## **Screenshot 9: show the contents of c:/windows/system32/drivers/etc/hosts**

![Windows Notepad displaying the hosts file with entries for www.your_username.local and your_username.local.](./assets/images/file-625f6183be5db.png)

## **Screenshot 10: Firefox with a closed padlock and no errors**

![Firefox showing the Apache default page over HTTPS with a closed padlock and no certificate errors.](./assets/images/file-5f324ca919a07_slide20_flat.png)


Try without the www and the certificate error returns because the common name was only for www.your-name.local and not a wildcard such as *.your-name.local.
![Firefox warning page showing a certificate error when visiting the site without the matching trusted hostname.](./assets/images/Pasted%20image%2020260304105735.png)

https://www.youtube.com/watch?v=Pzv_7Bx1C-Y

[Prev](04_certificate-work.md) | [Home](README.md) | [Next](06_troubleshooting-openssl.md)
