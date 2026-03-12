# Setup and Notes

## Setup

This lab will require cooperation with **at least one**, but preferably multiple students in your class.

This lab will require a Linux virtual machine, the distribution used in these examples is Ubuntu Server so if your distribution is different then these commands may differ.

In the original lab we used a public UNIX service called Freeshell; **however, that is not required.** If you wish to still get a Freeshell account you can follow the instructions on sdf.org and contact me and I’ll validate your account. **In conclusion, we are using the Linux virtual machines you create instead.**

The evaluation section of this lab differs from my original lab in the following ways:

### Evaluation

**[This lab](https://docs.google.com/document/d/1XMQCzzbFMqPhJXMAYu4_0xxaZYU9CHjJpM84P6oM6kQ)**

Will result in the creation and submission of 5 screenshots. You may work in groups of 2 or 3. Part marks will be awarded for solo work since **you must sign another student’s key.**

**[Original lab](https://docs.google.com/document/u/0/d/1OgBEiwsXZw1XZW_7OdftsErCP1zskaBA416ZGSg_FcI/edit)**

Consisted of only a quiz.

### Environment Check

- You must have routable internet access. You should be able to ping `google.com`.

- A basic understanding of how to get files to and from your Linux virtual machine.

- The ability to SSH into your virtual machine.

- The following commands must work:
  - **`gpg --version`** should display the installed GPG version.
  - **`git --version`** should display the installed Git version.

## Notes

### Available Keyservers

All good things must come to an end. The Mozilla keyserver suffered a certificate spamming attack and was permanently closed. As of July 2021, all the keyservers that were available in 2019 are down.

**Keyserver graveyard**

- [gpg.mozilla.org](http://gpg.mozilla.org): Mozilla’s SKS OpenPGP key server. [More information](https://github.com/mozilla/gpg.mozilla.org)
- [pgp.key-server.io](https://pgp.key-server.io/): Available through the web browser and command line.
- [pgp.mit.edu](http://pgp.mit.edu/): Usually only usable from the command line and can be extremely slow.

**A working keyserver**

- [https://keyserver.ubuntu.com/](https://keyserver.ubuntu.com/): Ubuntu’s keyserver works like a charm.

### Terms

- **HKP**: OpenPGP HTTP Keyserver Protocol, used to interact with a keyserver from the command line.
- **Keyserver plaque**: Old fossil keys that never go away and bogus keys. [More information](https://en.wikipedia.org/wiki/Key_server_(cryptographic))
- **Certification**: Signing another person’s public key.

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

- **`gpg --gen-key`**: Generate a key.
- **`gpg --import somekey.key`**: Import a key. It could be `.asc` or another extension, so use tools like `file` and `head` to determine what it is.
- **`gpg --list-keys`**: List installed keys.
- **`gpg --list-sigs`**: List signatures.
- **`gpg --keyserver pgp-server-address [--send-keys|recv-keys|search] keyID-or-email`**: Interact with the keyserver from the command line.

---

[Home](README.md) | [Next](02_walk-through-videos.md)
