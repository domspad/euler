

# BRUte with arb precision arith!
#15 mins
# In [85]: time %run p80.py
# 40886
# CPU times: user 64.6 ms, sys: 5.78 ms, total: 70.4 ms
# Wall time: 75.6 ms


import decimal
from math import sqrt
from decimal import Decimal

decimal.getcontext().prec = 105

def is_square(n):
	return int(sqrt(n))**2 == n

def sum_sq_dig(N):
	"""
	N is > 0 and not square
	"""
	num = Decimal(N) ** Decimal(0.5)
	str_num = str(num).replace('.','')

	return sum(map(int,str_num[:100]))

print sum(sum_sq_dig(N) for N in xrange(1,101) if not is_square(N))
