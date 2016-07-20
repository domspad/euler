

# brute force - (from p3) 20 mins to answer
# In [31]: %time sum(primes_lt3(2000000))
# CPU times: user 30.5 s, sys: 122 ms, total: 30.6 s
# Wall time: 31.1 s
# Out[31]: 142913828922


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
