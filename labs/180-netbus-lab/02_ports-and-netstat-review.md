# Ports and Netstat Review

NetBus is being treated here as a **RAT**: a remote access trojan whose goal is to stay reachable and give control over the victim system.

---
### 🧠 Objectives of a RAT

> [!NOTE]
> **Question:** Which of the following are valid objectives of a RAT?
>
> - [ ] Stealing data
> - [ ] Modifying data
> - [ ] Disrupting the performance of computers or computer networks
> - [ ] Deleting data

<details>
<summary>👉 <b>Check your answer</b></summary>

**Correct Options:** Stealing data, Modifying data, Disrupting performance, and Deleting data
</details>

---

### 🎥 Introduction to ports

[Watch Video](https://youtu.be/CYbVxTcEVXI)

Read these two references before continuing:

- [Ephemeral port](https://en.wikipedia.org/wiki/Ephemeral_port)
- [Command Redirection and Pipes](https://ss64.com/nt/syntax-redirection.html)

## What the first video is demonstrating

The walkthrough uses Firefox to compare:

- a process that is merely running
- ports that are in a `LISTENING` state
- ports that are in an `ESTABLISHED` state

Key points from the walkthrough:

- `0.0.0.0` means the service is listening on every IP address assigned to the computer
- the local port is the port on your own system
- the foreign port is the port on the remote server
- ephemeral ports are the temporary source ports used by the client side of a connection
- one browser tab can create many outbound connections because modern pages load content from multiple external services

## Recommended commands from the walkthrough

Use the commands below while reviewing the video:

```bat
tasklist
netstat -nao
netstat -nao | find /i "established"
tasklist | find /i "firefox"
```

The first video also points out that `find` is case-sensitive by default, so using `/i` avoids unnecessary misses.

---
### 🧠 Ephemeral port

> [!NOTE]
> **Question:** In a client connection, where is the ephemeral port normally found?
>
> - [ ] Source of the connection
> - [ ] Target of the connection

<details>
<summary>👉 <b>Check your answer</b></summary>

**Correct Option:** Source of the connection
</details>

---

### 🧠 Find Firefox

> [!NOTE]
> **Question:** What command did the original H5P expect for finding `firefox` while ignoring case?

<details>
<summary>👉 <b>Reveal answer</b></summary>

```bat
tasklist | find /i "firefox"
```
</details>

---

### 🧠 Connection states

> [!NOTE]
> **Question:** What Windows connection-state terms did the original H5P use for these meanings?
>
> - connected
> - waiting for a connection

<details>
<summary>👉 <b>Reveal answer</b></summary>

- connected: `ESTABLISHED`
- waiting for a connection: `LISTENING`
</details>

---

### 🎥 Part 2 Netstat example

[Watch Video](https://youtu.be/TdlYQNcISBM)

## What `netstat -nao` means

The second video breaks down the switches used throughout the lab:

- `-n` keeps port numbers numeric instead of resolving them to service names like `https`
- `-a` shows all connections and listening ports
- `-o` shows the PID so you can map a connection back to a process

The video also demonstrates using these commands together to verify whether a port really changed before trying to connect to the trojan from the attacker system.

---
### 🧠 Tasklist and searching

> [!NOTE]
> **Question:** When using `find` with `tasklist`, what are you searching for?

<details>
<summary>👉 <b>Reveal answer</b></summary>

**Correct answer:** the process name
</details>

---

### 🧠 Netstat search targets

> [!NOTE]
> **Question:** What can you search for in `netstat` output?
>
> - [ ] `ESTABLISHED`
> - [ ] `LISTENING`
> - [ ] PID
> - [ ] source or destination IP address
> - [ ] port

<details>
<summary>👉 <b>Check your answer</b></summary>

**Correct Options:** all of the above
</details>

---
[Prev](01_overview-and-preparation.md) | [Home](README.md) | [Next](03_challenge-and-submission.md)
