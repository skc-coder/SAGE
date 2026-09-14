**Identification:** Uniquely identifies the group of fragments of a single IP datagram

**Flags:**
- Reserved (R): 1 bit, must be set to 0
- Don't Fragment (DF): 1 bit, if set, packet is dropped if fragmentation is required. Used for [[path MTU discovery]]
- More Fragments (MF): 1 bit, set for all fragments except the last. Cleared for unfragmented packets

**Fragment Offset:**
- 13 bits
- Specifies the amount of *payload data* (in unit of 8 bytes) *ahead* of current fragment. 
	- ![](attachments/Pasted%20image%2020260429122148.png)
- *Measured in units of 8 bytes (so fragment payload size are multiples of 8,* ***except last***) ^2dc9f8
- First fragment offset is always 0
- Range: 0 to 8191 ($2^{13} - 1$)
- *Maximum offset:* $(2^{13} - 1) \times 8 = 65,528$ bytes of *data* (including 20-byte header = 65,548 bytes total fragmented IPv4 datagram (greater than IPv4 max size!))

[[ipv4 fragmentation]]