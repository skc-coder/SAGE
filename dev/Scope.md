[[../padai/cse/lang/moc python]]
Global variables are not directly referenceable in functions, as lvalue. They are available as rvalue tough. By default in functions the variables reference to local variables.

To use global variable we use  `global glbl_Var` in function.

There is also `nonlocal` to reference to variable of a parent.