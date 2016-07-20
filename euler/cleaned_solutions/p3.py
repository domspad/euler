 # -*- coding: utf-8 -*-

NUM = 600851475143

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


def prime_factorization(N):
	"""
	Return \{prime: alpha\} for prime fact of N > 2 int.
	"""
	factorization = {}
	for p in primes_lt(N/2):
		divides_c = times_divides_N(p,N)
		if divides_c != 0:
			factorization[p] = divides_c
	return factorization


def times_divides_N(n,N):
	"""
	Return number of times n (<N) divides N.
	"""
	c = 0
	while N % n == 0:
		N /= n
		c += 1
	return c

# MINUTES PASSING!

def p3(N):
	"""
	Return largest prime factor of N
	"""
	return max(prime_factorization(N).keys())

######
###### recursive?


# recursively construct prime factorization of N via find prime facts(a), prime facts(b) (a,b) 
from collections import Counter
def prime_facts(N):
	"""
	return prime facts of N as list
	"""
	def rec_get_divisors(M, start=2):
		"""
		return 
		"""
		for i in xrange(start,M/2):
			if M % i == 0:
				# smallest non-1 divisor of M MUST be prime
				return [i] + rec_get_divisors(M/i, start=i)
		# no divisors, must be prime itself!
		return [M]
	return Counter(rec_get_divisors(N))

def p3_rec(N):
	return max(prime_facts(N).keys())

print p3_rec(NUM)
# In [62]: %time p3_rec(NUM)
# CPU times: user 694 µs, sys: 194 µs, total: 888 µs
# Wall time: 719 µs
# Out[62]: 6857

# range(d-digits) == 10 ^ (d - 8) secs
	# N = thousand		10 µs
	# N = million		10 ms
	# N = billion		10 s
	# N = trillion		10,000 s == 160 mins == 3 hrs

	# range begins to choke (nonlinear increase due to memory?) around billion
		# million 		8 MB
		# 10 million 	80 MB
		# 100			800 MB
		# billion 		8 GB

		# In [8]: getsizeof(range(100 000 000))
		# Out[8]: 800000072

		# In [9]: getsizeof(range(1000000000)) 		#CHUGGGGGGING
		# Out[9]: 8000000072
													# and memory is still REALLY HIGH? (wasnt assigned... why not destroyed?)
		# In [10]: 
		# Do you really want to exit ([y]/n)? y 	# TAKES about 2 mins  

 	# WHY xrange is better

 		# In [1]: %time for i in xrange(1000000): pass
 		# CPU times: user 67 ms, sys: 5.25 ms, total: 72.3 ms
 		# Wall time: 68.8 ms

 		# In [2]: %time for i in xrange(10000000): pass
 		# CPU times: user 513 ms, sys: 8.44 ms, total: 522 ms
 		# Wall time: 520 ms

 		# In [3]: %time for i in xrange(100000000): pass
 		# CPU times: user 5.56 s, sys: 26.6 ms, total: 5.59 s
 		# Wall time: 5.61 s

 		# In [4]: %time for i in xrange(1000000000): pass
 		# CPU times: user 53 s, sys: 119 ms, total: 53.1 s
 		# Wall time: 53.2 s

 		# In [5]: from sys import getsizeof

 		# In [6]: getsizeof(xrange(1000000))
 		# Out[6]: 40

 		# In [7]: getsizeof(xrange(10000000))
 		# Out[7]: 40

 		# In [8]: getsizeof(xrange(100000000))
 		# Out[8]: 40

 		# In [9]: getsizeof(xrange(1000000000))
 		# Out[9]: 40