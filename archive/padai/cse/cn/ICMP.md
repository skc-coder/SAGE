https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol

IPv4 is unreliable and connection less.
No flow and only basic error control.

ICMP is a supporting protocol.

![](attachments/Pasted%20image%2020260429131810.png)

ICMP messages are themselves encapsulated using [IPv4 Header](IPv4%20Header.md). 

ICMP doesn't have port numbers, it uses the port number of UDP/TCP of the original message to inform the application of the error message. Usually this is ignored but [[ping]] and [traceroute](traceroute.md) do make use of it.

![](attachments/Pasted%20image%2020260429132926.png)

The extra 8 bytes contain info about TCP/UDP and port numbers.

#### ICMP messages
- Error reporting
	- ![](attachments/Pasted%20image%2020260429132141.png)
	- Always sent back to original source/originator of the datagram
	- Used by [traceroute](traceroute.md)
- Query: 
	Interestingly, query messages in ICMP can be used independently without relation to
	an IP datagram. Of course, a query message needs to be encapsulated in a datagram, as
	a carrier. Query messages are used to probe or test the liveliness of hosts or routers in
	the Internet, find the one-way or the round-trip time for an IP datagram between two
	devices, or even find out whether the clocks in two devices are synchronized. Naturally,
	query messages come in pairs: request and reply.
	
	‘The echo request (type 8) and the echo reply (type 0) pair of messages are used by
	a host or a router to test the liveliness of another host or router. A host or router sends
	an echo request message to another host or router; if the latter is alive, it responds with an echo reply message. 
	Used by [[ping]]. 
#### Other points
The following are important points about *ICMP error messages:*

- No ICMP error message will be generated in response to a datagram carrying an ICMP error message.

- No ICMP error message will be generated for a fragmented datagram that is not the first fragment.

- No ICMP error message will be generated for a datagram having a multicast address.

- No ICMP error message will be generated for a datagram having a special address such as 127.0.0.0 or 0.0.0.0. ([[DHCP]])
