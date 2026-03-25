# Submission Guide

## What to Submit

Submit the completed PowerPoint template with:

- Screenshot 1: Broken Script vs Sourced Script
- Screenshot 2: Executable Script with Prompt and Argument Modes
- Screenshot 3: DNS Failure and Route Inspection
- Screenshot 4: Reachable Target Returns UP
- Screenshot 5: Failure Path Returns a Diagnostic Exit Code
- Screenshot 6: Batch Test Logged with `tee`

## Before You Submit

Make sure:

- each screenshot is on the correct slide
- terminal text is readable at normal zoom
- command lines and exit codes are not cut off
- `hostcheck.sh`, `targets.txt`, and `batch-results.txt` still exist on the VM

## Final Check

Before you upload the file, make sure you can explain:

- why the Part 1 `hostcheck` idea broke once it was saved as a script
- why `read` is only used when no argument was passed
- why DNS is checked before route and ping
- why the script writes failures to `stderr`
- why `2>&1 | tee batch-results.txt` matters in the final batch test

---
[Prev](05_test-and-log-multiple-targets.md) | [Home](README.md)
