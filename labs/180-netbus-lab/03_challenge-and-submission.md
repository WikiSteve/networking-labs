# Challenge and Submission

## Challenge

The final capture instruction preserved in the lab material is:

> Capture 6: take a screen capture showing the new listening port used to make the connection and the password prompt window.

The note also says the exact command is **not** given. You must prove both that:

- the listening port has changed
- the malware is prompting for a password

This is the only explicit capture instruction still present in the available lab text. The walkthrough videos may have covered additional captures, but they are not described in the written material.

## Suggested victim-side workflow from the video

The second video gives a concrete workflow for proving the trojan is listening and then connected:

1. On the victim machine, run the NetBus executable.
2. Use `tasklist` to find the process.
3. Use `netstat -nao` and the PID to confirm which ports it is listening on.
4. The walkthrough shows the default listening ports as `12345` and `12346`.
5. Change the listening port for the exercise.
6. Verify with `netstat` that the new port is actually listening before trying to connect.
7. From the attacker machine, connect to the victim.
8. Confirm that the victim now shows an `ESTABLISHED` state and the password prompt window.

Helpful commands from the walkthrough:

```bat
tasklist
netstat -nao
netstat -nao | find /i "listening"
netstat -nao | find "<pid>"
netstat -nao | find /i "established"
```

## Screenshot 1

Capture one screenshot that shows all of the following:

1. the hostname in the command prompt window
2. the new listening port used for the connection
3. the password prompt window

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
