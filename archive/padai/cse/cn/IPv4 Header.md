https://en.wikipedia.org/wiki/IPv4#Packet_structure

![](attachments/Pasted%20image%2020260429110016.png)

 **Length** of data = total length - (HLEN) x 4
### [fragmentation fields](fragmentation%20fields.md)
[ipv4 fragmentation](ipv4%20fragmentation.md)
### TTL
When the TTL field hits zero, the router discards the packet and typically sends an [ICMP time exceeded](https://en.wikipedia.org/wiki/ICMP_time_exceeded "ICMP time exceeded") message to the sender.

The program _[[traceroute]]_ sends messages with adjusted TTL values and uses these ICMP time exceeded messages to identify the routers traversed by packets from the source to the destination. ^1df7bd

**NOTE:** HOST accepts TTL = 0 message. Why would it drop? :)

### Protocol Field
 
 Defines the next level protocol used in the data portion of the IP datagram.

| Protocol Number | Protocol Name                      | Abbreviation |
| --------------- | ---------------------------------- | ------------ |
| 1               | Internet Control Message Protocol  | [[ICMP]]     |
| 2               | Internet Group Management Protocol | [[IGMP]]     |
| 6               | Transmission Control Protocol      | [[TCP]]      |
| 17              | User Datagram Protocol             | [[UDP]]      |
| 89              | Open Shortest Path First           | [[OSPF]]     |


### [[IPv4 Checksum]]

### [[IPV4 Options]]

https://gateoverflow.in/402845/go-classes-iiith-pgee-2026-mock-test-4-question-87?show=402845#q402845

https://gateoverflow.in/402903/go-classes-iiith-pgee-2026-mock-test-4-question-64?show=402903#q402903

https://gateoverflow.in/403390/go-classes-iiith-pgee-2026-mock-test-5-question-67?show=403390#q403390

https://gateoverflow.in/403410/go-classes-iiith-pgee-2026-mock-test-5-question-58?show=403410#q403410