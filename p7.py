
# BRUTE Force - alg from p3...
# In [35]: %time p7()
# 10 0
# 20 8
# 40 12
# 80 22
# 160 37
# 320 66
# 640 115
# 1280 207
# 2560 375
# 5120 685
# 10240 1254
# 20480 2312
# 40960 4288
# 81920 8009
# CPU times: user 1.05 s, sys: 24.2 ms, total: 1.07 s
# Wall time: 1.1 s
# Out[35]: 104743

from math import sqrt


def extend_primes(N, primes=None):
	"""
	Return all primes less than N > 0 int
	"""
	if primes is None or len(primes) == 0:
		# test every number less than N/2
		primes = [ i for i in xrange(2,N)
					 if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]

		return primes

	else:
		start = primes[-1] + 1

		more_primes = [ i for i in xrange(start,N)
					   if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]
		primes.extend(more_primes)
		return primes




def p7():
	primes = []
	N = 10
	while len(primes) < 10001:
		print N, len(primes)
		N *= 2
		primes = extend_primes(N, primes=primes)
	return primes[10000]