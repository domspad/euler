# compile using `python setup_cyp100.py build_ext --inplace`
# then can import like any other python module!
# runs about 1 million every 0.25 sec ~10x faster
# MAKE SURE YOU ARE IN 'SCIENTIFIC' workenv when compiling! else gcc failure!


from math import sqrt 
from time import time

# 			521.260391951 			2147000000
			# 521.460042 			-2147000000


# Roughly 0.2 sec per 1,000,000! --> 25 X speedup!
# 								 --> 0.2 * (70bill/1mill) == 3.8 hours!
			# 0.201745033264 			1030001000000
			# 0.178977966309 			1030002000000
			# 0.195358037949 			1030003000000
			# 0.193830966949 			1030004000000
			# 0.202977895737 			1030005000000
			# 0.195896148682 			1030006000000
			# 0.209393024445 			1030007000000
			# 0.190097808838 			1030008000000
			# 0.20233297348 			1030009000000
			# 0.192817926407 			1030010000000

def check(long long int m):
	cdef long long int b, r
	b = int(m / sqrt(2)) + 1
	r = m - b
	return b**2 - b - 2*b*r - r**2 +r == 0

def p100():
	cdef long long int m
	cdef double st
	m = 10 ** 12 + (3 * (10 ** 10))
	st = time()
	while True:
		if check(m):
			return m
		if m % 1000000 == 0:
			print '\t\t\t', time() - st, '\t\t\t',m
			st = time()
		m += 1