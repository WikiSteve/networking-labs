# Computing Foundations and Securing Linux

This book combines a computing-foundations sequence with a follow-on GNU/Linux administration and security sequence into one continuous path. It starts with how computers, operating systems, storage, and processes work, then moves into Linux administration, trust, services, and defense.

The goal is not to reproduce slide decks page by page. The goal is to preserve the teaching logic that mattered:

- understand the machine before you secure it,
- learn the command line before you automate it,
- understand storage and recovery before you build services on top,
- understand trust before you deploy encrypted or remotely managed services,
- and treat hardening as an ongoing practice instead of a one-time checklist.

Where older materials used narrow distro details, term-specific lab numbering, or aging implementation choices, this book keeps the durable concept and trims the noise. Where the reconstructed course material had useful operational detail, this public book keeps it instead of flattening everything into overview prose.

This book also pulls forward the cleaned lecture notes and labs that already exist in this repo. Use [Repo Companion Material](repo-companion-material.md) if you want the chapter-by-chapter bridge back into those notes and labs.

## How To Read This Book

- Read Part I first if you want the full foundation.
- Start at Part II if you already know basic computer architecture, operating systems, storage, and the command line.
- Use the practice links at the end of each chapter when you want hands-on follow-up from the cleaned repo materials.
- Use the external reading links when you want a second explanation, a diagram, or a broader reference point.

## Part I: Computing Foundations

1. [Systems, Startup, and Virtualization](01-systems-startup-and-virtualization.md)
2. [Privilege, System Calls, Processes, and Interfaces](02-privilege-system-calls-and-processes.md)
3. [Memory, Filesystems, and Storage Layout](03-memory-filesystems-and-storage-layout.md)
4. [Availability, RAID, Backup, and Recovery Planning](04-availability-raid-backup-and-recovery-planning.md)
5. [Command Lines, Batch Files, and Administrative Automation](05-command-lines-batch-files-and-administrative-automation.md)

## Part II: GNU/Linux Administration and Operations

6. [GNU/Linux Foundations, Editors, Packages, and Source-Based Administration](06-gnu-linux-foundations-editors-packages-and-source-based-administration.md)
7. [Identities, Permissions, ACLs, and Local Security](07-identities-permissions-acls-and-local-security.md)
8. [Boot, Recovery, Terminals, and Secure Remote Access](08-boot-recovery-terminals-and-secure-remote-access.md)
9. [Linux Storage, LVM, and Filesystem Administration](09-linux-storage-lvm-and-filesystem-administration.md)
10. [Linux Networking and Distribution-Specific Administration](10-linux-networking-and-distribution-specific-administration.md)

## Part III: Trust, Services, and Defense

11. [Certificates, TLS, and Service Trust](11-certificates-tls-and-service-trust.md)
12. [File Transfer, File Sharing, Hardening, and Rootkits](12-file-transfer-file-sharing-hardening-and-rootkits.md)

## Companion Material

- [Repo Companion Material](repo-companion-material.md)
- [Study Guide and Reading Paths](study-guide.md)
- [Glossary](glossary.md)
- [Wikipedia and Web Resources](wikipedia-and-web-resources.md)
- [Reuse and License](reuse-and-license.md)
- [About the Author](about-the-author.md)

## Practical Scope

This book stays aligned with repo material that is already cleaned and safe to reuse. When a chapter points to hands-on work, it favors the public lab notes and normalized reading packs rather than older branded source files.
