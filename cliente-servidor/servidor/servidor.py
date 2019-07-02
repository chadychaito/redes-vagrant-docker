import socket
import sys

host = 'localhost'
port = 8220
address = (host, port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen(5)

print ("Listening for client . . .")
conn, address = server_socket.accept()
print ("Connected to client at ", address)

while True:

    output = conn.recv(2048)
 
    if output.strip() == (b"disconnect"):
        conn.close()
        sys.exit("Received disconnect message.  Shutting down.")
        conn.send(b"dack")
    elif output:
        arq = open('banco-dados.txt', 'wb')
        arq.write(output)
        conn.send(b"ack")
        arq.close()