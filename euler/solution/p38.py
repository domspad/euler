

# 14 minutes
# In [63]: time %run p38.py
# 932718654
# CPU times: user 9.99 ms, sys: 2.87 ms, total: 12.9 ms
# Wall time: 11.4 ms



def is_pandigital(n):
	"""
	is 1-9 pandigital
	"""
	str_n = str(n)
	digs = set(str_n)
	return len(str_n) == 9 and len(digs) == 9 and '0' not in digs


def conc_prod(N,tup):
	"""
	Return the concatenated product of N with tuple of at least one number
	"""
	return int(''.join(map(str, (N*i for i in tup))))

print max(conc_prod(N,(1,2)) for N in xrange(9000,10000) if is_pandigital(conc_prod(N,(1,2))))
# print max(conc_prod(N,(1,2,3)) for N in xrange(900,1000) if is_pandigital(conc_prod(N,(1,2,3))))
# print max(conc_prod(N,(1,2,3,4)) for N in xrange(90,100) if is_pandigital(conc_prod(N,(1,2,3,4))))