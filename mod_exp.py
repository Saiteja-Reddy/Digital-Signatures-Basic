import sys

# code for modular exponentiation
def mod_expo(a, b, c):
	ans = 1;
	a = a%c;
	while b>0:
		bit = b%2
		if bit == 1:
			ans = (ans*a)%c;
		a = (a*a)%c;
		b = b//2
	return ans

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))

# print(mod_expo(a,b,c))