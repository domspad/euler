
#~90 mins before running + 60 mins running? need to run again...
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

# PRIME_FACTS = prime_fact_upto(30)

from itertools import combinations
from collections_extended import bag,frozenbag
from collections import defaultdict

N = 12500

#from http://stackoverflow.com/questions/19368375/set-partitions-in-python
def partition(collection):
    if len(collection) == 1:
        yield [ collection ]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        # put `first` in its own subset 
        yield [ [ first ] ] + smaller

def trans_pf_dict_to_bag(pf_dict):
	return sum(([k]*pf_dict[k] for k in pf_dict),[])

def calc_k(bag):
	prod = reduce(lambda x,y: x*y, bag, 1)
	return prod - sum(bag) + len(bag)



found_ks = defaultdict(int)
FOUND_KS = set()

for e,pf in enumerate(prime_fact_upto(N)):
	if e < 2:
		continue
	if e % 100 == 0:
		print e
partitions = partition(trans_pf_dict_to_bag(pf))
bags = set(frozenbag(map(lambda x: reduce(lambda y,z: y*z, x, 1), p)) for p in partitions)
for k in map(calc_k, bags):
	FOUND_KS.add(k)
	if found_ks[k] == 0:
		found_ks[k] = e

print sum(set((found_ks[i] for i in xrange(2,12001))))

########################################################################

#dp method?
N = 100
K = N/2

# prod_partitions = [[(,)]*K for i in xrange(N)]




