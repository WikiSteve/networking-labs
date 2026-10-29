# Release Your Game with GPG

> **Before you start:** Download the [Game Release Submission Template](<./assets/Game Release SUBMISSION TEMPLATE.pptx>). Add each required screenshot directly into this file as you complete the lab, then submit the completed template for grading.

## Goal

Build your own edition of a terminal game. Publish an installer that another student can verify, and encrypt your modified source so a trusted developer can work on it.

Use **Snake Duel** by default. **Tetris** and **Battleship** are alternatives. All three run in a terminal without a graphical desktop.

This follows [Simple Web of Trust](../060-simple-web-of-trust/README.md). Reuse your keys and the fingerprints you checked with their owners. A certification on a public key helps establish identity; it does not give that person access to encrypted files.

## What you need

- A Debian or Ubuntu Linux VM, internet access, and a terminal
- Your working GPG key pair from the web-of-trust lab
- Three students with separate accounts and private keys
- Working SSH/SCP between group members and VM network connectivity for the class download server
- Matching Linux distribution versions and CPU architectures for the publisher and player

**You may choose Windows.** The walkthrough supports Linux. If you choose Windows, find suitable build and installer instructions and arrange a compatible system for your partner to test. The same four screenshot requirements apply; use your actual Windows installer filenames in place of the `.deb` filenames. WSL follows the Linux route and produces a Linux game, not a native Windows executable. A detached GPG signature is checked with GPG; it does not provide Windows Authenticode signing.

## Group roles

| Role | Your job |
| --- | --- |
| Publisher | Modify and compile the game, build and sign its installer, and encrypt the source to the developer |
| Trusted developer | Verify the release, decrypt the source using your own private key, and rebuild the game |
| Player | Verify and play the public release, then demonstrate that you cannot decrypt the source |

Choose one release for your group's submission. Use that release for all four screenshots. Rotate roles for practice so everyone uses their own key to sign and decrypt. Keep each round in its own folder and remove the previous round's installed `student-game` package before installing the next one.

## Four screenshots

- Screenshot 1: Modified Game Running
- Screenshot 2: Original and Tampered Installer Verification
- Screenshot 3: Trusted Developer Decrypts and Rebuilds
- Screenshot 4: Player Cannot Decrypt the Source

Submit one group PowerPoint with everyone's classroom name and role on the cover. Add the screenshots to the matching slides. Keep the release files and source available until grading is complete.

## Pages

- [01 Setup and Keys](01_setup-and-keys.md)
- [02 Build and Modify Your Game](02_build-and-modify-your-game.md)
- [03 Package, Protect, and Publish](03_package-protect-and-publish.md)
- [04 Verify and Play](04_verify-and-play.md)
- [05 Decrypt and Rebuild](05_decrypt-and-rebuild.md)

