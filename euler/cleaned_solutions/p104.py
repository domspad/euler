
# In [16]: %time %paste
# 329468
# CPU times: user 23.4 s, sys: 152 ms, total: 23.5 s
# Wall time: 24.1 s



from math import sqrt, floor
import decimal
from decimal import Decimal
decimal.getcontext().prec = 300

SQRT5 = Decimal.sqrt(Decimal(5))
PHI = (Decimal(1) + SQRT5) / Decimal(2)

def fib(n):
	return int( ((PHI**n)/SQRT5) + Decimal(0.5) )  # CANNOT USE floor (gives float --> 'inf')

def trunc_fib_gen():
	"""Just the first 9 digits of each fib number"""
	a, b = 0, 1
	while True:
		yield a
		a,b = b, ((a+b) % 1000000000)

def is_pandigital(n):
	"""
	is 1-9 pandigital
	"""
	str_n = str(n)
	digs = set(str_n)
	return len(str_n) == 9 and len(digs) == 9 and '0' not in digs


def p104():
	gen = trunc_fib_gen()
	for e, tfib in enumerate(gen):
		if is_pandigital(tfib):
			#calculate the actual e^th fib...
			fibe = fib(e)
			digits = len(str(fibe))
			if is_pandigital(int(fibe / 10 ** (digits - 9))):
				print(e)
				break

p104()