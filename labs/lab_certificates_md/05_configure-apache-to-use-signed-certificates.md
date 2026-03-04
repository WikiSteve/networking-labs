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

![Screenshot](./assets/images/file-5f323d42a2bc7_slide2_flat.png)

Edit the Apache config file:

`/etc/apache2/apache2.conf`

Search for `Global configuration` and add:

```apache
ServerName localhost
```

![Screenshot](./assets/images/file-5f3233f6524ee_slide3_flat.png)

Enable the new SSL site:

```bash
a2ensite 000-default-ssl.conf
```

![Screenshot](./assets/images/file-5f32347bc8931_slide4_flat.png)

**a2enmod ssl**
![Screenshot](./assets/images/file-5f3234c402a88_slide4_flat.png)

Restart Apache:

```bash
systemctl restart apache2
```

![Screenshot](./assets/images/file-5f32369fedc9c_slide5_flat.png)

Double-check Apache status:

```bash
systemctl status apache2
```

![Screenshot](./assets/images/file-5f323733a0f39_slide5_flat.png)

You should now be able to browse to the HTTPS version of your default Apache page on your LAMP server, but there is still a certificate error in Windows.

## **Screenshot 7: Firefox with the certificate error going to the default page.**

![Screenshot](./assets/images/file-5f323f52e3e3d.png)

Windows needs to trust the certificate authority. The certificate file is `/etc/ssl/certs/cacert.pem` on `your_username-CA`.

There are multiple ways to transfer the file, but we will use [FileZilla](https://filezilla-project.org/). Select `SFTP - SSH File Transfer Protocol`.
![[Pasted image 20260304105309.png]]

Accept the server fingerprint.

![Screenshot](./assets/images/file-5f3241a9b0ad3_slide8_flat.png)

Remote server is on the right, your local system is on the left. In this example, the file is copied to the desktop. Double-click the file in the bottom-right panel to begin transfer.

![Screenshot](./assets/images/file-5f32423406b41.png)

Step 1:

![Screenshot](<./assets/images/Pasted image 20260302121139.png>)

![Screenshot](<./assets/images/Pasted image 20260302121227.png>)

![Screenshot|582](./assets/images/file-5f32448368e6e_slide12_flat.png)

Scroll to the bottom and select **View Certificates**.

![Screenshot](./assets/images/file-5f3244d9288d2_slide13_flat.png)



![Screenshot](./assets/images/file-5f32453baeacb_slide14_flat.png)

![Screenshot|465](./assets/images/file-5f3245f61c67b_slide15_flat.png)

Select both trust options.

![Screenshot](./assets/images/file-5f32464e3b227_slide16_flat.png)



## **Screenshot 8: authorities showing your imported certificate**

![Screenshot](<./assets/images/Pasted image 20260302121500.png>)

**Put an entry in the hosts file**

Because certificates prove domain ownership, we need to map `your_username-LAMP` to an IP address. We do not need a full DNS infrastructure for this lab; use the Windows hosts file.

Open `c:/windows/system32/drivers/etc/hosts` with Notepad **as Administrator**.

![Screenshot](./assets/images/file-5f32499c4035d.png)

![Screenshot](./assets/images/file-5f324a43bbb4f_slide18_flat.png)

Add these two entries:

```text
192.168.90.10 www.your_username.local
192.168.90.10 your_username.local
```

## **Screenshot 9: show the contents of c:/windows/system32/drivers/etc/hosts**

![Screenshot](./assets/images/file-625f6183be5db.png)

## **Screenshot 10: Firefox with a closed padlock and no errors**

![Screenshot](./assets/images/file-5f324ca919a07_slide20_flat.png)


Try without the www and the certificate error returns because the common name was only for www.your-name.local and not a wildcard such as *.your-name.local.
![[Pasted image 20260304105735.png]]

https://www.youtube.com/watch?v=Pzv_7Bx1C-Y

[Prev](04_certificate-work.md) | [Home](README.md) | [Next](06_troubleshooting-openssl.md)
