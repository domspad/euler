
# brute with bad divisors (12 mins, but didnt' wait to finish running)
# ?
# ?
# ?

# brute with sqrt divisors imp (5 mins total)
# In [5]: %time %run p12.py
# 76576500
# CPU times: user 5.26 s, sys: 34 ms, total: 5.29 s
# Wall time: 5.31 s



from math import sqrt
def divisors(n):
	"""
	return all divisors of n (including 1,n)
	"""
	upper = int(sqrt(n)) + 1
	ll = []
	for i in xrange(1, upper):
		if n % i == 0:
			ll.extend([i, n/i ])
	return ll
	# return [i for i in xrange(1,n/2 + 1)
	#           if n % i == 0] + [n]



inc = 2
tn = 1
while True:
	if len(divisors(tn)) > 500:
		print tn
		break
	tn += inc
	inc += 1
