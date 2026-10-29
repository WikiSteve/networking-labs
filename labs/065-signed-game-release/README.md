# Release Your Game with GPG

> **Before you start:** Download the [Game Release Submission Template](<./assets/Game Release SUBMISSION TEMPLATE.pptx>). Add each required screenshot directly into this file as you complete the lab, then submit the completed template for grading.

## Goal

Modify and compile a terminal game. Sign its installer so your partner can verify it, then encrypt the source so only your partner can decrypt that copy.

**Target: 30–40 minutes**, with tools installed and the [Web of Trust](../060-simple-web-of-trust/README.md) keys and file transfers already working.

Work in **pairs**. Both of you build your own game and act as the other's trusted developer. Submit your own four screenshots, with both names on the cover.

## Before class

- Use your lab VM with your own valid private key and your partner's imported, fingerprint-checked public key.
- Use compatible Debian/Ubuntu VMs with the same architecture and distribution version.
- Have a working file-transfer method from the previous lab.
- Download the [installer helper](assets/build-installer.sh) using **Download raw file** on GitHub. It makes the installer for you.

<details>
<summary>Install the build tools if needed</summary>

```bash
sudo apt update
sudo apt install git golang-go
```

For the C/ncurses choices, install these instead:

```bash
sudo apt install git build-essential libncurses-dev pkg-config
```

Go downloads its code dependencies during the first build. The C tools supply the compiler, Make and ncurses headers. `pkg-config` lets Make find ncurses.

</details>

**Windows is your choice:** prepare a working compiler and installer method beforehand, and use a compatible partner system. Substitute your installer filenames for the Linux examples. WSL follows the Linux route.

## Complete the practical

- [01 Build Your Game](01_build-your-game.md) — about 10 minutes
- [02 Sign and Share](02_sign-and-share.md) — about 10 minutes
- [03 Protect the Source](03_protect-the-source.md) — about 10 minutes

Allow the remaining time for screenshots and playing your partner's game. These are planning estimates.
