

# 1hr 15 mins (2nd solution faster)
	# tho first solution could be modified to check periodically and would've stopped MUCH sooner because next prime is feasible
# In [1]: time %run p51.py
# *2*3*3
# CPU times: user 13.4 s, sys: 154 ms, total: 13.6 s
# Wall time: 15.2 s

from math import sqrt
from time import time

def primes_lt3(N):
	"""
	Return all primes less than N > 0 int
	"""
	# test every number less than N/2
	primes = [ i for i in xrange(2,N)
				 if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]

	return primes


####### O(N) testing
PRIMES = filter(lambda x: x > 100000,primes_lt3(1000000))
PRIMES_SET = set(PRIMES)

def pattern_gen(num):
	"""
	561131 --> [*61131, 5*1131, 56**3*, 5611*1]

	"""
	str_num = str(num)
	digs = set(str_num)
	return [str_num.replace(d,'*') for d in digs]

def test_pattern(pattern):
	"""
	returns number of variations of pattern that are prime
	e.g. '*3' == 6
	"""
	start = 1 if pattern[0] == '*' else 0
	c = 0
	for d in xrange(start,10):
		if int(pattern.replace('*',str(d))) in PRIMES_SET:
			c += 1
	return c


def p51():
	TRIED_PATTERNS = set()
	start = time()
	t = float(len(PRIMES))
	for i,p in enumerate(PRIMES):
		if i % 10000 == 0:
			print i/t, time() - start
			start = time()
		for pattern in pattern_gen(p):
			if pattern in TRIED_PATTERNS or pattern[-1] == '*':
				continue
			else:
				TRIED_PATTERNS.add(pattern)
				if test_pattern(pattern) == 8:
					print pattern
					return

p51()

# SOlution attempt 1 - testing all pairs of primes O(N^2) -- est time to completion 3.5 hours :(
#

def p51_2():
	PRIMES = filter(lambda x: x > 100000,primes_lt3(1000000))

	def differ_pattern(n1,n2):
		"""
		n1!=n2 integers and same number of digits
		returns differ pattern if differs by only one pair of digits
		"""
		str_n1, str_n2 = str(n1), str(n2)

		if len(str_n1) != len(str_n2):
			return None

		differ_pattern = ''
		differ_digits = None
		for d1,d2 in zip(str_n1,str_n2):
			if d1 != d2:
				if differ_digits is not None:
					if (d1,d2) == differ_digits:
						differ_pattern += '*'
					else:
						return None
				else:
					differ_digits = (d1,d2)
					differ_pattern += '*'
			else:
				differ_pattern += d1
		return differ_pattern

	assert(differ_pattern(561131, 564434) == '56**3*')

	from collections import defaultdict
	from time import time

	# return first pattern to have a count of 8
	# iterate through all pairs of primes
	dd = defaultdict(set)
	start = time()
	t = float(len(PRIMES))
	for i,p1 in enumerate(PRIMES):
		if i % 100 == 0:
			print i/t, time() - start
			start = time()
		for p2 in PRIMES[i+1:]:
			dp = differ_pattern(p1,p2)
			if dp is not None:
				dd[dp].update((p1,p2))

	s = sorted(dd.items(),key=lambda x:len(x[1]), reverse=True)

