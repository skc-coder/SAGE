In C, the ternary operator (`?:`) is **right-associative**. 
This means that in a chain like `a ? b : c ? d : e`, it is parsed as `a ? b : (c ? d : e)`.