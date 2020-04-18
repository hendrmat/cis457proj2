# Matt Hendrick
# CIS 457
# Project 2

import socket
import threading

# This is the server side of the chat application

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 6550
server.bind((host, port))
print("Server waiting")
server.listen(1)
client, address = server.accept()
thread = threading.Thread(target = server, args = (client,))
print("Now online")

def send_message(message, server):
    socket, (host, port) = client
    client.send(server.message.encode("utf8"))

def receive_message(message, client):
    while True:
        message = client.recv(4096)
        server.message = message.decode("utf8")
        server.send_message(server)
