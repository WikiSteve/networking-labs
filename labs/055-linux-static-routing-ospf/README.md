# Linux Group Routing: Static Routes and OSPF

Continue what you learned in [Lab 050: Linux Static Routing](../050-linux-static-routing/README.md). Work in groups of **three or four**, with one Debian VM per person. Keep every VM **Bridged** onto the college network.

One person routes for the group; the others host named Nginx websites. Connect with another group using static routes, then repeat with OSPF and try a third group. You will compare what happens when a partner router disappears.

> **Before you start:** Download the [Linux Group Routing SUBMISSION TEMPLATE](<./assets/Linux Group Routing SUBMISSION TEMPLATE.pptx>). Add your group number and members' names. Add each screenshot as you complete the lab, then submit the completed template.

Use the [network allocation workbook](<./assets/Group Routing Network Allocation.xlsx>) to record your assigned network and router DHCP addresses. A [CSV copy](<./assets/Group Routing Network Allocation.csv>) is also available.

## Activities

1. [Group networking and websites](./01_group-networking.md)
2. [Static routing: working path and stale route](./02_group-static-routing.md)
3. [OSPF: learning, withdrawal and recovery](./03_group-ospf.md)

## Five screenshots

| Screenshot | Show |
|---|---|
| 1 | Working static routing and partner websites |
| 2 | Partner stopped: static route remains |
| 3 | OSPF learns the partner network; websites work |
| 4 | Partner stopped: OSPF route disappears |
| 5 | Partner returns; a third group's network and website work |

Examples use Steve Sharpe and fictional partners. Use your real names and addresses. The example terminals show recorded Debian VM commands; your commands may be simpler. For power-state evidence, use the partner's VMware window.

---
[Start](./01_group-networking.md)
