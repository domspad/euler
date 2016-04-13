

# brute force - (from p3) 20 mins to answer
# In [31]: %time sum(primes_lt3(2000000))
# CPU times: user 30.5 s, sys: 122 ms, total: 30.6 s
# Wall time: 31.1 s
# Out[31]: 142913828922

# trying to be smart using primes instead... MUCH SLOWER than list comps!
# In [29]: %time sum(primes_lt(2000000))
# CPU times: user 24min 13s, sys: 8.64 s, total: 24min 22s
# Wall time: 24min 44s
# Out[29]: 142913828922

from math import sqrt

def primes_lt3(N):
	"""
	Return all primes less than N > 0 int
	"""
	# test every number less than N/2
	primes = [ i for i in xrange(2,N)
				 if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]

	return primes

def p4():
	return sum(primes_lt3(2000000))

def primes_lt(N):
	"""
	Return all primes less than N > 0 int
	"""
	primes = []

	# test every number less than N/2
	for i in xrange(2, N):
		if any( ( i % p == 0 for p in primes ) ):
			pass
		else:
			primes.append(i)

	return primes

def primes_lt2(N):
	"""
	Return all primes less than N > 0 int
	"""
	primes = []

	# test every number less than N/2
	primes = [ i for i in xrange(2,N)
				 if not any( ( i % p == 0 for p in xrange(2,i/2) ) )]

	return primes

#(not faster for list comprehension b/c cant reference itself!)
# In [11]: %time a = primes_lt(10000)
# CPU times: user 131 ms, sys: 9.64 ms, total: 141 ms
# Wall time: 137 ms

# In [12]: %time a = primes_lt2(10000)
# CPU times: user 862 ms, sys: 8.1 ms, total: 870 ms
# Wall time: 871 ms



# FINALLY FASTER THAN FIRST!
# In [29]: %time a = primes_lt3(100000)
# CPU times: user 569 ms, sys: 15.2 ms, total: 584 ms
# Wall time: 580 ms

# In [30]: %time a = primes_lt(100000)
# CPU times: user 6.79 s, sys: 46.5 ms, total: 6.83 s
# Wall time: 6.9 s


