**Core Concept:**  
A packet sent to this address is intended for **every device on the local physical network segment**. It never leaves the local subnet.

**The Process:**
1.  **Source:** A host (e.g., a new laptop) needs an IP but has none (`0.0.0.0`).
2.  **Encapsulation:**
    *   **IP Header:** Src=`0.0.0.0`, Dst=`255.255.255.255`.
    *   **MAC Header:** Src=`[My MAC]`, Dst=`FF:FF:FF:FF:FF:FF` (Layer 2 broadcast).
3.  **Transmission:** The frame hits the switch. The switch floods it out **all ports** (except the incoming one) within the same VLAN.
4.  **Reception:** Every device on that LAN receives the frame.
5.  **Filtering:**
    *   Most OSs check the IP. If it’s not for them (and they aren’t the intended service), they drop it immediately.
    *   **Routers:** Drop the packet. They do not forward `255.255.255.255` to other subnets.

---
Used in [[DHCP]]