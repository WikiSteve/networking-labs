# Decrypt and Rebuild

The trusted developer and player download the **same encrypted archive**. Their different private keys determine whether they can open it.

## Trusted developer: recover the source

On the **developer's VM**, download the encrypted source into your workspace:

```bash
cd ~/game-release
wget http://PUBLISHER_IP:8000/source.tar.gpg
gpg --output source.tar --decrypt source.tar.gpg
```

`--decrypt` uses the matching private key in your keyring. Enter its passphrase if prompted. `--output` saves the recovered bytes as `source.tar` instead of printing them in the terminal. Successful decryption identifies your recipient key and finishes without a decryption error.

Create a new folder for the recovered project and unpack it there:

```bash
mkdir recovered
cd recovered
tar -xf ../source.tar
cat CHANGES.txt
```

`../source.tar` refers to the archive in the parent folder. Read the release label, source changes, and build instructions. Inspect the actual edited source files and confirm that they match the notes.

For Snake Duel, rebuild from inside `recovered`:

```bash
cd nbsdgames/src
make -B snakeduel
```

`-B` forces Make to compile again, even if the archive contains an already-built executable. You should see a compiler command rather than only an "up to date" message.

For Battleship, use **`make -B battleship`** in the same directory. For Tetris, enter **`cd tetris`** from `recovered`, then run **`make -B`**.

## **Screenshot 3: Trusted Developer Decrypts and Rebuilds**

**Requirement:** In one screenshot, show successful source decryption, the release label in `CHANGES.txt`, and a fresh compiler command completing without errors on the developer's VM.

Keep the decryption output visible above the archive extraction and build commands. Enlarge your terminal if needed. Show actual output, not a typed claim that decryption worked.

Run the rebuilt game with **`./snakeduel`**, **`./battleship`**, or **`./tetris`**, as appropriate. Confirm that the release label and changes survived the handoff. No additional screenshot is required.

## Player: try the same archive

On the **player's VM**, download the encrypted source and the developer's public key:

```bash
cd ~/game-release
wget http://PUBLISHER_IP:8000/source.tar.gpg
wget http://PUBLISHER_IP:8000/developer-public.asc
gpg --import developer-public.asc
```

Check the developer's full fingerprint with its owner, then display the public key and attempt decryption:

```bash
gpg --fingerprint DEVELOPER_FINGERPRINT
gpg --output player-source.tar --decrypt source.tar.gpg
```

Expect **decryption failed: No secret key**. The developer's public key is present, but the matching private key belongs on the developer's VM. The player can verify the public installer and play it without having access to the modified source package.

If decryption succeeds, investigate before submitting: did the publisher encrypt to the player's key, add extra recipients, or did someone copy a private key between accounts? Do not remove your existing keys to manufacture a failure. Use the agreed roles and correct recipient.

## **Screenshot 4: Player Cannot Decrypt the Source**

**Requirement:** In one screenshot, show the developer's public key fingerprint, the player's decryption command, and the failure message `No secret key`.

## Finish your submission

Use exactly four screenshots, one per numbered slide. Identify all group members and their roles on the cover. Under Screenshot 1, explain the two source changes. Add a short answer beneath each remaining screenshot:

- Screenshot 2: Whose private key created the signature, and whose public key verified it?
- Screenshot 3: Whose public key protected the archive, and whose private key opened it?
- Screenshot 4: Why did importing the developer's public key fail to grant source access?

Keep the signed installer, its signature, and the encrypted source archive available until grading is complete. Stop the publisher's download server with **Ctrl+C** when your partners have finished. Rotate roles in a new workspace to practise the other key operations; submit the four captures from your selected release only.

---
[Prev](04_verify-and-play.md) | [Home](README.md)

