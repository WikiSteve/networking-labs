# Configure PuTTY to Use Your Private Key

PuTTY can store connection settings so you do not need to rebuild the same SSH configuration each time.

## Optional: adjust the display font

If the default text is too small, change it before saving the session.

![PuTTY configuration window with the Appearance page open and the font-selection dialog visible](assets/images/file-609b2b9d54df8.png)

## Set the login username

Under **Connection > Data**, enter the username you use on the Linux system in **Auto-login username**.

## Point PuTTY to the private key

Open **Connection > SSH > Auth** and browse to the `.ppk` file you created in PuTTYgen.

![PuTTY configuration window on the SSH Auth page, showing the private-key browse field](assets/images/file-609b2c5481add.png)

## Save a reusable session

Go back to the **Session** page, enter a clear saved-session name, and click **Save**.

Suggested examples:

- `ubuntu-key`
- `centos-key`

![PuTTY configuration window on the Session page with a saved-session name entered](assets/images/file-609b2c7fa30bd.png)

If you want separate profiles for different systems, save one profile per host.

## Connect and test

Load the saved session, enter the server IP address if needed, and connect.

![PuTTY configuration beside a terminal window showing a successful SSH login using the saved session](assets/images/file-609b2ca655809.png)

If everything is configured correctly, PuTTY should:

- use the saved username
- present the `.ppk` key automatically
- avoid a normal password prompt unless your key itself has a passphrase

---
[Prev](04_install-your-key-on-both-linux-systems.md) | [Home](README.md) | [Next](06_mac-file-and-directory-basics.md)
