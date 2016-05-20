

# 11:45



# 15 mins, (using primes_lt3 from p10)
# In [41]: time %run p35.py
# CPU times: user 12.3 s, sys: 100 ms, total: 12.4 s
# Wall time: 12.6 s

from math import sqrt

def primes_lt3(N):
	"""
	Return all primes less than N > 0 int
	"""
	# test every number less than N/2
	primes = [ i for i in xrange(2,N)
				 if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]

	return primes

PRIMES = set(primes_lt3(1000000))

CIRCULAR = set()

def get_circles(num):
	"""
	get all circular shifts of num
	"""
	str_num = str(num)
	str_circs = [str_num[-i:] + str_num[:-i] for i in xrange(1,len(str_num)+1)]
	return map(lambda x: int(x.lstrip('0')), str_circs)

	#careful with 0!

for prime in PRIMES:
	if prime in CIRCULAR:
		continue
	else:
		circles = get_circles(prime)
		if all(circle in PRIMES for circle in circles):
			CIRCULAR.update(circles)


print len(CIRCULAR)
