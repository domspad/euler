
# 85 mins
# running time? estimate...

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
	# Wall time: 11.7 s

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
		else:
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

PRIME_FACTS = prime_fact_upto(1000000)
	# Wall time: 25min 7s

from itertools import product, ifilter

def pf_to_divs(pf):
	"""
	give all proper divisors, given a prime factorization
	{p:num, 2:2, 3:4} --> []
	"""
	items = pf.items()
													# QUESTION is order of iter from dict ALWAYS the same?
	iter_exp = product(*(xrange(a+1) for _,a in items))
	divs = []
	for exp in iter_exp:
		total = 1
		for i, a in enumerate(exp):
			total *= items[i][0]**a
		divs.append(total)
	#pop last total because it is not proper
	divs.pop()
	return divs


# sanity check
assert sum(pf_to_divs(PRIME_FACTS[28])) == 28


MAPP = map(lambda pf: sum(pf_to_divs(pf)), PRIME_FACTS)
	# Wall time: 24.1 s


MEMO_F = {0:0, 1:0}

def amicable_chain_length(n):
	"""
	n >= 0
	28 --> 28 so f(n) == 1, 
	12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 ... so f(12496) == 5
	
	to be considered "amicable chain" it MUST return to its starting point...

	ALSO updates MEMO
	"""

	if n in MEMO_F:
		return MEMO_F[n]
	else:
		chain = [n]
		set_chain = set([n])
		iter_n = MAPP[n]
		while iter_n not in set_chain:
			# print iter_n
			set_chain.add(iter_n)
			chain.append(iter_n)
			if iter_n > 1000000: #exceeds bounds of MAPP
				MEMO_F[n] = -1
				return -1
			iter_n = MAPP[iter_n]
		if iter_n == n: # is amicable chain
			chain_len = len(chain)
			for c in chain:
				MEMO_F[c] = chain_len
		else:
			chain_len = -1
			MEMO_F[n] = chain_len
		return chain_len
			# return -1  # is not amicable chain, because doesnt return to starting point
		#update MEMO_F	
		# print chain + [iter_n]
		# print set_chain
		for c in chain:
			MEMO_F[c] = chain_len


for i in xrange(1000000):
	amicable_chain_length(i)
	# Wall time: 7.66 s


maxx = 28
maxx_v = 1
for k in MEMO_F:
	if MEMO_F[k] > maxx_v:
		maxx, maxx_v = k, MEMO_F[k]

print maxx
	 # Wall time: 232 ms

# Too long to use bag with all subsets because <10000 longest bag is 13 --> 2^13 subsets...f
	# from collections_extended import bag
	# pf_bags = map(lambda pf: bag(k for k in pf for i in xrange(pf[k])),  PRIME_FACTS)
