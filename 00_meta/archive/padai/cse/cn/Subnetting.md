* Addressing

** Classfull and classless addresing

Classfull address used to be used before 1983 to save bits transmission that would have been needed for sharing subnet masks. But it led to wastage of a lot of IP addresses and also lead to grwoth in size of routing tables.

Hence classless addressing (CIDR) was created.

https://www.practicalnetworking.net/stand-alone/classful-cidr-flsm-vlsm/

** Reserved addresses in classfull addressing:
There are two kinds of reservations. One affects the network and one affects host address asignment.

*** Type 1.
This reservation reduces the number of networks assignable in each class i.e. some NID numbers are reserved.

In class A, and class C the starting and end network block (group of networks) is also blocked for specific purposes.
In class A the ending block is used for loopback.

So in class A 0.x 127.x and in class C 192.0.0.x and 223.255.255.x is reserved and can't be used as a network. Note that this doesnt reduce any usable host in other networks, it just means that this whole network group of class A and C cant be used.

For other blocks I don't know their use.

Class D is reserved for multicast and cannot be used for regular unicast traffic. Class E is reserved
and cannot be used on the public Internet.

Class B used to have this reservation too, but was later droped.


*** Type 2.
In each class the first and last address are reserved, for network identification purpose
and network brodcast address i.e. the HID numbers are reserved.

In any network say 193.34.23.x (Class C), 193.34.23.0 and 193.34.23.255 are reserved for NID and DBA purpose.

The number of addresses usable for addressing specific hosts in each network is always 2n − 2, where n is the number of rest field bits, and the subtraction of two adjusts for the use of the all-bits-zero host value to represent the network address and the all-bits-one host value for use as a broadcast address.

Mentioned at end.
https://en.wikipedia.org/wiki/Classful_network

** Subnetting
Create groups of networks in a given network.
Done by reserving some bits from HID part.

*Of course the natural way is to reserver the starting bits of the HID part but questions may do it unusual ways.*

** NID, DBA, No of Hosts

For each network/subnet we can define.

NID = All host bits 0 (for subnets it becomes SID).

DBA = All host bits 1

No of hosts = 2^{HID} - 2.

** Supernetting

Combining multiple contigious, same class networks together. Specefic to classful addressing.
Follow the three ruels. They are important here.

** Questions to do
1. On page no 25 and alike.
TODO: The trick to solve such questions is to divide the total hosts possible (take whole 2^{HID}) repeditely by 2. Make a pie and visualize this.

2. Learn class sizes, no of networks and host, range, and their subnet masks.
3. In subnet category five questions.
   Given a IP address, and a subnet mask.
   SID =  IP add AND subnet mask. 
   HID = IP add host part - SID.
   Note that here SID = 01 means 64 and not 1. (try last question on pg. 37).
   Do 6th question on page 38.
   Question 9 on page 39.
   Question 1 on page 40.
    We use class range and the given mask to find subnet bits. Then first subnet is 0, 2nd one is 1, 3rd one is 10 and so on.
    But in each subnet the first and last address are reserved (HID all 0 or all 1). So 1st host is 1, 2nd host is 10. and so on.
   On pg. 41 question 7.
4. On page 29. Focus on diffrentiating between no of IP address / subnet and no of hosts / subnet.
5. To get SID from DBA:
   Note that in DBA in the right hand side, the 0 bits will be 1 in SID and 1 bits may or may not be 1 in SID.
6. Both questions on pg. 48
7. Do questions on 52.
8. Pg. 56.

** Routing table questions

https://en.wikipedia.org/wiki/Routing_table

http://www.faqs.org/docs/linux_network/x-087-2-issues.routing.html

The address recevied by router (desitnation address = DA) is ANDed with net masks (could be subnet mask, or /n in CIDR).
Then if the result matches the network desitnation, router forwards the packet to the correspodning node.

In the questions we start our matching with netids with most 1s.

Note that a router can be connected to a network with subnetting (hence netid will be something like 255.255.255.192) or a simple network (255*4)
or a remote network (255.255.192.0).
