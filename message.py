from struct import *

#function to convert IP Address to integer and back
def convertIpToInt(ip):
	return sum([int(ipField) << 8*index for index, ipField in enumerate(reversed(ip.split('.')))])

def convertIntToIp(ipInt):
	return '.'.join([str(int(ipHexField, 16)) for ipHexField in (map(''.join, zip(*[iter(str(hex(ipInt))[2:].zfill(8))]*2)))])

# function to unpack the packet of fixed size with different parameters
def unpack_message(packet):
	opcode, s_addr, d_addr, c, s, q, g, y1, y2, plaintext, ver_status, dummy = unpack('iqq160slllll1024sii', packet)
	out = {}
	out['opcode'] = opcode
	out['s_addr'] = convertIntToIp(s_addr)
	out['d_addr'] = convertIntToIp(d_addr)
	out['c'] = c.decode("ascii").rstrip('\x00')
	out['s'] = s
	out['q'] = q
	out['g'] = g
	out['y1'] = y1
	out['y2'] = y2
	out['plaintext'] = plaintext.decode("ascii").rstrip('\x00')
	out['ver_status'] = ver_status
	out['dummy'] = dummy
	return out

# Create a Packet with input arguments 
def create_message(opcode = 10,
		s_addr = "127.0.0.1",
		d_addr = "127.0.0.1",
		c = "",
		s = -1,
		q = -1,
		g = -1,
		y1 = -1,
		y2 = -1,
		plaintext = "",
		ver_status = -1,
		dummy = -1
	):

	s_addr = convertIpToInt(s_addr)
	d_addr = convertIpToInt(d_addr)

	if len(c) > 160:
		print("Choose smaller c!! (<= 160 chars)")
		return "Err";
	
	if len(plaintext) > 1024:
		print("Choose smaller plaintext!! (<= 1024 chars)")
		return "Err";	
	
	packet = pack('iqq160slllll1024sii', opcode, s_addr, d_addr, c.encode("ascii")
		, s, q, g, y1, y2, plaintext.encode("ascii"), ver_status, dummy)

	return packet

# msg = create_message(c = "20")
# print(msg)
# print(unpack_message(msg))
