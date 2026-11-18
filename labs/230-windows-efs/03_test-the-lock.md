# Test the Lock

`public.txt` is your **control file**. It sits in the same folder as `secret.txt` but is not encrypted. If a person can read it, Windows permissions let that person into the folder. Both files were created in the same folder with inherited permissions. The expected difference is that EFS also requires Alice’s private key for `secret.txt`.

## Bob tries

Sign in as **Bob**. Skip any PIN or Windows Hello offer.

Choose **one** route.

**GUI route:** In File Explorer, go to `C:\Users\Public\Documents\EFS-Lab`. Notice the padlock: Bob can see *that* the file is encrypted, and its name and size, but not its contents. Open `public.txt`. Bob can read the notice. Now open `secret.txt`. Expect an error such as **Access is denied**. Open **Start** so Bob's name shows, then take the screenshot.

**Command route:** Open Command Prompt.

```cmd
cd C:\Users\Public\Documents\EFS-Lab
whoami
type public.txt
type secret.txt
```

`whoami` shows the signed-in account. `type` prints a file. Expect the public notice, then **Access is denied** for the secret.

If Bob cannot read `public.txt` either, the test cannot separate permissions from encryption. Stop and ask your instructor.

## **Screenshot 2: Bob Reads Public but Not Secret**

**Requirement:** In one screenshot, show Bob's account name, the readable `public.txt` text, and the access error for `secret.txt`.

**One warning:** encryption protects what a file *says*, not whether it *survives*. If folder permissions let someone delete or replace a file, encryption will not stop them. Permissions and backups handle that. Do not delete Alice's file.

**Sign out** Bob.

## LabAdmin tries

Sign in as **LabAdmin**. Administrators can override almost any permission. Find out whether that is enough.

Choose **one** route.

**GUI route:** Go to the `EFS-Lab` folder. Open `public.txt`; LabAdmin can read it. Open `secret.txt`. Expect an access error. Open **Start** so LabAdmin's name shows, then take the screenshot.

**Command route:** Open Command Prompt **as administrator**. The window title starts with **Administrator:**, showing that full administrator rights are active.

```cmd
cd C:\Users\Public\Documents\EFS-Lab
whoami
type public.txt
type secret.txt
```

Expect the public notice, then **Access is denied**.

An administrator can change permissions, move files or take ownership. None of that gives LabAdmin Alice's private key, so the contents stay scrambled. A **recovery agent** is an extra key some organizations configure so IT can recover encrypted files. If your chosen VM has one configured, its recovery behaviour can differ from this experiment.

## **Screenshot 3: LabAdmin Reads Public but Not Secret**

**Requirement:** In one screenshot, show LabAdmin's account name, the readable `public.txt` text, and the access error for `secret.txt`.

**Stay signed in** as LabAdmin for the next page.

**Be realistic:** this test shows that administrator rights alone did not decrypt the file. It does not make an administrator harmless. Someone who controls a running computer could install spyware to capture Alice's password, or copy her PFX and try to guess its password.

---
[Prev](02_hide-the-secret.md) | [Home](README.md) | [Next](04_reset-and-recover.md)
