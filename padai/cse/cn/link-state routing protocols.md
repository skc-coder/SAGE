https://en.wikipedia.org/wiki/Link-state_routing_protocol 
**Link-state routing protocols** are one of the two main classes of [routing protocols](https://en.wikipedia.org/wiki/Routing_protocol "Routing protocol") used in [packet switching](https://en.wikipedia.org/wiki/Packet_switching "Packet switching") networks for [computer communications](https://en.wikipedia.org/wiki/Computer_communication "Computer communication"), the others being [distance-vector routing protocols](https://en.wikipedia.org/wiki/Distance-vector_routing_protocol "Distance-vector routing protocol").[[1]](https://en.wikipedia.org/wiki/Link-state_routing_protocol#cite_note-1) Examples of link-state routing protocols include [Open Shortest Path First](https://en.wikipedia.org/wiki/Open_Shortest_Path_First "Open Shortest Path First") (OSPF) and [Intermediate System to Intermediate System](https://en.wikipedia.org/wiki/Intermediate_System_to_Intermediate_System "Intermediate System to Intermediate System") (IS-IS).[[2]](https://en.wikipedia.org/wiki/Link-state_routing_protocol#cite_note-2)

The link-state protocol is performed by every _switching node_ in the network (i.e., nodes which are prepared to forward packets; in the [Internet](https://en.wikipedia.org/wiki/Internet "Internet"), these are called [routers](https://en.wikipedia.org/wiki/Router_\(computing\) "Router (computing)")).[[3]](https://en.wikipedia.org/wiki/Link-state_routing_protocol#cite_note-3) The basic concept of link-state routing is that every node constructs a _map_ of the connectivity to the network in the form of a [graph](https://en.wikipedia.org/wiki/Graph_theory "Graph theory"), showing which nodes are connected to which other nodes.[[4]](https://en.wikipedia.org/wiki/Link-state_routing_protocol#cite_note-4) Each node then independently calculates the next best logical _path_ from it to every possible destination in the network.[[5]](https://en.wikipedia.org/wiki/Link-state_routing_protocol#cite_note-5) Each collection of best paths will then form each node's [routing table](https://en.wikipedia.org/wiki/Routing_table "Routing table").[[6]](https://en.wikipedia.org/wiki/Link-state_routing_protocol#cite_note-6)

This contrasts with distance-vector routing protocols, which work by having each node share its routing table with its neighbors. In a link-state protocol, the only information passed between nodes is _connectivity related_.[[7]](https://en.wikipedia.org/wiki/Link-state_routing_protocol#cite_note-7) Link-state algorithms are sometimes characterized informally as each router "telling the world about its neighbors."[[8]](https://en.wikipedia.org/wiki/Link-state_routing_protocol#cite_note-8)
Distance vector routing was used in the ARPANET until 1979, when it was
replaced by link state routing. The primary problem that caused its demise was
that the algorithm often took too long to converge after the network topology
changed (due to the count-to-infinity problem). Consequently, it was replaced by
an entirely new algorithm, now called link state routing.

Here every router knows the whole topology. The network graph. This is the difference between distance vector, where each node nodes about precaluated info about best next hop for a destination.

After knowing the network graph use dijstras algo.

In link-state routing protocols, each router possesses information about the complete [network topology](https://en.wikipedia.org/wiki/Network_topology "Network topology"). Each router then independently calculates the best next hop from it for every possible destination in the network using local information of the topology. The collection of best next hops forms the routing table.

In link-state routing protocols, each router possesses information about the complete [network topology](https://en.wikipedia.org/wiki/Network_topology "Network topology"). Each router then independently calculates the best next hop from it for every possible destination in the network using local information of the topology. The collection of best next hops forms the routing table.

This contrasts with [distance-vector routing protocols](https://en.wikipedia.org/wiki/Distance-vector_routing_protocol "Distance-vector routing protocol"), which work by having each node share its routing table with its neighbours. In a link-state protocol, the only information passed between the nodes is the information used to construct the connectivity maps. 
![](attachments/Pasted%20image%2020260429163650.png)
![](attachments/Pasted%20image%2020260429165930.png)
![](attachments/Pasted%20image%2020260429163855.png)
 Sequence and age field are also used algon with the distance eectors.

This algorithm has a few problems, but they are manageable. First, if the se-
quence numbers wrap around, confusion will reign. The solution here is to use a
32-bit sequence number. With one link state packet per second, it would take 137
years to wrap around, so this possibility can be ignored.

Second, if a router ever crashes, it will lose track of its sequence number. If it
starts again at 0, the next packet it sends will be rejected as a duplicate.

Third, if a sequence number is ever corrupted and 65,540 is received instead
of 4 (a 1-bit error), packets 5 through 65,540 will be rejected as obsolete, since the
current sequence number will be thought to be 65,540.

The solution to all these problems is to include the age of each packet after
the sequence number and decrement it once per second. When the age hits zero,
the information from that router is discarded. Normally, a new packet comes in,
say, every 10 sec, so router information only times out when a router is down (or
six consecutive packets have been lost, an unlikely event). The Age field is also
decremented by each router during the initial flooding process, to make sure no
packet can get lost and live for an indefinite period of time (a packet whose age is
zero is discarded).

~

The first main stage in the link-state algorithm is to give a map of the network to every node. This is done with several subsidiary steps. First, each node needs to determine what other ports it is connected to over fully working links; it does this using _reachability protocol_ that it runs periodically and separately with each of its directly connected neighbours.

Each node periodically (and in case of connectivity changes) sends a short message, the [link-state advertisement](https://en.wikipedia.org/wiki/Link-state_advertisement "Link-state advertisement"), which:

- Identifies the node that is producing it.
- Identifies all the other nodes (either routers or networks) to which it is directly connected.
- Includes a 'sequence number', which increases every time the source node makes up a new version of the message_._

This message is sent to all the nodes on a network. As a necessary precursor, each node in the network remembers, for every one of _its_ neighbors, the sequence number of the last link-state message which it received from that node. When a link-state advertisement is received at a node, the node looks up the sequence number it has stored for the source of that link-state message; if this message is newer (i.e., has a higher sequence number), it is saved, the sequence number is updated, and a copy is sent in turn to each of that node's neighbors. This procedure rapidly gets a copy of the latest version of each node's link-state advertisement to every node in the network.

The complete set produces the graph for the map of the network. The link-state message giving information about the neighbors is recomputed and then flooded throughout the network whenever there is a change in the connectivity between the node and its neighbors, e.g., when a link fails.

## Calculating the routing table

The second main stage in the link-state algorithm is to produce routing tables by inspecting the maps. Each node independently runs an [algorithm](https://en.wikipedia.org/wiki/Algorithm "Algorithm") over the map to determine the [shortest path](https://en.wikipedia.org/wiki/Shortest_path_problem "Shortest path problem") from itself to every other node in the network; generally, some variant of [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm "Dijkstra's algorithm") is used. A node maintains two data structures: a [Tree data structure tree](https://en.wikipedia.org/w/index.php?title=Tree_data_structure_tree&action=edit&redlink=1 "Tree data structure tree (page does not exist)") containing nodes which are "done", and a list of _candidates_. The algorithm starts with both structures empty; it then adds to the first one the node itself. The variant of a [greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm "Greedy algorithm") then repetitively does the following: