# Connect both phones

[← Verify the wired Partner PC](./05-verify-wired-partner.md) · [Lab overview](./README.md) · [Test the MAC filter and restore access →](./07-test-mac-filter.md)

1. Plug the Archer into the Router PC. Select the **OpenWrt Student Router** tab in VMware. Open **VM → Removable Devices**, point to the USB Wi-Fi adapter, then choose **Connect (Disconnect from Host)**. Accept the USB handoff if VMware prompts you. Reopen its menu and check that it now offers **Disconnect (Connect to host)**.
2. In the Student Router console, run these three commands in order. Look for USB ID `2357:0115` after the first command and a radio such as `phy0` after the second. Run the third only after the radio appears.

   ```sh
   lsusb
   ls /sys/class/ieee80211
   wifi config
   ```

   If the USB ID is missing, review VMware’s device handoff. If the ID appears and there is no radio, ask your instructor to check driver and firmware support. After `wifi config`, sign back in to LuCI and open **Network → Wireless**.
3. Edit the network row beneath your radio, or select **Add** on the radio row if there is no network. In **Device Configuration**, choose the country code for your location and the channel assigned to your bench. For a 2.4 GHz bench, use a width of **20 MHz** and channel **1**, **6**, or **11** as assigned.
4. In **Interface Configuration → General Setup**, select **Access Point**, enter `FirstName-Wireless` as the ESSID using the Router PC operator’s first name, and select **lan** for **Network**. In **Wireless Security**, choose **WPA2-PSK** and set a temporary passphrase. Save, enable the network if needed, and click **Save & Apply**.
5. Join one phone at a time. If the phone offers to stay connected without Internet access, choose to stay connected to your lab Wi-Fi. Open `http://minion.lab/` on each phone. In **Associated Stations**, match each phone to the row that appeared when it joined. A station row shows that the phone joined the radio. Opening the portal checks its network path separately. If the phone is associated but the page will not open, see [Phone joined but Minion will not open](./09-troubleshooting.md#phone-joined-but-minion-will-not-open).

## **Screenshot 5: Show two phones on your access point**

**Requirement:** Show two **Associated Stations** rows under your own SSID. Label them **Phone A** and **Phone B**. Show only the last two pairs of digits of each phone’s Wi-Fi MAC address, and use those same endings in Screenshot 6.

![Two phones associated with the same access point, with client identifiers masked](./evidence/05-phones.png)

[← Verify the wired Partner PC](./05-verify-wired-partner.md) · [Lab overview](./README.md) · [Test the MAC filter and restore access →](./07-test-mac-filter.md)
