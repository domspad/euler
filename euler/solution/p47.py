

# 15mins - ugly brute force
# In [26]: time %run p47.py
# 134043
# CPU times: user 39 s, sys: 120 ms, total: 39.1 s
# Wall time: 39.2 s

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

def has_4_prime_facts(n):
	i = 0
	p = PRIMES[i]
	bound = n
	count = 0
	while p <= bound:
		if n % p == 0:
			bound /=p
			count += 1
		i += 1
		if i >= len(PRIMES):
			break
		p = PRIMES[i]
	return count == 4

consecutive = []
cand = 100 # arbitrary starting point
BOUND = PRIMES[-1]**2
while cand < BOUND:
	if has_4_prime_facts(cand):
		consecutive.append(cand)
		if len(consecutive) == 4:
			print consecutive[0]
			break
	else:
		consecutive = []
	cand += 1
