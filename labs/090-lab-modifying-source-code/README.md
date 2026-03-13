# Lab Modifying Source Code

## Goal
Download the `traceroute` source package, make a small string change in the C source, build it with `make`, install it, and verify the modified program from both the build tree and the system path.

## Prereqs
- A Debian or Ubuntu Linux virtual machine with internet access
- A user account with `sudo` access
- Basic comfort using `vi`, `apt-get`, and shell commands

## Deliverables
- Screenshot 1: source code downloaded into your home directory
- Screenshot 2: edited `version_string` block in `traceroute.c`
- Screenshot 3: successful `make`
- Screenshot 4: `./traceroute -V` showing your custom version string
- Screenshot 5: successful `sudo make install`
- Screenshot 6: `traceroute -V` run from your home directory after install
- Screenshot 7: a working traceroute command to `www.google.ca`
- Written response comparing the traceroute command variants

## Pages
- [Get the source code](01_get-the-source-code.md)
- [Source tree and build basics](02_source-tree-and-build-basics.md)
- [Edit the source code](03_edit-the-source-code.md)
- [Build the program](04_build-the-program.md)
- [Test and install](05_test-and-install.md)
- [Test in production](06_test-in-production.md)
- [Traceroute exercises](07_traceroute-exercises.md)
- [Written response](08_written-response.md)

## Accessibility

- [Screenshot alt text and OCR transcript data](assets/screenshot-ocr.json)

## TODO
- Retake screenshots 2, 4, and 6 so the displayed custom version string matches the generic placeholder text used in the instructions.
