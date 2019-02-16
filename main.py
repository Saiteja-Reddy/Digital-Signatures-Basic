from mod_exp import *
from MR import *
from euclid_mod_inverse import *
import hashlib

print("For A:")
prime, gen = get_Prime_PR()
print(prime, gen)

a = randrange(1, prime - 1)
print("a: ", a)

y1 = mod_expo(gen, a, prime)
print("y1: ", y1)

y2 = mod_expo(y1, a, prime)
print("y2: ", y2)

print("Signing Phase by A:: ")
message = "010101101"
print("Message: ", message)

r = randrange(1, prime - 1)
print("r: ", r)

A = mod_expo(gen, r, prime)
A_bin = format(A, 'b')
print("A: ", A, A_bin )

B = mod_expo(y1, r, prime)
B_bin = format(B, 'b')
print("B: ", B, B_bin)

out = A_bin + B_bin + message
print(out)
c = hashlib.sha1(out.encode()).hexdigest()
c = int(c,16)%prime
print("C:", c)

s = (((a*c) % (prime-1) + r ) % (prime - 1)) ##changed

print("s:" , s)

print("\n Verification Phase by B:: ")

y1_inv = euclid_mod_inverse(y1, prime)
print("y1_inv", y1_inv)
y2_inv = euclid_mod_inverse(y2, prime)
print("y2_inv", y2_inv)

A_1 = (mod_expo(gen, s, prime) * mod_expo(y1_inv, c, prime))%prime
B_1 = (mod_expo(y1, s, prime) * mod_expo(y2_inv, c, prime))%prime

A_1_bin = format(A_1, 'b')
print("A_1", A_1, A_1_bin)

B_1_bin = format(B_1, 'b')
print("B_1", B_1, B_1_bin)

out = A_1_bin + B_1_bin + message  
print(out)
c_1 = hashlib.sha1(out.encode()).hexdigest()
c_1 = int(c_1,16)%prime
print("C_1:", c_1)


