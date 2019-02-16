import socket
import threading 
import time
import os
from random import *
from struct import *
from message import *
from constants import *
import hashlib
from mod_exp import *
from MR import *
from euclid_mod_inverse import *


def get_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

# thread fuction for each client connnected
def threaded(conn, addr): 
    s_addr = get_ip()
    d_addr = addr[0]

    msg = conn.recv(calcsize('iqq160slllll1024sii'))
    print(unpack_message(msg))

    # while True:
    #     msg = conn.recv(calcsize('iqq10s10si10si80si'))
    #     msg = unpack_message(msg)
    #     print("Received from client: ", msg)

    conn.close() 

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
while True: 
    conn, addr = s.accept()
    print('Connected by', addr)
    t = threading.Thread(target=threaded, args=(conn,addr,))
    t.start() 