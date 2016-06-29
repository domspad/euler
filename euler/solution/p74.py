
#14 mins
# In [14]: %time %run p74.py
# 402
# CPU times: user 2min 44s, sys: 927 ms, total: 2min 45s
# Wall time: 2min 49s

from math import factorial

# FACT_MAP = {}



def fact_dig_sum(n):
	return sum(factorial(int(i)) for i in str(n))

def fact_chain_length(n):
	"""
	returns length of chain 169 --> 1451 --> ... --> (something in chain)
	"""
	next_n = n
	chain = set()
	while next_n not in chain:
		chain.add(next_n)
		next_n = fact_dig_sum(next_n)
	return len(chain)


print sum(1 for i in xrange(1000000) if fact_chain_length(i) == 60)