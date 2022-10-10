import socket

# Which server to connect
#SERVER = "localhost"
SERVER = '172.16.190.73'
PORT = 5151

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_obj.connect((SERVER, PORT))

message_from_client = "[Client] : Hello Mr. Server! How ya doin'".encode('utf-8')
socket_obj.send(message_from_client)
message_from_server = socket_obj.recv(1024).decode('utf-8')
print(message_from_server)