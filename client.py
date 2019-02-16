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

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))

# msg = create_message(s_addr=s_addr,d_addr=d_addr, opcode = 40)
# s.sendall(msg)

while True:
	action = input('> ')

	if action == "send":
		message = input("Enter the message to send to server: ")
		if len(message) > 1024:
			print("Enter a message < 1024 characters!!")
			continue

		prime, gen = get_Prime_PR()
		print("Selected Prime : ", prime)
		print("Selected Generator : ", gen)
		
		a = randrange(1, prime - 1)
		print("Master Key - a: ", a)		

		y1 = mod_expo(gen, a, prime)
		print("y1: ", y1)

		y2 = mod_expo(y1, a, prime)
		print("y2: ", y2)

		msg = create_message(s_addr=s_addr,d_addr=d_addr, opcode = PUBKEY, q = prime,
			y1 = y1, y2 = y2, g = gen)
		print("Sent Msg:", unpack_message(msg))		
		server.sendall(msg)

		r = randrange(1, prime - 1)
		print("r: ", r)

		A = mod_expo(gen, r, prime)
		print("A: ", A)

		B = mod_expo(y1, r, prime)
		print("B: ", B)		

		out = str(A).encode() + str(B).encode() + message.encode()
		print(out)
		c = hashlib.sha1(out).hexdigest()
		send_c = c
		print("C:", c, send_c)	
		c = int(c,16)

		s = (((a*c) % (prime-1) + r ) % (prime - 1)) ##changed
		print("s:" , s)

		msg = create_message(s_addr=s_addr,d_addr=d_addr, opcode = SIGNEDMSG,
			plaintext = message, c = send_c, s = s)
		print("Sent Msg:", unpack_message(msg))		
		server.sendall(msg)



	elif action == "exit" or action == "quit":
		msg = create_message(s_addr=s_addr,d_addr=d_addr, opcode = 40)
		server.sendall(msg)
		exit()
	else:
		print("No such action!!")
		print("Choose one among the below actions:")
		print("""1. send\n2. exit/quit""")
