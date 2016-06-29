
#14 mins
# In [27]: %time %run p73.py
# 7295372
# CPU times: user 21.1 s, sys: 2.97 s, total: 24.1 s
# Wall time: 26.1 s

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


def prime_fact_upto(n):
	"""
	n > 1, return prime facts of all integers up to n

	12 --> {2:2, 3:1}
	"""
	PRIME_FACTS = [defaultdict(int),defaultdict(int)]
	for i in xrange(2,n):
		if i in PRIMES:
			new_pf = defaultdict(int)
			new_pf[i] = 1
			PRIME_FACTS.append(new_pf)
			continue
		for p in PRIMES:
			if p > sqrt(i) + 1: # not one found!
				new_pf = defaultdict(int)
				new_pf[i] = 1
				PRIME_FACTS.append(new_pf)
				break
			elif i % p == 0:
				new_pf = PRIME_FACTS[i/p].copy()
				new_pf[p] += 1
				PRIME_FACTS.append(new_pf)
				break
	return PRIME_FACTS

PRIME_FACTS = prime_fact_upto(12001)

def phi(n):
	"""
	n > 1 int
	compute phi(n) from prime_fac of n
	"""
	pf = PRIME_FACTS[n]
	total = 1
	for p,num in pf.items():
		total *= (p-1) * (p ** (num - 1))
	return total

PHIS = [phi(n) for n in xrange(2, len(PRIME_FACTS))]
# print sum(PHIS) ## 43 million - number of unique (n,k) for which GCD(n,k)==1 where k<n<=12000

def is_rel_prime(n,d):
	return len(set(PRIME_FACTS[n]) & set(PRIME_FACTS[d])) == 0


fracs = []
for d in xrange(4,12001):
	lb,ub = int(d/3) + 1, int(d/2)+1
	for n in xrange(lb,ub):
		if is_rel_prime(n,d):
			fracs.append((n,d))

print len(fracs)
