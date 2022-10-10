Socket is for end to end connection
Basically for end to end connection

```
Types of Socket connections:
socket.AF_INET --> for IPV4 Internet
socket.AF_INET6 --> for IPV6 Internet
socket.AF_BLUETOOTH --> for Bluetooth connection
socket.AF_INFRARED --> for Infrared connection etc.

We also need to specify if socket is
socket.SOCK_STREAM --> for TCP connection
socket.SOCK_DGRAM --> for UDP connection
```

Steps on server side:
1. Import socket
2. create a socket obj with socket type (AF_INET, AF_BLUETOOTH) and protocol (TCP/UDP)
3. Bind your machine with the socket obj
4. Start listening from client/s
5. accept() method returns a comm channel between server and client once connection is received. The comm channel is another socket obj. The method also returns address of the client.
6. While sending/receiving message it must be encoded/decoded.

On server side (You can utilize threading here to do all sort of stuffs. For threading look Tim's work ) Socket
Socket Programming with Python
