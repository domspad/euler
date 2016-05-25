

#15 min
# BRUTE on prime 3 -combos
# In [42]: time %run p49.py
# 2969 6299 9629
# CPU times: user 47.1 s, sys: 148 ms, total: 47.2 s
# Wall time: 47.4 s

from math import sqrt

def primes_lt3(N):
	"""
	Return all primes less than N > 0 int
	"""
	# test every number less than N/2
	primes = [ i for i in xrange(2,N)
				 if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]

	return primes


CANDIDATES = filter(lambda n: n > 1000, primes_lt3(10000))

from itertools import combinations
from collections import Counter

for p1,p2,p3 in combinations(CANDIDATES,3):
	# check arith
	assert p1 < p2 and p2 < p3
	if p2 - p1 != p3 - p2:
		continue

	# check perm
	c1, c2, c3 = Counter(str(p1)), Counter(str(p2)), Counter(str(p3))
	if c1 == c2 and c2 == c3 and p1 != 1487:
		print p1, p2, p3
		break
