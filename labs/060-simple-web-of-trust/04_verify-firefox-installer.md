# Verify Mozilla Firefox Installer

## Download Required Files

Download two files from Mozilla’s mirror:

- [Firefox 99.0 archive](https://ftp.mozilla.org/pub/firefox/releases/99.0/linux-i686/en-CA/firefox-99.0.tar.bz2)
- [Firefox 99.0 signature file](https://ftp.mozilla.org/pub/firefox/releases/99.0/linux-i686/en-CA/firefox-99.0.tar.bz2.asc)

In a directory of your choice, download both files with **`wget`**.

![Terminal creating a Firefox download directory and using wget to download firefox-99.0.tar.bz2 from Mozilla with progress output.](assets/images/image5.png)

## Verify the Files Are Authentic

The `.asc` file is a signature for the Firefox archive.

![Terminal showing the start of firefox-99.0.tar.bz2.asc, including the BEGIN PGP SIGNATURE block.](assets/images/image15.png)

Let's try to verify that the file really is from Mozilla or one of its developers.

![First gpg --verify attempt on the Firefox archive, failing with Can't check signature: No public key.](assets/images/image3.png)

Well, it is in fact a signature, but we’re missing Mozilla’s public key. They’ve given us the keyID above as 4360FE2109C49763186F8E21EBE41E90F6F12F6D.

Let’s search for this key and see if we can find it.

![Terminal searching the Ubuntu keyserver for Mozilla's signing key and importing Mozilla Software Releases <release@mozilla.com>.](assets/images/image30.png)

Try the verification again

![Second gpg --verify attempt showing a good Mozilla signature plus warnings that the key is not yet trusted, with primary and subkey fingerprints.](assets/images/image31.png)

Verification was successful. However, because we do not have a [web-of-trust path](https://serverfault.com/questions/569911/how-to-verify-an-imported-gpg-key) to Mozilla’s key, GnuPG may still report trust warnings even when the signature itself is valid.

You’ll see we don’t trust this key at all.

![Interactive gpg --edit-key view of Mozilla's key showing trust undefined, validity unknown, and the main key plus subkey IDs.](assets/images/image38.png)

> [!WARNING]
> In a real workflow, verify the key fingerprint from an official Mozilla source. Do not mark Mozilla’s key as ultimately trusted, because `ultimate` trust is reserved for keys you control.

For this lab, stop after confirming the fingerprint and the good signature. A trust warning can still appear because you have not established trust through your personal web of trust, and that is expected.

Rerun the verification and confirm that the signature is valid. A trust warning may still appear, but that does not invalidate the good signature.

![Verification after a trustdb update showing a good signature from Mozilla Software Releases and the key marked ultimate in the original workflow.](assets/images/image32.png)

## **Screenshot 5: Show a successful verification**

---

[Prev](03_signing-other-keys.md) | [Home](README.md)
