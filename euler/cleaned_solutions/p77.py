

# 14 mins dynamic prog
# In [52]: %time  %run p77.py
# 71
# CPU times: user 3.4 ms, sys: 3.45 ms, total: 6.86 ms
# Wall time: 12 ms#

#In [210]: sum(sqrt(i) for i in xrange(100))
# Out[210]: 661.4629471031477
# In [214]: sum(len(dp_array[i]) for i in xrange(len(dp_array)))
# Out[214]: 2600
	# dp_array dims
#total = sum = 3200
	# do list index accessing grow with len? NO?

			# In [216]: aa = range(1000000)

			# In [217]: %time aa[300000]
			# CPU times: user 5 µs, sys: 1e+03 ns, total: 6 µs
			# Wall time: 12.2 µs
			# Out[217]: 300000

			# In [218]: %time aa[len(aa)/2]
			# CPU times: user 11 µs, sys: 14 µs, total: 25 µs
			# Wall time: 13.8 µs
			# Out[218]: 500000

			# In [219]: aaa = range(10000000)

			# In [220]: %time aaa[len(aaa)/2]
			# CPU times: user 10 µs, sys: 1e+03 ns, total: 11 µs
			# Wall time: 16.9 µs
			# Out[220]: 5000000

			# In [225]: aaaa = range(1000)

			# In [226]: %time aaaa[len(aaaa)/2]
			# CPU times: user 10 µs, sys: 3 µs, total: 13 µs
			# Wall time: 19.8 µs
			# Out[226]: 500


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