
# brute force and not carful
# # 12 mins to answer
# In [3]: %time p52()
# CPU times: user 526 ms, sys: 21.3 ms, total: 548 ms
# Wall time: 538 ms
# Out[3]: 142857

def check_digits(a,b):
	"""
	checks if a,b have same digits (and same number of times)
	"""
	if len(str(a)) != len(str(b)):
		return False
	else:
		return set(str(a)) == set(str(b))

def check_p52(a):
	"""
	checks if a, 2a,...,6a all have same digits
	"""
	return all(check_digits(a, i*a) for i in xrange(2,7))

from time import time
def p52():
	n = 1
	st = time()
	while not check_p52(n):
		n += 1
		if n % 1000000 == 0:
			print n
	return n