# Test the MAC filter and restore access

[← Connect both phones](./06-connect-both-phones.md) · [Lab overview](./README.md) · [Submit and clean up →](./08-submit-and-clean-up.md)

1. Choose one of the two phones to block. Read its current full Wi-Fi MAC address from **Associated Stations**. Phones can use a randomized address for a network, so use the address OpenWrt actually sees.
2. In **Network → Wireless**, click **Edit** beside your SSID. Open **Interface Configuration → MAC-Filter** and choose **Allow all except listed**. In **MAC-List**, select the phone’s full address or enter it and press **Enter**. Confirm it appears in the list. Click **Save**, then **Save & Apply**.
3. Wait for the AP to return. On both phones, try to reconnect using their saved settings. In **Associated Stations**, check that the blocked phone has no row and the other phone is associated again. If a phone uses a different randomized address, record the new address before repeating the filter test. Open Minion again on the phone that can join.

## **Screenshot 6: Demonstrate the MAC filter**

**Requirement:** With the rule active, show the deny-list entry and the other phone’s **Associated Stations** row. Put two LuCI browser windows side by side if needed. Show only the last two address pairs, matching Screenshot 5. In the slide notes, record the blocked phone’s reconnect attempt and what happened after you restored access.

![Saved deny rule with the selected phone’s MAC address ending](./evidence/06-filter.png)
![The other phone associated while the deny rule is active](./evidence/06-filter-station.png)

In **MAC-Filter**, set **MAC Address Filter** back to **Disable**, then **Save** and **Save & Apply**. Reconnect the blocked phone. Verify that it appears in **Associated Stations** and can open the portal again. Keep WPA2 enabled.

[← Connect both phones](./06-connect-both-phones.md) · [Lab overview](./README.md) · [Submit and clean up →](./08-submit-and-clean-up.md)
