https://en.wikipedia.org/wiki/IPv4#Fragmentation_and_reassembly

#### Terms 
*MTU* = max data supported over the link. 
header+data both considered.

*Fragment payload size:* the nearest smallest multiple of 8 to $MTU - header$.

This because fragment offset count data in 8 bytes unit.

[So fragment payload size of **every fragment but the last** are multiples of 8.](fragmentation%20fields.md#^2dc9f8)
![](attachments/Pasted%20image%2020260429122148.png)
#### Re-fragmentation

It is possible that a packet is fragmented at one router and that the fragments are further fragmented at another router. For example, a packet of 4,520 bytes, including a 20-byte IP header, is fragmented to two packets on a link with an MTU of 2,500 bytes:

| Fragment | Size (bytes) | Header size (bytes) | Data size (bytes) | Flag More fragments | Fragment offset (8-byte blocks) |
|:---|:---|:---|:---|:---|:---|
| 1 | 2,500 | 20 | 2,480 | 1 | 0 |
| 2 | 2,040 | 20 | 2,020 | 0 | 310 |

The total data size is preserved: 2,480 bytes + 2,020 bytes = 4,500 bytes. The offsets are 0 and $\frac{0 + 2,480}{8} = 310$.

When forwarded to a link with an MTU of 1,500 bytes, each fragment is fragmented into two fragments:

| Fragment | Size (bytes) | Header size (bytes) | Data size (bytes) | Flag More fragments | Fragment offset (8-byte blocks) |
| :------- | :----------- | :------------------ | :---------------- | :------------------ | :------------------------------ |
| 1        | 1,500        | 20                  | 1,480             | 1                   | 0                               |
| 2        | 1,020        | 20                  | *1,000*           | 1                   | 185                             |
| 3        | 1,500        | 20                  | 1,480             | 1                   | 310                             |
| 4        | 560          | 20                  | *540*             | 0                   | 495                             |

Again, the data size is preserved: 1,480 + 1,000 = 2,480, and 1,480 + 540 = 2,020.

**The last offset and last data size are used to calculate the total data size: 495 x 8 + 540 = 3,960 + 540 = 4,500.**

---

*In such cases we focus on apply MTU limit individually to (fragments) packets.*

One more example
	![](attachments/Pasted%20image%2020260429125535.png)
#### Reassembly

A receiver knows that a packet is a fragment if at least one of the following conditions is true:

- The flag _more fragments_ is set, which is true for all fragments except the last.
- The field _fragment offset_ is nonzero, which is true for all fragments except the first.

The receiver identifies matching fragments using the source and destination addresses, the protocol ID, and the identification field. The receiver reassembles the data from fragments with the same ID using both the fragment offset and the more fragments flag.