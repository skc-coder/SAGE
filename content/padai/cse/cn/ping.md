We can use the ping program to find if a host is alive and responding. 

We use ping here to see how it uses ICMP packets. 

The source host sends ICMP echo-request messages;
the destination, if alive, responds with ICMP echo-reply messages. 

The ping program sets the identifier field in the echo-request and echo-reply message and starts the sequence number from 0; this number is incremented by 1 each time a new message is sent. 

Note that ping can *also calculate the round-trip time.* It inserts the sending time in the data section
of the message. When the packet arrives, it subtracts the arrival time from the departure time to get the round-trip time (RTT).
