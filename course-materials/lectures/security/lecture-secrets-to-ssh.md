# Lecture Secrets to SSH

- Filename: `Lecture Secrets to SSH.pptx`
- Subject: `security`
- Type: `lecture`
- Reusable: `yes`
- Source file: [Source copy](../../sources/Lecture%20Secrets%20to%20SSH.pptx)

## Summary

This reusable lecture deck teaches the conceptual foundations of SSH with a strong emphasis on separating secrecy, server authentication, and user authentication so those parts are not conflated. It explains SSH as a secure replacement for Telnet, notes its default use of TCP port 22, and covers capabilities such as SCP/SFTP, port forwarding, passwordless login, two-factor combinations, and X11 forwarding. The lecture then moves into Diffie-Hellman and perfect forward secrecy as the mechanism for creating temporary symmetric session keys, while stressing that those keys are not the same as the keys used for authentication. It also covers server identity verification, man-in-the-middle attacks, `known_hosts`, first-connection trust warnings, SSH certificate-authority concepts, user keypairs, passphrases, PAM extensions such as Google Authenticator and YubiKey, key file locations, and nonce-based challenge-response authentication.

## Key Details

- Introduces SSH as a secure replacement for Telnet and notes default use of TCP port 22.
- Lists major SSH capabilities beyond shell access, including SCP/SFTP, port forwarding, passwordless authentication, two-factor combinations, and X11 forwarding.
- Explains Diffie-Hellman as the secrecy step that creates a session key.
- Repeats the core teaching point that secrecy is not the same as authentication.
- Uses cartoon examples to explain man-in-the-middle risk and why server authentication matters.
- Covers host public keys, `.pub` file distinctions, and multiple host key types such as ECDSA, Ed25519, and RSA.
- Explains first-time trust warnings and the role and limits of `known_hosts`.
- Mentions certificate authorities as the stronger option for reducing first-contact MITM risk.
- Covers user authentication methods including passwords, keypairs, password-plus-keypair combinations, and PAM-based extensions like Google Authenticator and YubiKey.
- Teaches private-key passphrases correctly, including the warning that a passphrase does not become a true second factor by itself.
- Identifies important file locations such as `~/.ssh/id_rsa`, `id_rsa.pub`, and `authorized_keys`.
- Ends by explaining nonce-based challenge-response logic for proving possession of the private key.

## Tags

- `ssh`
- `lecture`
- `diffie-hellman`
- `perfect-forward-secrecy`
- `known-hosts`
- `mitm`
- `authorized-keys`
- `pam`
