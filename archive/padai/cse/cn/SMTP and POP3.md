## Components
- **User Agent (Mail Reader)**:
  - Local program to read, send, manage emails
  - GUI (Outlook, Thunderbird) or command-line
  - Also called **MUA** (Mail User Agent)
- **Message Transfer Agent (MTA)**:
  - Keeps running in background
  - Moves messages between mail servers
  - Also called **MDA** (Mail Delivery Agent)

## Why not direct host-to-host?
- Receiver may not be always online
- User may access mail from multiple devices
- Mail servers act as reliable intermediaries

## Email Flow (Alice → Bob)

![](attachments/Pasted%20image%2020260429093538.png)

1. Alice's MUA → Alice's mail server (SMTP)
2. Alice's server → Bob's mail server (SMTP, port 25)
   - Uses DNS to find Bob's MX record
3. Bob's mail server stores email
4. Bob's mail server -> Bob's MUA  (POP3/IMAP)

## Protocols
![](attachments/Pasted%20image%2020260429102326.png)
- **SMTP**: sending mail (server-to-server, client-to-server)
- **POP3**: downloading mail (server → client, *deletes* from server)
- **IMAP**: managing mail on server (*sync* across devices)
