https://en.wikipedia.org/wiki/Distance-vector_routing_protocol

A **distance-vector routing protocol** in [data networks](https://en.wikipedia.org/wiki/Data_networks "Data networks") determines the best route for data packets based on distance. Distance-vector routing protocols measure the distance by the number of [routers](https://en.wikipedia.org/wiki/Router_\(computing\) "Router (computing)") a packet has to pass; one router counts as one hop. 

To determine the best route across a network, routers using a distance-vector protocol exchange information with one another, and then using [[bellman ford algorithm]]. 

It requires *max*\* $n-1$  round for $n$ router network.
After 1 iteration of sharing, everyone will know about shortest path to other node using 1 other node.

Distance-vector routing protocols also require that a router inform its neighbours of [network topology](https://en.wikipedia.org/wiki/Network_topology "Network topology") changes periodically.

Another way of calculating the best route across a network is based on link cost, and is implemented through [[link-state routing protocols]].

The term _distance vector_ refers to the fact that the protocol manipulates _vectors_ ([arrays](https://en.wikipedia.org/wiki/Array_data_structure "Array data structure")) of distances to other nodes in the network.


\*: bellman ford algorithm start with not knowing even the neighbors as well.

\*: exact number of iterations for *sure* convergce: max number of hops between any two nodes.

---

#### Example:

![](attachments/Pasted%20image%2020260429153359.png)

Solution:
![](attachments/Pasted%20image%2020260429153440.png)

#### Count to infinity problem
![](attachments/Pasted%20image%2020260429154850.png)

*The core of the count to infinity problem is that if A tells B that it has a path somewhere, there is no way for B to know if the path has B as a part of it.* To see the problem, imagine a subnet connected like A–B–C–D–E–F, and let the metric between the routers be "number of jumps". Now suppose that A is taken offline. In the vector-update-process B notices that the route to A, which was distance 1, is down – B does not receive the vector update from A. The problem is, B also gets an update from C, and C is still not aware of the fact that A is down – so it tells B that A is only two jumps from C (C to B to A). Since B doesn't know that the path from C to A is through itself (B), it updates its table with the new value "B to A = 2 + 1". Later on, B forwards the update to C and due to the fact that A is reachable through B (From C's point of view), C decides to update its table to "C to A = 3 + 1". 

This slowly propagates through the network until it becomes infinity or reaches the max hop count. *This increase convergence time.*

*This problem can be thaught of a special form of routing loop. B will forward to C and C to B messages with A as destination.*

One solution is to limit the max number of hopes, at that point just consider the node offline.

Other is to also send the "nodes making the path" info as well. 

Another solution is for b to advertise infinity to c, just after the disconnection, before c transfers its info to b.  c then will consider that its intermediate route to a, b is reporting it got cut from a then it will also make the entry infinity.

Another solution is *split horizon*
![](attachments/Pasted%20image%2020260429160740.png)

*Split Horizon*: instead of flooding the table through each interface, each node sends only part of its table through each
interface. If, according to its table, node B thinks that the optimum route to reach X is
via A, it does not need to advertise this piece of information to A.

*Split horizon with poisonous reverse:*
![](attachments/Pasted%20image%2020260429161150.png)
![](attachments/Pasted%20image%2020260429161633.png)

In 3 node lope both of these can fail.
![](attachments/Pasted%20image%2020260429162149.png)
![](attachments/Pasted%20image%2020260429162256.png)