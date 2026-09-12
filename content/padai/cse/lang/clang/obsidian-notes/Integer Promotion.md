Whenever a small integer type (`char` or `short`) is used in an expression, it is implicitly converted to int.

Note: in printf a single instance of these data types is NOT integer promoteded (unless it is part of a bigger expression). Clearly what would be the use if this was not the case?

It depends on the format specifier used.
%c used with char -> nothing
%d used with char -> extension. Tough this is not integer promotion.

Integer promotion requires expressions.
