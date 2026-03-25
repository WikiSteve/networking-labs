# Bash Scripting Health Checks

> **Before you start:** Download the [Bash Scripting Health Checks Submission Template](<./assets/Bash Scripting Health Checks SUBMISSION TEMPLATE.pptx>). Add each required screenshot directly into this file as you complete the lab, then submit the completed template for grading.

## Required Reading

- [Bash Introduction](../../course-materials/lectures/systems/bash-introduction.md)
- [Chapter 5: Command Lines, Batch Files, and Administrative Automation](../../books/computing-foundations-and-securing-linux/05-command-lines-batch-files-and-administrative-automation.md)

## Goal

Build a reusable `hostcheck.sh` script that:

- accepts a host or IP address as an argument
- prompts with `read` if no argument was provided
- checks DNS resolution before attempting to ping
- checks for a route before attempting to ping
- returns meaningful exit codes and messages
- logs multiple test results using standard input redirection and `tee`

## Prereqs

- a Debian or Ubuntu VM with `bash`, `ping`, `getent`, `ip`, `awk`, and `tee`
- VMware Workstation configured to use NAT networking
- basic comfort editing a text file with `nano`
- the Bash Part 1 lecture or equivalent knowledge of `stdin`, `stdout`, `stderr`, `read`, and `$?`

## Deliverables

- Screenshot 1 through Screenshot 6 as listed in the lab pages
- a working `hostcheck.sh` in your lab folder
- a `targets.txt` file and a `batch-results.txt` file kept on the VM until grading is complete

## Pages

- [01 Why the First Hostcheck Broke](01_why-the-first-hostcheck-broke.md)
- [02 Build the Real Script](02_build-the-real-script.md)
- [03 Add DNS, Route, and Ping Checks](03_add-dns-route-and-ping-checks.md)
- [04 Test Success and Failure](04_test-success-and-failure.md)
- [05 Test and Log Multiple Targets](05_test-and-log-multiple-targets.md)
- [06 Submission Guide](06_submission-guide.md)
