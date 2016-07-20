
# 25 mins (wiht sympy)
# In [43]: %time %run p101.py
# 37076114526
# CPU times: user 120 ms, sys: 5.69 ms, total: 125 ms
# Wall time: 132 ms

from sympy.abc import x
from sympy import interpolate

def f(n):
	return sum( (-n)**i for i in xrange(11))

def optimal_poly(values):
	"""
	given [1,8,27] 
		assume F(1) ==  1,
			   F(2) ==  8,
			   F(3) ==  27
	find "minimal polynomial" that generates given sequence of values
	"""
	pdict = {'p':interpolate(values,x)}
	def poly(n):
		return pdict['p'].subs({'x':n})
	return poly


# assuming that FITs persist until degree of interpolated degree matches ideal
DEGREE = 10
FITs = []
for d in xrange(DEGREE):
	seq = [f(n) for n in xrange(1,d+2)]
	# get OP
	p = optimal_poly(seq)
	# find FIT and append to list
	n = 1
	while True:
		if f(n) != p(n):
			FITs.append(p(n))
			break
		n += 1

print sum(FITs)