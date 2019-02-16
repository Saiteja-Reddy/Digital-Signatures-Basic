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
    prime = -1
    gen = -1
    y1 = -1
    y2 = -1    

    while True:
        msg = conn.recv(calcsize('iqq160slllll1024sii'))
        msg = unpack_message(msg)
        print("Received from client: ", msg)

        if msg['opcode'] == EXIT:
            print("Client ", addr, " has disconnected!!")
            conn.close()
            exit()

        if msg['opcode'] == PUBKEY:
            #receiving PUBKEY from the client
            print("Received PUBKEY message from Client", addr)
            prime = msg['q']
            gen = msg['g']
            y1 = msg['y1']
            y2 = msg['y2']
            print("Client", addr, "sent : Prime -" ,prime, ", gen-", gen, ", Y1-", y1, ", Y2-", y2)
            continue

        elif msg['opcode'] == SIGNEDMSG:
            #receiving SIGNEDMSG from the client
            print("Received SIGNEDMSG message from Client", addr)
            message = msg['plaintext']
            c = msg['c']
            s = msg['s']
            recv_c = c
            print("Client", addr, "sent : message -" ,message, ", c-", c, ", s-", s)
            c = int(c,16)

            #running the verification algorithm
            y1_inv = euclid_mod_inverse(y1, prime)
            y2_inv = euclid_mod_inverse(y2, prime)
            A_1 = (mod_expo(gen, s, prime) * mod_expo(y1_inv, c, prime))%prime
            B_1 = (mod_expo(y1, s, prime) * mod_expo(y2_inv, c, prime))%prime

            print("A1:", A_1, "B1:", B_1)
            #recomputing the hash using the generated A and B values
            out = str(A_1).encode() + str(B_1).encode() + message.encode()
            # print(out)
            c_1 = hashlib.sha1(out).hexdigest()
            print("Generated c_1:", c_1)

            status = -1

            if c_1 == recv_c:
                print("Received message -", message , "has been verified!!")
                status = 1
            else:
                print("Received Message failed to Verify!!!")
                status = -1

            #sending the verification status to the client
            msg = create_message(s_addr=s_addr,d_addr=d_addr, opcode = VERSTATUS, ver_status = status)
            conn.sendall(msg)

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