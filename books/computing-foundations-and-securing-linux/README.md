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

## Practical Scope

This book stays aligned with repo material that is already cleaned and safe to reuse. When a chapter points to hands-on work, it favors the public lab notes and normalized reading packs rather than older branded source files.

## Reuse and License

Unless otherwise noted, the original text and original diagrams in this book are licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

That means you may:

- copy and redistribute the material,
- adapt, remix, transform, and build on it,
- and use it commercially,

as long as you provide attribution, indicate whether you made changes, and include a link to the license.

### Preferred Attribution

If you reuse or adapt this book, please include:

- the book title,
- the author name,
- a link back to the source,
- a link to the CC BY 4.0 license,
- and a note if you changed the material.

Preferred source link:

- <https://github.com/WikiSteve/networking-labs/tree/main/books/computing-foundations-and-securing-linux>

Suggested attribution:

> *Computing Foundations and Securing Linux* by Steve Sharpe, from the `networking-labs` repository, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Changes were made.

If you are reusing the material without changes, replace `Changes were made.` with `No changes were made.`

### Third-Party Material

Some chapters include third-party images, linked external readings, or other referenced material.

- Those items retain their own attribution and licensing requirements.
- The CC BY 4.0 license here applies to the original book material in this directory unless a chapter or asset notes otherwise.
- When in doubt, keep the original source attribution with the reused material.

## About the Author

Steve Sharpe is an IT instructor and hands-on systems educator whose teaching focuses on computing fundamentals, GNU/Linux administration, networking, and security.

His teaching style is practical first. Instead of treating computers as abstract theory, he tends to start with the questions administrators and defenders actually face:

- what the system is doing,
- what layer is responsible,
- what failed,
- how to verify it,
- and how to fix it without guessing.

That approach shapes this book. It explains why the chapters keep returning to:

- command-line literacy,
- step-by-step troubleshooting,
- permission and trust boundaries,
- storage and recovery planning,
- and service configuration that is grounded in real operational choices.

Much of the material in this book was rebuilt from detailed teaching notes, labs, demonstrations, and lecture sequences, then rewritten into a cleaner public form for students. The goal was not to preserve old course packaging. The goal was to keep the useful parts:

- the examples that made concepts stick,
- the administrative habits that prevent avoidable mistakes,
- and the technical depth students need before they can secure systems confidently.

If this book feels more like a guided technical apprenticeship than a glossy overview, that is intentional.
