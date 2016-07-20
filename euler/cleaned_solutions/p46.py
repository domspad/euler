

# 13 mins -- brute
# In [4]: time %run p46.py
# 5777
# CPU times: user 191 ms, sys: 4.71 ms, total: 196 ms
# Wall time: 195 ms

from math import sqrt

def primes_lt3(N):
	"""
	Return all primes less than N > 0 int
	"""
	# test every number less than N/2
	primes = [ i for i in xrange(2,N)
				 if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]

	return primes

PRIMES = primes_lt3(10000)

def is_square(n):
	"""
	n > 2
	"""
	return int(sqrt(n))**2 == n

def is_goldbach(odd_comp):
	"""
	n >= 9 is odd composite
	"""
	i = 0
	p = PRIMES[i]
	bound = odd_comp
	while p < bound:
		if (odd_comp - p) % 2 == 0 and is_square((odd_comp - p)/2):
			return True
		i += 1
		p = PRIMES[i]
	return False

cand = 9 #first odd composite
BOUND = PRIMES[-1]**2
while cand < BOUND:
	#check if prime
	if cand in PRIMES:
		cand += 2
		continue
	else:
		if is_goldbach(cand):
			cand += 2
			continue
		else:
			print cand
			break
