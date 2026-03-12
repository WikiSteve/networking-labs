# Generate Your Key

Create your **2048 bit RSA** GPG key

![Terminal running gpg --full-generate-key and prompting for RSA key type, a 2048-bit key size, and a 5-week expiry.](assets/images/image25.png)

To prevent [keyserver plaque](https://en.wikipedia.org/wiki/Key_server_(cryptographic)#Problems_with_keyservers), make sure the key **expires in 5 weeks**.

![GUI passphrase dialog asking for a passphrase to protect the new GPG key.](assets/images/image19.png)

Enter a [passphrase](https://en.wikipedia.org/wiki/Passphrase) to protect the private key

![GnuPG prompt confirming the new user ID for Steve Sharpe with email and comment fields.](assets/images/image6.png)

Reminder of the importance of randomness in cryptography.

![GnuPG message explaining it needs random bytes and suggesting keyboard, mouse, or disk activity to generate entropy.](assets/images/image2.png)

Summary

![Terminal output showing Steve Sharpe's new GPG key created, marked ultimately trusted, and a revocation certificate stored.](assets/images/image28.png)

List the keys

![Terminal output from gpg --list-keys --fingerprint showing Steve Sharpe's 2021 key fingerprint and ultimate trust.](assets/images/image9.png)

Before proceeding, it’s vital that the expiry date is only 5 weeks ahead.

NOTE THE BELOW SCREENSHOT FROM 2019

![2019 terminal output from gpg --list-keys showing the older shorter key ID format for Steve Sharpe's temporary key.](assets/images/image16.png)

Note the output of the fingerprint in 2019 was shorter than in 2021. [See this post about why the change.](https://unix.stackexchange.com/questions/613839/help-understanding-gpg-list-keys-output)

## Uploading Your Key to the Keyserver

Upload to the [Ubuntu keyserver](https://keyserver.ubuntu.com/). Note the term [hkp](https://en.wikipedia.org/wiki/Key_server_(cryptographic)).

![Terminal running gpg --keyserver keyserver.ubuntu.com --send-keys and reporting Steve Sharpe's key sent to the Ubuntu keyserver.](assets/images/image18.png)

Try and find your key. There are various ways to do this. [I searched for my name.](https://keyserver.ubuntu.com/pks/lookup?search=steve+sharpe&fingerprint=on&op=index)

![Ubuntu keyserver web search results showing Steve Sharpe's uploaded public key and self-signatures.](assets/images/image20.png)

## **Screenshot 1: Show the key from the keyserver**

---

[Prev](02_walk-through-videos.md) | [Home](README.md) | [Next](04_signing-other-keys.md)
