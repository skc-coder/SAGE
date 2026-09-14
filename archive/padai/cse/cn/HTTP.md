[HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status#informational_responses)
[[http commands]]
## Basics
- Used for **web pages**
- Built on **TCP**
- **Stateless**: no user info stored by protocol

## Versions
- **HTTP 1.0**: Non-persistent connection
- **HTTP 1.1**: Persistent connection

## Nonpersistent Connections
- One TCP connection per request/response
- Steps:
  1. Client opens TCP, sends request
  2. Server sends response, closes connection
![](attachments/Pasted%20image%2020260429083915.png)
## Persistent Connections
- Single TCP connection for multiple objects on a page or multiple pages. https://gateoverflow.in/523071/gate-cse-2026-set-1-question-9#a_list
- Two modes:
  - **Non-pipelined**: request one object at a time, wait for response
  - **Pipelined**: send multiple requests after base object, without waiting
- Reduces connection overhead vs non-persistent
![](attachments/Pasted%20image%2020260429084112.png)

![](attachments/Pasted%20image%2020260429084314.png)

## Comparison
- Both need $N+1$ requests for $N$ objects
- Non-persistent: disconnect/reconnect each time
- Persistent: keep connection open, less overhead

