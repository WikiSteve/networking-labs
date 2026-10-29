# Protect the Source

## Encrypt with your partner's public key

Quit the game. Archive your own modified project:

```bash
cd ~/game-release
tar -cf source.tar source
```

For Tar, `-c` creates an archive and `-f` names the output file. Use **`gpg --fingerprint`** to display your imported keys and their fingerprints. Encrypt to your partner's verified fingerprint, without spaces:

```bash
gpg --encrypt --recipient PARTNER_FINGERPRINT source.tar
```

`--encrypt` creates `source.tar.gpg`. `--recipient` selects the public key whose matching private key can decrypt it. Select **only your partner**, not yourself. If GPG asks whether to use an uncertified key, confirm it is the fingerprint you checked with your partner before proceeding.

Send the encrypted copy using your existing transfer method:

```bash
scp source.tar.gpg PARTNER_USER@PARTNER_IP:game-release/incoming/
```

Keep the unencrypted archive and working source on your own VM.

## Your partner decrypts; you decrypt theirs

On your own VM, open the archive received from your partner:

```bash
cd ~/game-release/incoming
gpg --output partner-source.tar --decrypt source.tar.gpg
tar -xf partner-source.tar
```

`--decrypt` uses your private key; enter its passphrase if prompted. `--output` saves the recovered archive. Tar's `-x` extracts it and `-f` names the archive.

Show the source change:

```bash
cd source
git diff
```

Git shows the edited line beside the original. You do not need to rebuild the game. Press **Q** if Git opens a scrolling view.

## **Screenshot 3: Partner Source Decrypted**

**Requirement:** Show your successful decryption command and output, followed by the recovered source line containing your partner's name.

## Can you decrypt the copy you sent?

Try opening your **own outgoing archive**, which you encrypted only to your partner:

```bash
cd ~/game-release
gpg --output check.tar --decrypt source.tar.gpg
```

Expect **No secret key**. You have your partner's public key, but they hold the private key needed to decrypt this copy. You still have your original plaintext source. If decryption succeeds, check whether you also selected your own key as a recipient.

## **Screenshot 4: Sender Cannot Decrypt the Partner's Copy**

**Requirement:** Show your attempt to decrypt the outgoing archive and the failure message `No secret key`.

Submit your four screenshots in the template. Remember: **sign with your private key; verify with the signer's public key. Encrypt to the recipient's public key; decrypt with the recipient's private key.**

---
[Prev](02_sign-and-share.md) | [Home](README.md)
