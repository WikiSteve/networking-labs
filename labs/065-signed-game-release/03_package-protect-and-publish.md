# Package, Protect, and Publish

The **publisher** completes this page. Your installer will be available to everyone. Your modified source archive will be encrypted for the trusted developer.

## Build a Linux installer

Download the [package folder template](assets/game-package.tar) and copy it into **`~/game-release`** on your VM. This small archive contains the folders and package description needed for a Debian installer. It contains no game executable.

Unpack it:

```bash
cd ~/game-release
tar -xf game-package.tar
```

For Tar, `-x` means extract and `-f` names the archive file. You now have a `package` folder.

Copy **your compiled game** and its licence into that folder. For Snake Duel:

```bash
cp nbsdgames/src/snakeduel package/usr/bin/student-game
cp nbsdgames/LICENSE package/usr/share/doc/student-game/copyright
```

For Battleship, use these instead:

```bash
cp nbsdgames/src/battleship package/usr/bin/student-game
cp nbsdgames/LICENSE package/usr/share/doc/student-game/copyright
```

For Tetris, use these instead:

```bash
cp tetris/tetris package/usr/bin/student-game
cp tetris/LICENSE package/usr/share/doc/student-game/copyright
```

All three routes install the command **`student-game`**. `copyright` is the conventional Debian package location for the licence notice.

Check your VM's architecture and edit the package description:

```bash
dpkg --print-architecture
nano package/DEBIAN/control
```

Set `Architecture` to the value printed by Dpkg, such as `amd64` or `arm64`. Replace the example maintainer with your classroom name and email, and set the description to your release label. Keep the package name `student-game` and version `1.0` for this round. Leave a newline after the last line.

Build the installer:

```bash
dpkg-deb --build --root-owner-group package student-game.deb
```

`--build` makes the installer from the folder. `--root-owner-group` records the installed files as owned by root while letting you build as your normal user. `student-game.deb` is the output file. See the [Dpkg-deb manual](https://manpages.debian.org/bookworm/dpkg/dpkg-deb.1.en.html) for the package format.

Keep the publisher and player's Linux distribution version and architecture the same. This installer contains your compiled binary, which depends on their system libraries.

## Sign the finished installer

Sign using **your own** key:

```bash
gpg --local-user YOUR_FINGERPRINT --detach-sign student-game.deb
```

`--local-user` selects your signing key. `--detach-sign` creates the separate file `student-game.deb.sig`. Enter your private key's passphrase if asked. The installer stays readable and installable.

The signature covers the finished installer's exact bytes. If you rebuild or edit the installer, create a new signature for the replacement. Signing does not encrypt the installer. [GnuPG signing operations](https://gnupg.org/documentation/manuals/gnupg/Operational-GPG-Commands.html)

## Archive and encrypt the modified source

For Snake Duel or Battleship:

```bash
tar -cf source.tar nbsdgames CHANGES.txt
```

For Tetris, use this instead:

```bash
tar -cf source.tar tetris CHANGES.txt
```

`-c` creates an archive, and `-f` names it. The archive contains your modified project, its licence, and your build notes. It may also contain the files produced during compilation; the developer will force a fresh build.

Encrypt it to the **developer's verified public key**:

```bash
gpg --encrypt --recipient DEVELOPER_FINGERPRINT source.tar
```

`--encrypt` creates `source.tar.gpg`. `--recipient` selects the person whose private encryption key can open it. If GPG asks whether to use a key with unconfirmed validity, check the full fingerprint against your completed identity check before answering. Do not guess from the displayed name.

Select only the developer as a recipient for this round. Keep your original source locally. Encrypting the archive does not delete or protect the unencrypted copy on your own VM. The public upstream game also remains available; this exercise protects your modified source package.

Encryption alone does not establish who created the source. The detached signature in this lab authenticates the installer, not the source archive.

## Publish the release files

Create a folder containing only the files you intend to share:

```bash
mkdir public
cp student-game.deb student-game.deb.sig publisher-public.asc developer-public.asc source.tar.gpg public/
cd public
ls
```

Check that these five files are present. Keep `source.tar`, the working source folder, and all private keys outside `public`.

Start the class download server from **inside `public`**:

```bash
python3 -m http.server 8000
```

`-m http.server` runs Python's file-server module. `8000` is its listening port. It serves the current folder. Leave this terminal open while your partners download, and stop it with **Ctrl+C** when finished. [Python HTTP server documentation](https://docs.python.org/3/library/http.server.html)

Give your partners **`http://PUBLISHER_IP:8000/`**, using your VM's reachable address. In another terminal, **`ip address`** shows your addresses. Use the VM network address, not loopback `127.0.0.1`.

Your partners should see the five release files. If the page does not load, check the VM address, shared network connectivity, and whether the server is still running. Where a VM firewall is enabled, permit TCP port 8000 on the class network.

---
[Prev](02_build-and-modify-your-game.md) | [Home](README.md) | [Next](04_verify-and-play.md)
