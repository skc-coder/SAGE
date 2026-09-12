## Basics
- Uses **TCP**
- At server: `21` for data, `20` for control
- Client can have custom ports
- Two channels:
  - **Control channel**: authentication, commands (remains open)
  - **Data channel**: file transfer (created per file, non-persistent)

## Connection Flow
1. Client initiates **control connection** to server port 21
2. Client sends username/password over control channel
3. For file transfer, server initiates **data connection** to client
4. **File transferred, data connection closes**
5. Repeat for next file (new data connection)

## FTP Modes
https://en.wikipedia.org/wiki/File_Transfer_Protocol#Protocol_overview
### Active Mode
- Client listens on port $M$ for incoming data connection
- Sends `PORT M` command to server
- Server initiates data connection from port 20 to client's port $M$
- Works when client can accept incoming connections

### Passive Mode
- Client sends `PASV` command to server
- Server responds with IP address and port number
- Client initiates data connection to server's specified port
- Used when client is behind firewall (can't accept incoming TCP connections)

