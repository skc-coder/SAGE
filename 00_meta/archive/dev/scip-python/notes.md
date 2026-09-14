# Lexical scoping
https://stackoverflow.com/questions/1047454/what-is-lexical-scope/19800331#19800331
C doesn't support nested functions and hence staic/lexical scoping also not supported and neither dynamic scoping.

Lexical scoping is finding meaning of a identifier in a function based on the surrounding text where it was defined (thus needing nested function defintions).

Dynamic scoping is finding meaning of an identifier in a function based on the function's caller.

The former can be resolved at compile time always and the later is resolved at runtime.

[functional programming functions](../../padai/cse/bda/functional%20programming%20functions.md)