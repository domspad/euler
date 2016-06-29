
# PRECOMPUTE PRIMES
# PRECOMPUTE PRIME_FACTS
# brute
# 30 mins



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

PRIMES = primes_lt3(100000)


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

PRIME_FACTS = prime_fact_upto(10000000)

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

from collections import Counter
def is_perm(d1,d2):
	"""
	is one number a perm of the other?
	"""
	sd1, sd2 = str(d1), str(d2)
	return Counter(sd1) == Counter(sd2)

phi_perms = []

for n in xrange(2, len(PRIME_FACTS)):
	phi_n = phi(n)
	if is_perm(n,phi_n):
		phi_perms.append((n,phi_n))

print min(phi_perms, key=lambda np: 1.*np[0]/np[1])[0]



