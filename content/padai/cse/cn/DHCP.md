DHCP relies heavily on limited broadcast because a new client has **no IP address** and **no knowledge of the server's IP**.

**The DORA Process:**

1.  **Discover (Client → Server)**
    *   **Action:** Client asks, "Is there a DHCP server out there?"
    *   **Src IP:** `0.0.0.0` (Client has no IP).
    *   **Dst IP:** `255.255.255.255` (Limited Broadcast).
    *   **Dst MAC:** `FF:FF:FF:FF:FF:FF`.
    *   **Port:** UDP 67 (Server) / 68 (Client).

2.  **Offer (Server → Client)**
    *   **Action:** DHCP Server sees the broadcast, reserves an IP, and says, "I can give you `192.168.1.50`."
    *   **Src IP:** Server's IP (e.g., `192.168.1.1`).
    *   **Dst IP:** Usually `255.255.255.255` (or the offered IP if the client supports it).
    *   **Note:** The client still doesn't have a valid IP, so it listens to the broadcast.

3.  **Request (Client → Server)**
    *   **Action:** Client says, "I accept `192.168.1.50`."
    *   **Dst IP:** `255.255.255.255`.
    *   **Why Broadcast?** To inform *other* DHCP servers that their offers were declined.

4.  **Acknowledge (Server → Client)**
    *   **Action:** Server confirms, "IP `192.168.1.50` is yours. Here is your subnet mask and gateway."
    *   **Dst IP:** `255.255.255.255` (or Unicast depending on OS implementation).
    *   **Result:** Client configures its network interface.

**Key Takeaway:** Without [[limited broadcast]], a device with no IP address could never talk to a server to get one.