printf doesn’t use the information about type of variable in its interpretation of the bit patterns tough if the format/conversion specifiers don't match then the truncation/extension will use the source data type. 

```c
signed char c = 'x';
printf("%d", c);
```

'c' will be sign extended and the extension is zero or 1 depends on the type of c.
But the type is not used to direct the interpretation of the data. Format specifier does.