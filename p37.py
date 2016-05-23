

# 10 min
# In [46]: time %run p37.py
# 748317
# CPU times: user 12.4 s, sys: 113 ms, total: 12.5 s
# Wall time: 12.7 s

from math import sqrt

def primes_lt3(N):
	"""
	Return all primes less than N > 0 int
	"""
	# test every number less than N/2
	primes = [ i for i in xrange(2,N)
				 if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]

	return primes

PRIME_LIST = primes_lt3(1000000)
PRIME_SET = set(PRIME_LIST)

def is_trunc_prime(p):
	"""
	test if p is truncatable prime
	requires p > 9, AND p IS ALREADY PRIME
	"""
	str_p = str(p)
	return all(int(str_p[:i]) in PRIME_SET and int(str_p[i:]) in PRIME_SET for i in xrange(1,len(str_p)))

# CANDIDATES = filter(lambda p: p > 9 and str(p)[0] in (2,3,5,7) and ())

print sum(filter(is_trunc_prime, PRIME_LIST)[4:]) #drop the first 4 since they are single digit primes