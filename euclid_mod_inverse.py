def gcd(a, b):
	if a == 0:
		return b
	if b == 0:
		return 0
	while(a!=b):
		if(a>b):
			a = a-b
		elif(b>a):
			b = b-a
	return a;

# for a^-1 mod (m)
def euclid_mod_inverse(a, m):
	if gcd(a,m) != 1:
		return -1
	M = m
	y = 0
	x = 1
	if m == 1:
		return 0
	while(a>1):
		q = a//m #quotient
		t = m #divisor

		m = a%m
		a = t
		t = y

		y = x-q*y
		x = t
	if x < 0:
		x = x + M
	return x

print(euclid_mod_inverse(3,23))
