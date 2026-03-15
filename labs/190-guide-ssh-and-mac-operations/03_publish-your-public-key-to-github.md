# Publish Your Public Key to GitHub

GitHub can act as a convenient place to store your public SSH key so Linux systems can import it later.

## Add the key to your account

1. Sign in to GitHub.
2. Open **Settings**.
3. Go to **SSH and GPG keys**.

![GitHub account settings page with the SSH and GPG keys section visible](assets/images/file-609b29a12e93c.png)

4. Click **New SSH key**.
5. Give the key a descriptive title, such as `windows-laptop` or `lab-pc`.
6. Paste in the public key text from PuTTYgen.
7. Save the key.

## Important security note

The public key can be uploaded to GitHub safely. The private key is the sensitive part and must not be shared.

## Keep your naming simple

Using short, clear titles makes later imports easier to recognize, especially if you keep more than one key in GitHub.

---
[Prev](02_generate-ssh-keys-with-puttygen.md) | [Home](README.md) | [Next](04_install-your-key-on-both-linux-systems.md)
