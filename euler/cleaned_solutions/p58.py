
#20 mins - smarter brute
# In [18]: %time %run p58.py
# 26241
# CPU times: user 2.21 s, sys: 17.2 ms, total: 2.22 s
# Wall time: 2.24 s


from math import sqrt

def primes_lt3(N):
	"""
	Return all primes less than N > 0 int
	"""
	# test every number less than N/2
	primes = [ i for i in xrange(2,N)
				 if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]

	return primes

PRIMES = primes_lt3(100000)

def is_prime(n):
	"""
	how fast can I determine if n is prime?
	"""
	sqr_n = int(sqrt(n))
	for p in PRIMES:
		if p > sqr_n:
			break
		elif n % p == 0:
			return False
	return True

ratio = 1.

num_primes = 3
st = [3,5,7,9]
inc = 10
side_length = 3

while ratio > 0.1:
	# add layer
	for i in xrange(4):
		st[i] += inc
		if is_prime(st[i]):
			num_primes += 1
		inc += 2
	side_length += 2

	ratio = num_primes / ((2. * side_length) - 1 )

print side_length

