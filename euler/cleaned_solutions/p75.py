
# 90 mins (+30 for new solution)
# USE Primitive Pythag triple generators to SMART brute force solution
	# (only 1256149 SOLUTIONS to loop over!)
# In [87]: %time %run p75.py
# 161667
# CPU times: user 17.2 s, sys: 201 ms, total: 17.4 s
# Wall time: 17.8 s


import numpy as np
L = 1500000
A = np.array([[1,-2,2],
			  [2,-1,2],
			  [2,-2,3]])
B = np.array([[1,2,2],
			  [2,1,2],
			  [2,2,3]])
C = np.array([[-1,2,2],
			  [-2,1,2],
			  [-2,2,3]])

def prim_pyth_sol_ltN(N):
	"""
	yield all (a,b,c) primitive pythag triples s.t. a+b+c <= N
	N >= 12
	"""
	stack = [np.array((3,4,5))]
	while stack:
		x = stack.pop()
		ext = filter(lambda y: y.sum() <= N, [A.dot(x), B.dot(x), C.dot(x)])
		stack.extend(ext)
		yield x

def pyth_sol_ltN(N):
	"""
	yield all (a,b,c) pythag triples s.t. a+b+c <= N
	N >= 12
	"""
	for prim_sol in prim_pyth_sol_ltN(N):
		k = 2
		sol = prim_sol
		L = sol.sum()
		while L <= N:
			yield L
			sol = prim_sol* k
			k += 1
			L = sol.sum()

from collections import Counter
c = Counter(pyth_sol_ltN(L))
print sum(1 for k in c if c[k] == 1)


#### OLD BRUTE SOLUTION --- prob 8 hours to finish


#8:10 ~ 1 hour in

# SQUARES = [ n**2 for n in xrange(15000)]
# SQUARES_SET = set(SQUARES)
# LOOKS LIKE n^2 for even smart brute :(
# 1500 		0.03 s
# 15000		3.00 s
# 150000	300	 s
# 1500000	30000 s = 8 hrs?
L = 1500000
LL = L**2

from collections import Counter
from itertools import combinations
from math import sqrt 

def is_square(n):
	return int(sqrt(n))**2 == n

def biggest_b(a):
	return ((LL - 2*L*a)/(2*(L-a)))

# triangle = Counter()


# will probly take a day...
# for a in xrange(L/6,L/3):
# 	aa = a**2
# 	# print a
# 	for b in xrange(a,biggest_b(a)):
# 		if is_square(aa + b**2):
# 			triangle[a+b] += 1

# sum(len(xrange(a,biggest_b(a))) for a in xrange(1,L/3)) #~ 100 billion!
