# Samba Active Directory and File Shares

> **Before you start:** Download the [Samba AD Lab Submission Template](https://github.com/WikiSteve/networking-labs/releases/download/samba-ad-lab-html/Samba-AD-Lab-Submission-Template.pptx). Add each required screenshot as you complete the lab, then submit the completed template for grading.

[Download the interactive HTML lab](https://github.com/WikiSteve/networking-labs/releases/download/samba-ad-lab-html/index.html?rev=3) · Open the downloaded `index.html` in your browser. The screenshots load from GitHub.

Your team is preparing an event. Everyone needs the bulletin. Only the editors should see the draft on Samba. On Windows Server, reviewers should be able to read the workbench without changing it. Use the same domain accounts on both servers.

## Lab pages

1. <a name="before-you-start"></a>[Before you start](./01-before-you-start.md)
2. <a name="1-create-the-domain"></a>[Create the domain](./02-create-the-domain.md)
3. <a name="2-join-windows"></a>[Join Windows](./03-join-windows.md)
4. <a name="3-publish-samba-shares"></a>[Publish Samba shares](./04-publish-samba-shares.md)
5. <a name="4-set-windows-permissions"></a>[Set Windows permissions](./05-set-windows-permissions.md)
6. <a name="5-test-as-alice-and-bob"></a>[Test as Alice and Bob](./06-test-as-alice-and-bob.md)
7. <a name="troubleshooting"></a>[Troubleshooting](./07-troubleshooting.md)

<a name="administrators-lookup"></a>Looking for the Workbench picker explanation? [Administrators lookup](./07-troubleshooting.md#administrators-lookup).

## Four screenshots to submit

1. [Domain controller DNS with your hostname](./02-create-the-domain.md#screenshot-1-domain-controller-dns)
2. [Both Windows domain members](./03-join-windows.md#screenshot-2-both-windows-domain-members)
3. [Alice saves to Workbench](./06-test-as-alice-and-bob.md#screenshot-3-alice-saves-to-workbench)
4. [Bob is denied access to Drafts](./06-test-as-alice-and-bob.md#screenshot-4-bob-denied-access-to-drafts)
