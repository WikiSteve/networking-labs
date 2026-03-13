# Starting Debian installer

With the hardware profile configured, power on the virtual machine.

![Illustration introducing the Debian installer startup section.](assets/images/file-62bbbfed7d6ad.png)

Starting Debian installer

Start the virtual machine. Select **Install** and **do not** choose **Graphical Install**.

![Debian installer boot menu with Install selected instead of Graphical Install.](assets/images/file-62bbc106c25da.png)

![Debian installer language selection screen.](assets/images/file-62bbc178d30bd.png)

![Debian installer location selection screen.](assets/images/file-62bbc1aa26504.png)

![Debian installer keyboard configuration screen.](assets/images/file-62bbc1d2bdcad.png)

Accept the defaults on these three screens.

![Debian installer hostname screen with SSharpe-Debian entered as the system name.](assets/images/file-62bbc2b4b85e8.png)

Name the system the same way you named the VM in the previous step.

![Debian installer domain name screen showing Sharpe.com as the example domain.](assets/images/file-62bbc3cfc02ee.png)

Set the domain name to **your last name dot com**. In the example screenshot, that becomes **Sharpe.com**.

![Debian installer root password screen.](assets/images/file-62bbc5ca64ee6.png)

A few notes here:

1. If you set a root password here, `sudo` will **not** be configured automatically.
2. In a later exercise, you will practice disabling the root account and installing `sudo`.

For this lab, have another person set the root password so you do not know it.

Create your regular user account.

![Debian installer screen for entering the full name of the new user.](assets/images/file-62bbc7e2e3ed4.png)

![Debian installer username screen using steve as the account name.](assets/images/file-62bbc862e3055.png)

Use your first name for the user.

![Debian installer user password screen.](assets/images/file-62bbc9295d63d.png)

Have that same person set this password as well. **You should not know either password yet.**

![Debian installer time zone selection screen.](assets/images/file-62bbca16edf86.png)

The original source material assumes the Eastern time zone. If you are elsewhere, select the time zone that matches your location.

---
[Prev](02_downloading-debian.md) | [Home](README.md) | [Next](04_partition-disk-and-configure-lvm.md)
