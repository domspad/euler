

from math import sqrt
from collections import defaultdict

def primes_lt3(N):
	"""
	Return all primes less than N > 0 int
	"""
	# test every number less than N/2
	primes = [ i for i in xrange(2,N)
				 if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]

	return primes

PRIMES = primes_lt3(10000)


from Queue import deque

def get_value(rep):
	total = 1
	for a,p in zip(rep,PRIMES):
		total *= p**a
	return total

def get_children(rep):

	children = []
	if len(rep) == 1:
		children = [(1,0)]
	elif len(rep) == 2:
		children = [(rep[0]+1,0),(rep[0],1,0)]
	else:
		if rep[-2] == rep[-3]:
			children = [rep[:-1] + (1,0)]
		else:
			children = [rep[:-2] + (rep[-2]+1,0) ,rep[:-1] + (1,0)]
	return children

def growing_exps():
	fringe = deque([(0,)])
	while True:
		rep = fringe.popleft()

		# append children
		fringe.extend(get_children(rep))
		# yield val
		yield rep



### ADDED SPICE


from sympy import gcd, divisors

def are_coprime(pair):
	m,n = pair
	return gcd(m,n) == 1

def num_sols_gcd(n):
	divs = divisors(n)
	c = 0
	for e, d1 in enumerate(divs):
		for d2 in divs[e:]:
			if are_coprime((d1,d2)):
				c += 1
	return c

### HERE WE GO

g = growing_exps()

smallest_above_mil = 10**72
smallest_val = 0

for i in g:
	sols = num_sols_gcd(i)
	if sols > 1000 and i < smallest_above_mil:
		smallest_above_mil, smallest_val = i, sols
		break