

# brute 40 mins
# In [42]: %time %run p106.py
# 21384
# CPU times: user 295 ms, sys: 5.07 ms, total: 300 ms
# Wall time: 298 ms



from itertools import combinations


def pair_needs_check(A,B):
	"""
	REQ: A,B collections of numbers with equal number of DISTINCT elements
	RET: false if "pairing" exists between elements of A,B
	"""
	# find set with minimum element
	min_el = min(min(A),min(B))
	if min_el in B:
		A,B = B,A

	return not all( a < b for (a,b) in zip(sorted(A),sorted(B)))

N = 12
ks = xrange(2,(N/2) + 1)
c = 0
for k in ks:
	for A in combinations(range(N),k):
		remaining = set(range(N)) - set(A)
		for B in combinations(remaining,k):
			if pair_needs_check(A,B):
				c += 1

print c/2 #(double counts all pairs)




# 
# analysis functions
# 
"""import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def num_equal_subset_pairs(N):
	return sum( (nCr(N,k)*nCr(N-k,k))/2 for k in xrange(2,(N/2)+1))
"""