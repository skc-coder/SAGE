## Purpose
- Translates **hostnames** to **IP addresses**
- Humans use names, machines use IPs
- Like a phonebook for the internet

## DNS Services
- **Hostname to IP translation**: `www.example.com` → `93.184.216.34`
- **Host aliasing**: Multiple names for same host (e.g., `www` → `example.com`)
- **Mail server aliasing**: Maps domain to mail server
- **Load distribution**: Rotates IPs for same name (load balancing)

## DNS Hierarchy
![](attachments/Pasted%20image%2020260429091759.png)
- **Root DNS servers**: 13 root servers worldwide
- **TLD servers**: Manage `.com`, `.org`, `.edu`, etc. (~1000+ TLDs)
- **Authoritative DNS servers**: Hold actual records for domains
- **Local DNS server**: ISP-provided or custom resolver

## Query Types
![](attachments/Pasted%20image%2020260429091948.png)
- **Recursive query**: the server asks the next server itself
- **Iterative query**: the server gives address to next server to client to ask himself
- Note: **Host-to-local** in both cases is **recursive**

## DNS Records (Name, Value, Type, TTL)
![](attachments/Pasted%20image%2020260429095929.png)

| Type      | Purpose                           | Example                                  |
| --------- | --------------------------------- | ---------------------------------------- |
| **A**     | Hostname → IPv4                   | `(relay1.bar.foo.com, 145.37.93.126, A)` |
| **NS**    | Domain → authoritative nameserver | `(foo.com, dns.foo.com, NS)`             |
| **CNAME** | Alias → canonical name            | `(foo.com, relay1.bar.foo.com, CNAME)`   |
| **MX**    | Domain → mail server              | `(foo.com, mail.bar.foo.com, MX)`        |

## Host Aliasing (CNAME)
- https://www.youtube.com/watch?v=ZXCQwdVgDno
- Translates one host name to another
- Useful for load balancing and simplifying DNS management

Source: https://en.wikipedia.org/wiki/Domain_Name_System


https://gateoverflow.in/401431/go-classes-iiith-pgee-2026-mock-test-2-question-84?show=401431#q401431 #doubt