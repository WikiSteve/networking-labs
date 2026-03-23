# Submission and Cleanup

Complete [05 Validate and Prove](05_validate-and-prove.md) before starting this page.

## Step 10. Cleanup

Delete the resource group after you finish validating and capturing evidence.

## Submission

Submit one package per person or pair.

Submit screenshots only.
Use the submission template and place exactly one required screenshot on each slide.


## Required Evidence

1. **Screenshot 1: Resource Group Overview.** Show the resource group name and the main resources created, including both VMs and the VNet.
2. **Screenshot 2: Nginx Running on the Server.** Show the server hostname and `systemctl status nginx` with `Active: active (running)` visible.
3. **Screenshot 3: Internal-Only Service Running on Port 8080.** Show the server hostname, the `ss -ltnp | grep 8080` listener output, and the local `curl http://127.0.0.1:8080` result.
4. **Screenshot 4: Server NSG Inbound Rules.** Show the **Inbound security rules** page with the full custom rule list from `100` through `160` visible, including the client-subnet CIDR in the **Source** column for the allow rules.
5. **Screenshot 5: Server VM Final Network Settings.** Show the server VM **Network settings** page after refresh. The screenshot must show the server VM name, the server IP information, the new subnet-level NSG name, and the full final inbound rule list.
6. **Screenshot 6: Public Browser Access to Port 80.** Show the server public IP in the browser address bar and the public webpage loaded successfully.
7. **Screenshot 7: Failed Public SSH Attempt.** Show a new failed SSH attempt from outside Azure, with the server public IP visible in the command and a failure message such as `Connection timed out` or `Connection refused` visible.
8. **Screenshot 8: Azure-Side Deny Proof for SSH.** Show `IP Flow Verify` or `NSG diagnostics` reporting inbound TCP `22` to the server VM as `Denied`, with a public source IP and the matched rule visible.
9. **Screenshot 9: Client-to-Server SSH over the Private IP.** Show all four of these items: the client hostname, the server private IP in the SSH command, the server hostname after login, and the output of the `w` command with the client private IP visible in the `FROM` column.
10. **Screenshot 10: Client Curl to Port 8080.** Show the client hostname, the same server private IP used in the SSH proof with port `8080` in the command, and the returned internal-only page content.

## What to Submit

- the required screenshots listed above

---

[Prev](05_validate-and-prove.md) | [Home](README.md)
