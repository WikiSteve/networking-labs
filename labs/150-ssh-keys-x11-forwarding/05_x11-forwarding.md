# X11 Forwarding

X11 forwarding can be used across platforms: Linux to Linux, Linux to Windows, or Linux to macOS. In this lab you will demonstrate Linux to Windows.

Xming used to be a common Windows choice, but it has not been updated in years.

![Slide graphic noting that Xming is old and may not be reliable](assets/images/file-6052b070bd16d.png)

![Windows browser or notes showing the older Xming option before switching to VcXsrv](assets/images/file-62c6eda228317.png)

For this exercise, use **VcXsrv Windows X Server** instead.

Download VcXsrv from SourceForge:

https://sourceforge.net/projects/vcxsrv/

Choose the default options during setup. Launch VcXsrv and allow traffic through when Windows prompts you.

Once installed, you should see **XLaunch** in the Windows 11 Start menu. If not, just search for it.

![Windows Start menu search showing XLaunch](assets/images/file-6052a79eea877.png)

![XLaunch or VcXsrv startup window using the default configuration](assets/images/file-6052ad3b5d906.png)

![Windows firewall or security prompt allowing VcXsrv traffic](assets/images/file-62c6f0b036013.png)

Close your existing PuTTY window and then reopen it. Before reconnecting to your Linux VM, enable **X11 forwarding** in **Connection > SSH > X11**.

![PuTTY configuration window with Enable X11 forwarding checked](assets/images/file-6051da4bcb1c9.png)

After you connect, run the following workflow:

- Install `xterm`:
  `sudo apt install xterm`
- Try installing Firefox ESR:
  `sudo apt install firefox-esr`
- You will probably run out of disk space before Firefox finishes installing.
- Launch `xterm` over X11:
  `xterm&`
- A graphical `xterm` window should appear on your Windows desktop.
- After you learn more about LVM, you will resize the root volume so larger GUI applications can be installed and launched the same way.

![Windows desktop showing an xterm window forwarded from the Debian VM](assets/images/file-62c6f3944ff01.png)

## Screenshot 4

Show an `xterm` window with a long listing of your home directory.

---
[Prev](04_key-ring.md) | [Home](README.md)
