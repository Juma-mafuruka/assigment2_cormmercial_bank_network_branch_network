# assigment2_cormmercial_bank_branch_network
# Commercial Bank Branch Network Automation

## 📌 Project Overview

The **Commercial Bank Branch Network Automation** project is a network configuration, verification, and testing solution developed using **Python, Netmiko, Cisco IOS, and GNS3**.

The project simulates a commercial bank with two interconnected branches. Each branch contains a Cisco router and a Layer 2 switch supporting separate **Customer Service** and **Administration** VLANs.

Network configuration and verification are automated using Python and **Netmiko**, while **OSPF Area 0** provides dynamic routing between the two branches.

The main objective is to achieve reliable **end-to-end connectivity between all network segments and end-user devices** while reducing manual configuration through network automation.

---

## 🎯 Project Objectives

The project aims to:

- Automate Cisco router and switch configuration using Python and Netmiko.
- Configure VLANs for different bank departments.
- Implement 802.1Q trunking between switches and routers.
- Configure router-on-a-stick inter-VLAN routing.
- Establish dynamic routing between branches using OSPF.
- Verify interface, VLAN, trunk, OSPF, and routing status automatically.
- Perform end-to-end ICMP connectivity testing.
- Demonstrate practical Network Automation using a GNS3-based environment.
- Achieve complete connectivity between Branch 1 and Branch 2.

---

# 🏗️ Network Architecture

The network consists of two bank branches connected through a point-to-point link.

### Branch 1

**R1 + SW1**

- VLAN 11 → Customer Service
- VLAN 21 → Administration

### Branch 2

**R2 + SW2**

- VLAN 11 → Customer Service
- VLAN 21 → Administration

The routers are connected using a `/30` point-to-point network and exchange routing information using **OSPF Area 0**.

```text
                         OSPF AREA 0
                    Point-to-Point Link
                    10.2.2.0/30
                           
              10.2.2.1                 10.2.2.2
                 |                         |
                R1 ======================= R2
                 |                         |
               Trunk                     Trunk
                 |                         |
                SW1                       SW2
              /     \                   /     \
             /       \                 /       \
        VLAN 11     VLAN 21       VLAN 11     VLAN 21
       Customer     Admin        Customer      Admin
       Service                   Service
