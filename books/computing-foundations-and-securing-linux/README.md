# Computing Foundations and Securing Linux

This book introduces the systems knowledge needed to understand how computers work, how operating systems impose control on hardware, and how GNU/Linux systems are administered and secured in practice.

The first part builds the machine model used throughout the rest of the text: startup, memory, storage, processes, privilege, and the command line. The second part moves into day-to-day GNU/Linux administration: editors, packages, accounts, permissions, recovery, storage, and networking. The final part covers trust and service security, including certificates, TLS, file transfer, file sharing, hardening, and rootkits.

The chapters are organized so that each later topic rests on earlier ones. Before you can secure a system, you need to understand how it starts, how it stores data, how it separates users and processes, and how administrators inspect and change its state. Before you can deploy services safely, you need to understand trust, naming, permissions, recovery, and failure modes.

This book is written for students who need more than a glossary of terms. It emphasizes concrete system behavior, operational reasoning, and the kinds of examples that help explain not just what a command or service does, but why it behaves that way and how to troubleshoot it when something goes wrong.

## How To Read This Book

- Read Part I first if you want the full foundation.
- Start at Part II if you already know basic computer architecture, operating systems, storage, and the command line.
- Use the practice links at the end of each chapter when you want hands-on follow-up through the companion labs.
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

## Publication Notes

These notes are kept on the landing page for convenience, but they are secondary to the text itself.

<details>
<summary>Reuse and License</summary>

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

</details>

<details>
<summary>About the Author</summary>

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

This book is shaped by the same priorities that drive strong technical instruction:

- examples that make concepts stick,
- administrative habits that prevent avoidable mistakes,
- and enough technical depth for students to reason through problems instead of memorizing isolated commands.

If this book feels more like a guided technical apprenticeship than a glossy overview, that is intentional.

</details>
