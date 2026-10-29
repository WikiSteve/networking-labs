# Sign and Share

Quit the game. Both partners complete these steps for their own release.

## Make the installer

Return to your project folder:

```bash
cd ~/game-release/source
```

Run **one** command for your game:

| Game | Command |
| --- | --- |
| Go Tetris | **`bash ../build-installer.sh go-tetris`** |
| Snake Duel | **`bash ../build-installer.sh src/snakeduel`** |
| Battleship | **`bash ../build-installer.sh src/battleship`** |

The supplied helper packages your executable and licence as `student-game.deb` in the parent folder. `../` means the parent folder. You do not need to edit package metadata.

## Sign with your private key

```bash
cd ~/game-release
gpg --detach-sign student-game.deb
```

GPG uses your own private signing key. `--detach-sign` creates `student-game.deb.sig`. Enter your private-key passphrase if asked. The installer remains unencrypted.

Share **both files** using your existing transfer method. Put received files in `incoming`. For SCP:

```bash
scp student-game.deb student-game.deb.sig PARTNER_USER@PARTNER_IP:game-release/incoming/
```

Replace the username and IP with your partner's login details. Both partners must have created `incoming` first. The installer and signature may be shared with anyone; your private key stays with you.

## Verify with your partner's public key

```bash
cd ~/game-release/incoming
gpg --verify student-game.deb.sig student-game.deb
```

`--verify` checks the signature against the named installer. Expect **Good signature** from the partner whose public-key fingerprint you checked previously. Check the signer, not just the word “Good”.

Make a changed copy and check it against the same signature:

```bash
cp student-game.deb changed-game.deb
echo changed >> changed-game.deb
gpg --verify student-game.deb.sig changed-game.deb
```

`>>` appends text, changing the file's bytes. Expect **BAD signature**.

## **Screenshot 2: Original and Tampered Installer Verification**

**Requirement:** Show both verification commands, your partner's identity, a Good signature for the original, and a BAD signature for the changed copy.

Install only the verified original:

```bash
sudo apt install ./student-game.deb
student-game
```

The `./` tells Apt to use the local installer. Play your partner's edition. A valid signature establishes the signing key and unchanged bytes; it does not prove software is harmless.

---
[Prev](01_build-your-game.md) | [Home](README.md) | [Next](03_protect-the-source.md)
