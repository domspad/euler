

# 14 mins dynamic prog
# In [52]: %time  %run p77.py
# 71
# CPU times: user 3.4 ms, sys: 3.45 ms, total: 6.86 ms
# Wall time: 12 ms#

from math import sqrt

def primes_lt3(N):
	"""
	Return all primes less than N > 0 int
	"""
	# test every number less than N/2
	primes = [ i for i in xrange(2,N)
				 if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]

	return primes

N = 100
PRIMES = primes_lt3(N)
k = len(PRIMES)

dp_array = [ [0]*(k+1) for i in xrange(N)]

for j in xrange(k+1):
	dp_array[0][j] = 1

def p77():
	for i in xrange(1,N):
		for j in xrange(1,k+1):
			first_term = dp_array[i][j-1]
			second_term = dp_array[i-PRIMES[j-1]][j] if PRIMES[j-1] <= i else 0
			total = first_term + second_term
			if total > 5000:
				return i
			dp_array[i][j] = total

print p77()