Used for error checking of the **header (not data)**. 

Before sending a packet, the checksum is computed as the 16-bit [ones' complement](https://en.wikipedia.org/wiki/Ones%27_complement "Ones' complement") of the ones' complement sum of all 16-bit words in the header. 

![](attachments/Pasted%20image%2020260429115317.png)

This includes the _Header Checksum_ field itself, which is set to zero during computation. The packet is sent with _Header Checksum_ containing the resulting value. 

When a packet arrives at a router or its destination, the network device recalculates the checksum value of the header, now including the _Header Checksum_ field. The result should be zero; if a different result is obtained, the device discards the packet.

When a packet arrives at a router, the router decreases the _TTL_ field in the header. Consequently, the router must calculate a new header checksum before sending it out again.

Errors in the data portion of the packet are handled separately by the encapsulated protocol. Both [UDP](https://en.wikipedia.org/wiki/User_Datagram_Protocol "User Datagram Protocol") and [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol "Transmission Control Protocol") have separate checksums that apply to their data.