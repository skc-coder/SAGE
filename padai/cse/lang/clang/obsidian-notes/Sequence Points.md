 C, like most languages, does not specify the order in which the operands of an operator are evaluated. (The exceptions are &&, ||, ? :, and ','.) 

But many operators like `+` don't have sequence point.
So, statements like x = a++ + a++; are useless or you can say answer is undefined, because it is not clear what the value will be.
eg
```c
a++ + a++;
a++ - a++;
a++ * --a;
```

Which means sequence points is nothing but after that point the changes will definitely takes place.
```
Semicolon = ;
Conditional statements = If(), for(), while(), switch()
Ternary operator = ? :
Logical operators = ||, &&
```

https://en.wikipedia.org/wiki/Sequence_point