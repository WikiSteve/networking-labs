# Reset and Recover

## Change versus reset

A password **change** happens when Alice types her **old** password and then a new one. Windows uses the old password to re-protect her private key, so her encrypted files keep working.

A password **reset** happens when an administrator sets a new password **without** knowing the old one. Windows cannot re-protect Alice's private key, so her new password may no longer unlock it. That is a safety feature: otherwise any administrator could reset Alice's password, sign in as her and read her files. On a standalone computer with local accounts, a key backup is Alice's way back.

## LabAdmin resets Alice

Alice must be signed out. You signed her out on page 2.

Choose **one** route.

**GUI route:** Press **Windows+R**, type `lusrmgr.msc`, and press **Enter**. Select **Users**. Right-click **Alice** and select **Set Password**. Read the warning about possible loss of information, such as encrypted files. Select **Proceed**, type Alice's **new** password twice, and select **OK**.

**Command route:** In Command Prompt **as administrator**:

```cmd
net user Alice *
```

Type the new password twice. This command does not show the warning dialog that the GUI route displays.

**Restart** the VM: **Start > Power > Restart**. A restart makes sure no old Alice session remains.

## Alice comes back

Sign in as **Alice** with her **new** password.

Choose **one** route.

**GUI route:** In File Explorer, go to `C:\Users\Public\Documents\EFS-Lab`. Open `public.txt`; Alice can still read it. Open `secret.txt`. Expect an access error. Open **Start** so Alice's name shows, then take the screenshot.

**Command route:** Open Command Prompt (not as administrator).

```cmd
cd C:\Users\Public\Documents\EFS-Lab
whoami
type public.txt
type secret.txt
```

Expect the public notice, then **Access is denied**. The file still names Alice's certificate, but her new password cannot unlock the old private key.

If the secret opens instead, the reset did not remove Alice's key access. Do not fake the error. Ask your instructor; the VM may have different key-recovery or account settings. Do not delete certificates to force a failure.

## **Screenshot 4: Alice Locked Out After the Reset**

**Requirement:** In one screenshot, show Alice's account name, the readable `public.txt` text, and the access error for `secret.txt`.

## Restore the key

Choose **one** way to open the **Certificate Import Wizard**:

- Double-click `alice-efs.pfx` on the Desktop, **or**
- Press **Windows+R**, type `certmgr.msc`, and press **Enter**. This shortcut opens Alice's own certificates. Right-click **Personal** and select **All Tasks > Import**, then browse to the Desktop. Change the file type list to **Personal Information Exchange** so `alice-efs.pfx` appears.

Complete the wizard:

1. If asked for **Store Location**, choose **Current User**, then **Next**.
2. Check that the file name points to `alice-efs.pfx`. Select **Next**.
3. Type the backup password. Leave the other options as they are. Select **Next**.
4. Accept the suggested certificate store (**Automatically select** or **Personal**), then **Next**.
5. Select **Finish**. Expect **The import was successful**.

**Current User** matters: it puts the key in Alice's own profile, where EFS looks for it.

## Read the secret again

Choose **one** route.

**GUI route:** Open `secret.txt`. Expect the mission text. Look at the padlock on its icon: the file is **still encrypted**. Alice simply has her key back. Open **Start** so Alice's name shows.

**Command route:** In Command Prompt:

```cmd
cd C:\Users\Public\Documents\EFS-Lab
whoami
type secret.txt
cipher
```

Expect the mission text, then `E secret.txt` and `U public.txt`.

If access is still denied, sign Alice out and back in, then try again.

## **Screenshot 5: Alice's Secret Restored and Still Encrypted**

**Requirement:** In one screenshot, show Alice's account name, the mission text from `secret.txt`, and `secret.txt` still marked encrypted (padlock icon or `E` in `cipher` output).

Mission complete. Remember: **permissions decide who may open a file; encryption decides who can read it. Back up the key before you need it.**

---
[Prev](03_test-the-lock.md) | [Home](README.md)
