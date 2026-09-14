types of recurison head and tail.

example of it tail one: 

int sum(Node *head){
if (head == NULL){
return 0;
}

--- 
to get data from recurisve function call use back recursion....i mean return after the recruive call returns..
and obiusl if you want to passs data from top to bottom do via paramter passing and doing head recurison
....
create a tree of function calls.
if variables are before function call, then evaluate/print them.
otherwise after function calls
if variables are static, keep as variable
or if auto variable evaluate.
After creataing the tree do dfs traversal.

## Examples:

![](attachments/Pasted%20image%2020260426123018.png)
compare it to the static int i = 0 version
![](attachments/Pasted%20image%2020260426123302.png)
![](attachments/Pasted%20image%2020260426123516.png)

You may also need not create whole tree.
![](attachments/Pasted%20image%2020260426131734.png)



![](attachments/Pasted%20image%2020260425201812.png)

![](attachments/Pasted%20image%2020260425212902.png)

![](attachments/Pasted%20image%2020260426171209.png)