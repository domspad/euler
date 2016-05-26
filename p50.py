

# 13 mins
# In [50]: time %run p50.py
# 997651
# CPU times: user 11.7 s, sys: 103 ms, total: 11.8 s
# Wall time: 11.9 s




from math import sqrt

def primes_lt3(N):
	"""
	Return all primes less than N > 0 int
	"""
	# test every number less than N/2
	primes = [ i for i in xrange(2,N)
				 if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]

	return primes

BOUND = 10**6
PRIMES = primes_lt3(BOUND)
PRIMES_SET = set(PRIMES)
N = len(PRIMES)
longest = 0
longest_total = 0

for i in xrange(N):
	subsum = 0
	count = 0
	for j in xrange(i,N):
		subsum += PRIMES[j]
		count += 1
		if subsum > BOUND:
			break
		elif subsum in PRIMES_SET and count > longest:
			longest = count
			longest_total = subsum

print longest_total