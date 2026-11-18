# Hide the Secret

Sign in as **Alice** with her first password. The first sign-in takes a few minutes while Windows builds her profile. If Windows offers privacy choices, accept the defaults. If it offers to set up a **PIN** or **Windows Hello**, choose **Skip**. This lab uses passwords only.

## Make the mission folder

In File Explorer, select **View > Show > File name extensions** so you can see `.txt` and `.pfx`.

Alice uses **Public Documents**, a folder Windows shares with every local user. Bob and LabAdmin should be able to read plain files here, Both new files inherit the folder’s permissions. Reading the plain control file will confirm access before you test the encrypted file.

Choose **one** route.

**GUI route:** Open **File Explorer**. Click the address bar, type `C:\Users\Public\Documents`, and press **Enter**. Right-click empty space and select **New > Folder**. Name it `EFS-Lab` and open it.

Right-click empty space and select **New > Text Document**. Name it `public` (Windows keeps the `.txt` ending). Open it, type the text below, save with **Ctrl+S** and close Notepad:

```text
PUBLIC NOTICE: Book club meets Thursday. Snacks provided. Everyone welcome.
```

Make a second text document the same way. Type `secret` for its name; Windows keeps the `.txt` ending. Check that Explorer displays exactly **public.txt** and **secret.txt**, not names ending in `.txt.txt`. Put this text in the secret:

```text
TOP SECRET: The golden stapler is hidden behind rack 3. Trust no one. - Agent Alice
```

**Command route:** Open Command Prompt (not as administrator).

```cmd
cd C:\Users\Public\Documents
mkdir EFS-Lab
cd EFS-Lab
echo PUBLIC NOTICE: Book club meets Thursday. Snacks provided. Everyone welcome. > public.txt
echo TOP SECRET: The golden stapler is hidden behind rack 3. Trust no one. - Agent Alice > secret.txt
```

`echo` prints the text, and `>` saves it into the named file instead of the screen.

Finish your text **before** encrypting. Do not edit `secret.txt` afterward.

## Encrypt only secret.txt

Choose **one** route.

**GUI route:** Right-click `secret.txt` and select **Properties**. Select **Advanced**. Check **Encrypt contents to secure data**. Select **OK**, then **Apply**.

Windows shows an **Encryption Warning** because the folder itself is not encrypted. Select **Encrypt the file only**, then **OK** twice.

**Command route:**

```cmd
cd C:\Users\Public\Documents\EFS-Lab
cipher /e secret.txt
```

`cd` changes to the mission folder; `/e` means encrypt. `cipher` encrypts just the file you name.

Why **file only**? Encrypting the folder would make new files there encrypted too. Alice's notice must stay readable, so `EFS-Lab` and `public.txt` stay plain.

If Windows offers a key-backup notification, you can close the notification and follow the backup steps below.

## Check the result

**GUI route:** Look at the icons. `secret.txt` shows a small **padlock**; `public.txt` does not. For a closer look, open `secret.txt`'s **Properties > Advanced > Details**: expect only **Alice** under users who can access the file, with no recovery certificate. If a recovery certificate is listed, ask your instructor before the reset test.

**Command route:**

```cmd
cd C:\Users\Public\Documents\EFS-Lab
cipher
```

`cd` changes the current folder. With no options, `cipher` lists that folder. Expect `E secret.txt` (encrypted) and `U public.txt` (unencrypted).

Open `secret.txt`. Alice can read it normally because Windows unlocks her private key automatically.

## Back up Alice's key

Alice's private key lives only in her profile. Save a copy in a **PFX** file on her **Desktop**. The Desktop is outside the encrypted file and is not encrypted itself.

Choose **one** route.

**GUI route:** Press **Windows+R**, type `certmgr.msc`, and press **Enter**. This opens **Alice’s user certificates**.

1. Open **Personal > Certificates**. Select the certificate whose **Intended Purposes** includes **Encrypting File System**.
2. Right-click it and select **All Tasks > Export**.
3. Select **Next**, then **Yes, export the private key**, then **Next**. If this option is unavailable, stop and ask your instructor.
4. Keep **Personal Information Exchange (.PFX)**. Do not select **Delete the private key if the export is successful**. Select **Next**.
5. Select **Password**, enter the backup password twice, then **Next**.
6. Select **Browse**, choose **Desktop**, and name the file `alice-efs.pfx`. Select **Save > Next > Finish**.
7. Expect **The export was successful**.

**Command route:** Open Command Prompt (not as administrator). The full path below saves the backup to Alice’s Desktop, wherever your command window started.

```cmd
cipher /x C:\Users\Alice\Desktop\alice-efs
```

`/x` exports Alice's current EFS certificate **and** private key. Confirm the Windows prompt, then type the backup password twice. Windows adds `.pfx` to the name.

Expect `alice-efs.pfx` on the Desktop. If the file is missing or the export failed, stop here: do not reset Alice’s password until you have the backup. In real life, move a PFX to a USB drive or safe storage, because anyone holding it and its password can open Alice's files.

## **Screenshot 1: Alice's Encrypted Secret and Key Backup**

**Requirement:** In one screenshot, show all three of these, with no password visible:

- `secret.txt` marked encrypted (padlock icon or `E` in `cipher` output)
- `public.txt` not encrypted (no padlock, or `U`)
- `alice-efs.pfx` on Alice's Desktop

Close Notepad. **Sign out** Alice.

---
[Prev](01_create-the-agents.md) | [Home](README.md) | [Next](03_test-the-lock.md)
