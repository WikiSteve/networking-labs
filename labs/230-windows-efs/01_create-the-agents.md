# Create the Agents

Use an existing administrator login on your chosen VM to create three **local lab accounts**. You will play each role on the same computer:

| Account | Role |
| --- | --- |
| LabAdmin | Administrator: manages accounts and permissions |
| Alice | Standard user: owns the encryption key |
| Bob | Standard user: tries to read Alice's secret |

Keep your existing and built-in accounts. If your existing administrator account is already called **LabAdmin** and is an administrator, reuse it and create only Alice and Bob.

## Create the accounts

Choose **GUI or commands**, not both. Use practice passwords that you can remember. Do not use real passwords.

**GUI route:** Press **Windows+R**, type `lusrmgr.msc`, and press **Enter**. This opens **Local Users and Groups**.

1. Select **Users**, then **Action > New User**.
2. Enter `LabAdmin` as the user name and enter its practice password twice.
3. Clear **User must change password at next logon**. Select **Create**.
4. Repeat for `Alice` and `Bob`, then select **Close**.
5. Open **LabAdmin**'s properties. Select **Member Of > Add**. Type `Administrators`, select **Check Names**, then **OK > Apply**. Leave Alice and Bob as standard users.

If LabAdmin already exists, skip creating it and changing its membership.

**Command route:** Open **Start**, type `cmd`, right-click **Command Prompt**, and select **Run as administrator**. Approve the prompt.

```cmd
net user LabAdmin * /add
net localgroup Administrators LabAdmin /add
net user Alice * /add
net user Bob * /add
```

If you are reusing an existing LabAdmin account, run only the last two commands.

For `net user`, `/add` creates an account. The `*` asks you to enter the password twice without displaying it. For `net localgroup`, `/add` adds the named account to that group. Here it makes LabAdmin an administrator.

## Check the roles

**GUI:** In Local Users and Groups, open **Groups > Administrators**. LabAdmin should be listed; Alice and Bob should not. Open **Groups > Users** to check Alice and Bob are present.

**Commands:**

```cmd
net localgroup Administrators
net localgroup Users
```

Other built-in or existing entries are normal. No screenshot is needed here.

## Change users properly

Select **Start**, select your account name, then **Sign out**. Next, sign in as **Alice**.

Use **Sign out**, rather than **Switch user**, whenever this guide changes accounts. Switching users leaves the previous session running and can leave its encryption keys available.

---
[Home](README.md) | [Next](02_hide-the-secret.md)
