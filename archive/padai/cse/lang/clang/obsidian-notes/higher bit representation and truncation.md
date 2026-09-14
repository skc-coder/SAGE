When you try to "fit" a data of another type to another, you may experience promotion or truncation.

If the destination data type is big then we need promotion.
In promotion, the extension is either 1 or 0 and it depends only depends on the the data type of the source of the data.

1 in case of signed, and negative number (eg, 100)
0 in other cases: signed positive, or unsigned.

If destination type is small then source type or the data then we have truncation.
Truncation just cuts the data.

eg.

```c
char c = 299;
or
int x = 999;
char c = x;
```

---

This step is endiness independent, meaning do reversal in case of little endian.


