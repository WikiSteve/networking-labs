# Setup and Keys

## Prepare your VM

Work on your own VM using your own account. Install the tools:

```bash
sudo apt update
sudo apt install git build-essential libncurses-dev pkg-config gnupg python3 wget nano
```

`build-essential` supplies the C compiler and Make. `libncurses-dev` supplies the terminal drawing library's development files, and `pkg-config` lets the build find them. GnuPG handles the keys, Python serves the release files, and Wget downloads them.

Create a workspace on each VM:

```bash
mkdir ~/game-release
cd ~/game-release
```

The `~` means your home directory. Use a new folder for a later round rather than mixing two publishers' files.

## Confirm your existing key

List your private keys and their fingerprints:

```bash
gpg --list-secret-keys --fingerprint
```

`--list-secret-keys` lists the private keys available to your account without displaying their secret material. `--fingerprint` displays their full fingerprints. Check your classroom identity, expiry date, and encryption subkey. The RSA-and-RSA keys from the previous lab support signing and encryption.

If your key has expired or is missing, return to [Generate Your Key](../060-simple-web-of-trust/03_generate-your-key.md) before continuing. Recheck any replacement key with your partners.

In the commands below, replace capitalised placeholders with your group's actual details. Enter a full primary fingerprint **without spaces** wherever a command asks for a fingerprint. Do not type the placeholder itself.

## Exchange the developer's public key

On the **developer's VM**, export your public key:

```bash
gpg --armor --export YOUR_FINGERPRINT > developer-public.asc
```

`--export` exports the public key selected by your fingerprint. `--armor` writes it as text. The `>` saves that text into the named file. Your private key stays on your VM.

Send the public key to the publisher:

```bash
scp developer-public.asc PUBLISHER_USER@PUBLISHER_IP:game-release/
```

SCP copies the file over SSH. Replace `PUBLISHER_USER` with the publisher's Linux username and `PUBLISHER_IP` with their VM's address. The folder after the colon is inside their home directory. The publisher must have created it first and agreed to the transfer.

On the **publisher's VM**, import and inspect the key:

```bash
gpg --import developer-public.asc
gpg --fingerprint DEVELOPER_FINGERPRINT
```

The developer reads their full fingerprint from their own terminal. Compare every character face to face or over your call. Confirm whose key you are using before encrypting anything.

Export the publisher's public key on the **publisher's VM**:

```bash
gpg --armor --export YOUR_FINGERPRINT > publisher-public.asc
```

The developer and player will download this public key with the game and compare its fingerprint with the publisher directly.

## Predict which key you need

| Task | Key used |
| --- | --- |
| Sign your installer | Publisher's private signing key |
| Verify the installer | Publisher's public key |
| Encrypt the source for the developer | Developer's public encryption key |
| Decrypt the source | Developer's private encryption key |

Keep private keys and their passphrases on their owners' VMs. Public keys may be shared with everyone. Knowing a public key, or certifying it, does not give you its private key.

---
[Home](README.md) | [Next](02_build-and-modify-your-game.md)

