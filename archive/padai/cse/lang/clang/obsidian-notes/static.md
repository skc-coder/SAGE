- **Storage**: Static Memory (Compile time)
- **Initial Value**: Zero (if not initialized)
- **Scope**: 
  - Local: Within block
  - Global: Within same file (hidden from linker)
- **Lifetime**: End of program
- **Key Rule**: Initialization happens only ONCE and at **compile time**.
  - `static int x = i;` (where `i` is a local variable) is **invalid** because `i` is only known at runtime.
  - this is also the reason why default value is zero, because initialization happens once and only once. The compiler modifies the program and removes the initialization statements.
- **Linker**: Not available to the linker (file scope restriction).



![](attachments/Pasted%20image%2020260425180402.png)

![](attachments/Pasted%20image%2020260425180704.png)

![](attachments/Pasted%20image%2020260425181500.png)


![](attachments/Pasted%20image%2020260425181728.png)

![](attachments/Pasted%20image%2020260425181846.png)

![](attachments/Pasted%20image%2020260425181857.png)
global -> stored in static
but explict static is not accesible from other files
the int g one is.

![](attachments/Pasted%20image%2020260425182048.png)


![](attachments/Pasted%20image%2020260425193444.png)
![](attachments/Pasted%20image%2020260425193526.png)