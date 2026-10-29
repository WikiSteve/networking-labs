# Verify and Play

The **player** completes this page for Screenshot 2. The developer should also verify the release. Work on your own VM, using the publisher's address in the download commands.

## Download the public release

```bash
cd ~/game-release
wget http://PUBLISHER_IP:8000/student-game.deb
wget http://PUBLISHER_IP:8000/student-game.deb.sig
wget http://PUBLISHER_IP:8000/publisher-public.asc
```

Wget saves each download in the current directory. If you repeat a download, move the earlier copy out of this folder first; Wget may otherwise save the new file with a suffix such as `.1`. Verify the file you intend to install.

Import the publisher's public key and inspect its fingerprint:

```bash
gpg --import publisher-public.asc
gpg --fingerprint PUBLISHER_FINGERPRINT
```

Compare the full fingerprint with the publisher reading it from their own VM. Reuse the checked identity from the web-of-trust lab. A public key downloaded beside a game does not establish the publisher's identity on its own.

## Verify the installer

```bash
gpg --verify student-game.deb.sig student-game.deb
```

`--verify` checks the signature file against the installer named after it. Expect **Good signature** from your publisher. Check the signer against the key you just verified. An unexpected signer is a reason to stop even if the signature is mathematically valid.

GPG may also warn that the key is not certified with a trusted signature. That is a statement about your local identity/trust information. It is different from **BAD signature**. Resolve the identity using your fingerprint comparison; do not mark an unfamiliar key as ultimately trusted to hide a warning.

## Make a tampered copy

Keep the original installer. Copy it and append some text to the copy:

```bash
cp student-game.deb changed-game.deb
echo tampered >> changed-game.deb
gpg --verify student-game.deb.sig changed-game.deb
```

`>>` appends text to the file. The copy now has different bytes. Verification against the original signature must report **BAD signature**. Do not install this changed copy.

To put both results together for your screenshot, run:

```bash
gpg --verify student-game.deb.sig student-game.deb
gpg --verify student-game.deb.sig changed-game.deb
```

## **Screenshot 2: Original and Tampered Installer Verification**

**Requirement:** In one screenshot, show both verification commands, the publisher's identity, a Good signature for `student-game.deb`, and a BAD signature for `changed-game.deb`.

## Install the verified original and play

After confirming the original signature and publisher's fingerprint:

```bash
sudo apt install ./student-game.deb
student-game
```

The `./` tells Apt to install the local package file. Apt installs its required libraries if needed. Run the game as your normal user and look for the publisher's release label. Test the changes described by your partner.

A signature shows that the file matches what the signing key signed. It does not prove the program is harmless or that the signed binary was built from a particular source archive.

When you finish this round, remove the installed game:

```bash
sudo apt remove student-game
```

This lets the next group's version use the same package name without mixing releases. Your downloaded release files remain in the workspace.

---
[Prev](03_package-protect-and-publish.md) | [Home](README.md) | [Next](05_decrypt-and-rebuild.md)

