# compile using `python setup_cyp100.py build_ext --inplace`
# then can import like any other python module!
# runs about 1 million every 0.25 sec ~10x faster

from math import sqrt 
from time import time

# 			521.260391951 			2147000000
			# 521.460042 			-2147000000

def check(long long int m):
	cdef long long int b, r
	b = int(m / sqrt(2)) + 1
	r = m - b
	return b**2 - b - 2*b*r - r**2 +r == 0

def check_from():
	cdef long long int m
	cdef double st
	m = 3
	st = time()
	while m < 10 ** 12:
		if check(m):
			print m
		if m % 1000000 == 0:
			print '\t\t\t', time() - st, '\t\t\t',m
		m += 1