https://stackoverflow.com/questions/67623166/c-how-does-signed-to-signed-integer-conversion-work
https://beej.us/guide/bgc/html/split/types-iii-conversions.html#fnref113

![](attachments/Pasted%20image%2020260428074715.png)

In an expression with mix of these types, the numbers are converted as shown.

When we try to assign a data of another type to another, if the source can be preserved in the destination then it is preserved.

Other wise it is complicated, and implementation dependent.


NOTE: 4/3 results in an integer. It is integer division, not floor divison.
