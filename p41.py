

#25 mins
# BETTER WAY (see 1- below for first answer)
# In [27]: time %run p41.py
# 7652413
# CPU times: user 2.08 s, sys: 14.9 ms, total: 2.09 s
# Wall time: 2.1 s

# 18 minutes
# 1 - SILLY BRUTE FORCE GOT LUCKY GUESS (no proof of correctness)
# In [14]: time PRIMES = primes_lt3(10000000)
# CPU times: user 4min 31s, sys: 1.74 s, total: 4min 33s
# Wall time: 4min 35s
# In [15]: paste
# for i in xrange(len(PRIMES)-1,-1,-1):
#         if is_pandigital(PRIMES[i]):
#                 print PRIMES[i]
#                 break
# 7652413




from math import sqrt

def primes_lt3(N):
	"""
	Return all primes less than N > 0 int
	"""
	# test every number less than N/2
	primes = [ i for i in xrange(2,N)
				 if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]

	return primes

def is_pandigital(n):
	"""
	is 1-9 pandigital
	"""
	str_n = str(n)
	N = len(str_n)
	digs = set(str_n)
	return digs == set(str(i) for i in xrange(1,N+1))


# 1 - Silly brute way

# PRIMES = primes_lt3(10000000)

# for i in xrange(len(PRIMES)-1,-1,-1):
# 	if is_pandigital(PRIMES[i]):
# 		print PRIMES[i]
# 		break

# 2 - better provably correct way

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

from itertools import permutations

pandigital_primes = []

for n in xrange(9,0,-1):
	for perm in permutations(xrange(1,n+1)):
		num = int(''.join(map(str,perm)))
		if is_prime(num):
			pandigital_primes.append(num)

print max(pandigital_primes)
