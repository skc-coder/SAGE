**ARP (Address Resolution Protocol)** is the mechanism that maps a known **IP address** to an unknown **MAC address** on a local network.

It is communicated within the boundaries of a single [subnetwork](https://en.wikipedia.org/wiki/Subnetwork "Subnetwork") and is never [routed](https://en.wikipedia.org/wiki/Routed "Routed").
### How it Works (The Process)

1.  **Check Cache:**
    When Host A wants to send data to Host B (IP known), it first checks its **ARP Cache** (a local table).
    - If the MAC is there: Use it immediately.
    - If not: Proceed to step 2.

2.  **ARP Request (Broadcast):**
    Host A sends a broadcast frame to the entire LAN:
    - **Packet:** "Who has IP `192.168.1.5`? Tell `192.168.1.2`."
    - **Dest MAC:** `FF:FF:FF:FF:FF:FF` (Everyone receives it).
 #doubt how can it brodcast when it is not use all 255 as desitnation ip?
3.  **ARP Reply (Unicast):**
    Host B sees the request, recognizes its own IP, and replies directly to Host A:
    - **Packet:** "I am `192.168.1.5`. My MAC is `AA:BB:CC:DD:EE:FF`."
    - **Dest MAC:** Host A's specific MAC.

4.  **Update Cache:**
    Host A stores the mapping in its ARP Cache (usually for 2–20 minutes) to avoid asking again soon.

