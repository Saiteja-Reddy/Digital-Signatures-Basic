import socket
from random import randrange
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

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

s_addr = get_ip()
d_addr = HOST

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

msg = create_message(s_addr=s_addr,d_addr=d_addr, opcode = 40)
s.sendall(msg)
