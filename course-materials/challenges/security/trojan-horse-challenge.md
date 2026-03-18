# Trojan Horse Challenge

- Filename: `Trojan Horse Challenge.docx`
- Subject: `security`
- Type: `challenge`
- Reusable: `yes`
- Source file: [Source copy](../../sources/Trojan%20Horse%20Challenge.docx)
- Submission template: [Trojan Horse Challenge Submission Template](../../templates/security/trojan-horse-challenge-submission-template.md)

## Summary

This reusable challenge teaches how a Trojan horse can hide inside a seemingly legitimate Bash admin script, exfiltrate host data over HTTP, and be detected through basic forensic analysis on a Debian system. The activity uses a headless Debian VM as both victim and local C2 receiver, plus a Windows 11 VM for browser-based verification. Students build a fake C2 endpoint with Python's built-in HTTP server, create a wrapper script named `system_audit.sh`, install `curl` and `python3`, encode stolen data with `base64`, silently send it with `curl`, and then confirm the exfiltration by reviewing HTTP logs and decoding the stolen token. The challenge ties the exercise to social engineering, process deception, HTTP-based exfiltration, insider-threat style tradecraft, and basic incident response.

## Key Details

- The scenario frames the learner as a sysadmin running a fake "system health" or "optimize performance" script on Debian.
- Part 1 builds a local C2 endpoint under `~/c2/api/log` and serves it with `python3 -m http.server 8080`.
- Part 2 installs required tools with `sudo apt update && sudo apt install curl python3 -y`.
- The Trojanized Bash script collects `$USER`, `hostname`, and `/etc/debian_version`.
- The stolen value is base64-encoded and sent to `/api/log?token=...` using a silent backgrounded `curl` request.
- The wrapper script disguises itself as a normal audit tool by printing `df -h`, `free -h`, and success banners.
- Windows is used to verify browser reachability to `http://<DEBIAN_IP>:8080/api/log` and confirm `{"status":"received"}`.
- Required evidence includes four screenshots: browser proof, Debian audit completion, Python HTTP log proof, and base64 decode proof.
- The forensic phase has learners inspect the Python server logs and decode the exfiltrated token with `base64 -d`.
- The instructions explicitly explain why localhost `127.0.0.1` is used and how that still demonstrates real HTTP exfiltration mechanics.

## Tags

- `bash`
- `trojan-horse`
- `debian`
- `http-exfiltration`
- `python-http-server`
- `base64`
- `forensics`
- `challenge`
