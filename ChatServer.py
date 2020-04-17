# Matt Hendrick
# CIS 457
# Project 2

import socket
import threading
from project2 import ChatClient
#from project2 import ChatGUI

# This is the server side of the chat application

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Host is Matt-PC
host = socket.gethostname()
port = 6550
server.bind((host, port))
print("Server waiting")
server.listen(1)
client, address = server.accept()
print("Now online")

while 1:
    display = input(str(""))
    display = display.encode()
    client.send(display)
    print("Message Sent")
    receive = client.recv(4096)
    receive = receive.decode()
    print("Friend: ", receive)

#def acceptConnection():

 #   while True:
  #      client, address = server.accept()
  #      client.send("Enter your username: ".encode("utf-8"))
   #     print(address + " is now connected")
  #      threader = threading.Thread(target=clientHandler, args=(client, address))
 #       threader.daemon = True
 #       threader.start()

#def clientHandler(client):

 #   username = client.recv(4096).decode("utf-8")

