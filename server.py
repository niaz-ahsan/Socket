import socket

#HOST = socket.gethostbyname(socket.gethostname())
HOST = '172.16.190.73' # IP of this server
PORT = 5151 # port where this server is going to accept connection

socket_for_listening = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # the socket obj
socket_for_listening.bind((HOST, PORT)) # binding the socket obj with our server

socket_for_listening.listen() # server is listening

while True:
    socket_for_communication, client_addr = socket_for_listening.accept() # once a client connects accept() would return communication channel and client address.
    print(f"[Server-{HOST}] is connected to [{client_addr}]")

    message_from_client = socket_for_communication.recv(1024).decode('utf-8') # messages has be encoded/decoded.
    print(f"[Client-{client_addr}] : {message_from_client}")

    message_from_server = f"[Server-{HOST}] : Hello from server, Got your message!".encode('utf-8')
    socket_for_communication.send(message_from_server)

    socket_for_communication.close()
    print(f"[Server-{HOST}] has closed the connection!")