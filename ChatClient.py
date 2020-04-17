# Matt Hendrick
# CIS 457
# Project 2

# This is the client side of the chat application
import socket
import threading
import tkinter
from tkinter import *
#from project2 import ChatGUI
#from project2 import ChatServer
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = socket.gethostname()
host = input("Please enter the server hostname: ")
port = 6550
server.connect((host, port))
print("Success!")

#def sendMessage(event=None):
#    ChatGUI.sendMessage

def ChatGUI():

