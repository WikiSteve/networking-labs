# Challenge and Submission

## Challenge

The lab challenge is to prove that you can:

- identify the trojan process on the victim
- verify which ports it is listening on
- change the listening port
- prove the new port is active
- connect from the attacker system
- capture evidence of the connection and the password prompt

## Victim-side setup from the video

Use the victim VM first.

1. Go to `C:\Security\netbus` on the victim VM.
2. Show file extensions in Windows Explorer.
3. Rename `Patch.exe` so it looks harmless.
   - The video uses a fake screen-saver style name as a social-engineering example.
4. Run the renamed file on the victim.
5. Open a command prompt.
6. Use `tasklist` to identify the NetBus process and record its PID.
7. Use `netstat -nao` and the PID to confirm the listening ports.
8. The video shows the default listening ports as `12345` and `12346`.

Useful commands:

```bat
hostname
tasklist
tasklist | find /i "patch"
netstat -nao
netstat -nao | find "<PID>"
netstat -nao | find /i "listening"
```

## Port-change verification

The walkthrough makes one point very clearly: do not assume the port changed just because you tried to change it.

Before connecting from the attacker:

1. change the listening port in the trojan configuration
2. run `netstat -nao` again on the victim
3. verify that the old listening port is gone
4. verify that the new listening port is now present

## Attacker-side connection test

Once the victim is listening on the new port:

1. identify the victim IP address
2. open the attacker-side NetBus client
3. connect to the victim using the updated port
4. return to the victim and verify the state changed from `LISTENING` to `ESTABLISHED`
5. confirm that the password prompt window appears

Useful verification commands:

```bat
hostname
netstat -nao
netstat -nao | find /i "established"
```

## Screenshot 1

Capture one screenshot that shows all of the following:

1. the hostname in the command prompt window
2. the new listening port used for the connection
3. the password prompt window
4. enough `netstat` output to prove the connection is active

## Hostname guidance

Older course-platform-specific names have been scrubbed here, but the intent stays the same:

- make sure each VM has a clear hostname
- show that hostname in the command prompt in every screenshot

Example pattern:

- Windows 7 system: `Hacker-YourUsername`
- Windows Server 2008 system: `Victim-YourUsername`

## Submission rules

- crop the image to show only what is needed
- do not include the full VMware desktop if it is not relevant
- keep the submission clean and easy to read

---
[Prev](02_ports-and-netstat-review.md) | [Home](README.md)
