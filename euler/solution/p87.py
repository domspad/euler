

# dirty brute force
# 11 mins
# In [21]: %time %run p87.py
# 1097343
# CPU times: user 1.25 s, sys: 191 ms, total: 1.44 s
# Wall time: 1.73 s


from math import sqrt

def primes_lt3(N):
	"""
	Return all primes less than N > 0 int
	"""
	# test every number less than N/2
	primes = [ i for i in xrange(2,N)
				 if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]

	return primes

M = 5 * (10**7)

B = int((M ** 0.5) + 1)
PRIMES = primes_lt3(B)

PRIME_2 = set([p**2 for p in PRIMES])

PRIME_3 = set([p**3 for p in PRIMES if p**3 < M])

PRIME_4 = set([p**4 for p in PRIMES if p**4 < M])


VALIDS = set()

for p3 in PRIME_3:
	for p4 in filter(lambda x: x < (M - p3), PRIME_4):
		for p2 in filter(lambda x: x <(M - p3 - p4), PRIME_2):
			VALIDS.add(p2 + p3 + p4)

print len(VALIDS)