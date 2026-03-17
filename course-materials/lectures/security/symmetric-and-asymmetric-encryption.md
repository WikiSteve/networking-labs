# Symmetric and Asymmetric Encryption

- Filename: `Symmetric and Asymmetric Encryption.pptx`
- Subject: `security`
- Type: `lecture`
- Reusable: `yes`
- Source file: [Source copy](../../sources/Symmetric%20and%20Asymmetric%20Encryption.pptx)

## Summary

This reusable lecture deck introduces core cryptography concepts through the lens of confidentiality, integrity, and authenticity, then uses that framework to compare symmetric and asymmetric encryption and explain why real systems usually combine both. It starts with historical context and a plain-language definition of cryptography, then anchors the lesson in the CIA triad by linking confidentiality to symmetric encryption, integrity to hashing, and authenticity to asymmetric cryptography and digital signatures. It explains symmetric encryption as a fast single-key approach suited to bulk data protection, then focuses heavily on the operational problem of key distribution, key storage, rotation, and access control. It then shifts to asymmetric encryption, public/private keypairs, digital signatures, GPG or PGP email, HTTPS, and SSH-related key exchange, with repeated emphasis that Diffie-Hellman is for establishing shared secrets rather than encrypting payloads directly.

## Key Details

- Opens with a general introduction to cryptography and a short history arc from Caesar ciphers to Enigma and modern internet security.
- Uses the CIA triad as the main teaching scaffold, mapping confidentiality to symmetric encryption, integrity to hashing, and authenticity to asymmetric keys and digital signatures.
- Explains symmetric encryption as a fast single-key method for encrypting large amounts of data.
- Identifies symmetric use cases such as data at rest, internal protected traffic, and the bulk-encryption side of hybrid systems.
- Spends substantial time on key management, including secure distribution, storage, key rotation, and access control.
- Names concrete key-management ideas such as Diffie-Hellman, hardware security modules, and encrypted key vaults.
- Introduces asymmetric encryption as a public/private key system and explains how it supports both confidentiality and digital signatures.
- Uses applied examples including GPG or PGP email, verifying installers with GPG, and HTTPS or TLS browser key exchange.
- Clearly states that Diffie-Hellman is not encryption, but a key exchange protocol used to establish a shared secret.
- Compares RSA and ECC, highlighting RSA's track record and ECC's smaller keys and lower compute cost.
- Includes a conceptual discussion of quantum-computing risk and the need for cryptographic agility.
- Ends with the practical takeaway that real systems use hybrid cryptography: asymmetric methods exchange secrets and symmetric algorithms protect the bulk payload.

## Tags

- `cryptography`
- `symmetric-encryption`
- `asymmetric-encryption`
- `diffie-hellman`
- `rsa`
- `ecc`
- `key-management`
- `hybrid-crypto`
