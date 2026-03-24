# Setup and Notes

## Setup

This lab will require cooperation with **at least one**, but preferably multiple students in your class.

This lab uses a Linux virtual machine. The examples were created on Ubuntu Server, so prompts or package versions can differ slightly on another distribution.

You may work in groups of 2 or 3, but the signing portion still requires a real partner because the point of the lab is to build a small web of trust instead of only making a self-signed key.

### Environment Check

- You must have routable internet access. You should be able to ping `google.com`.

- A basic understanding of how to get files to and from your Linux virtual machine.

- The ability to SSH into your virtual machine.

- The following commands must work:
  - **`gpg --version`** should display the installed GPG version.

## Notes

### Available Keyservers

All good things must come to an end. The Mozilla keyserver suffered a certificate spamming attack and was permanently closed. As of July 2021, all the keyservers that were available in 2019 are down.

**Keyserver graveyard**

- [gpg.mozilla.org](http://gpg.mozilla.org): Mozilla’s SKS OpenPGP key server. [More information](https://github.com/mozilla/gpg.mozilla.org)
- [pgp.key-server.io](https://pgp.key-server.io/): Available through the web browser and command line.
- [pgp.mit.edu](http://pgp.mit.edu/): Usually only usable from the command line and can be extremely slow.

**A working keyserver**

- [https://keyserver.ubuntu.com/](https://keyserver.ubuntu.com/): Ubuntu’s keyserver works like a charm.

Keyserver results can take a few minutes to update after you upload a key or a new signature. If a search result does not appear immediately, wait a bit and try again.

### Terms

- **HKP**: OpenPGP HTTP Keyserver Protocol, used to interact with a keyserver from the command line.
- **Keyserver plaque**: Old fossil keys that never go away and bogus keys. [More information](https://en.wikipedia.org/wiki/Key_server_(cryptographic))
- **Certification**: Signing another person’s public key.
- **Fingerprint verification**: Reading a key fingerprint from a trusted out-of-band source such as your partner’s screen, voice, or video call before signing the key.

### Commands

#### General Linux Commands

- **`whoami`**: Display who is currently logged in.
- **`cat`**: Display the contents of a file on standard output.
- **`head`**: Show the first ten lines of an ASCII file.
- **`tail`**: Show the last ten lines of an ASCII file.
- **`xxd -b`**: Display binary files in a bit-oriented format.
- **`file`**: Make a best guess as to what a file contains.
- **`less`**: Scroll through and search a document.
- **`>`**: Redirect standard output to a file.

#### GPG-Specific Commands

Very short list of commands to get you started.

- **`gpg --full-generate-key`**: Generate a key with explicit choices for key type, size, and expiry.
- **`gpg --import somekey.key`**: Import a key. It could be `.asc` or another extension, so use tools like `file` and `head` to determine what it is.
- **`gpg --list-keys --fingerprint`**: List installed keys and show their fingerprints.
- **`gpg --list-sigs`**: List signatures on a key.
- **`gpg --keyserver hkps://keyserver.ubuntu.com --send-keys KEYID`**: Upload a key to the Ubuntu keyserver.
- **`gpg --keyserver hkps://keyserver.ubuntu.com --search-keys email@example.com`**: Search the keyserver from the command line.
- **`gpg --keyserver hkps://keyserver.ubuntu.com --recv-keys KEYID`**: Receive a key by its key ID or fingerprint.

> [!IMPORTANT]
> Before you sign another student’s key, verify that key’s fingerprint out of band. Do not sign a key just because the name or email looks right in a keyserver search.

---

[Home](README.md) | [Next](02_walk-through-videos.md)
