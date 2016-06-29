
M = 2000
#65 mins - brute with pythag solutions
# In [1]: %time %run p86.py
# 1818 1000457
# CPU times: user 30.8 s, sys: 887 ms, total: 31.7 s
# Wall time: 33.9 s


from collections import Counter
import numpy as np

SOLS = set()

A = np.array([[1,-2,2],
			  [2,-1,2],
			  [2,-2,3]])
B = np.array([[1,2,2],
			  [2,1,2],
			  [2,2,3]])
C = np.array([[-1,2,2],
			  [-2,1,2],
			  [-2,2,3]])

def prim_pyth_sol_ltN(M):
	"""
	yield all (a,b,c) primitive pythag triples s.t. a,b<= 2*M
	N >= 12
	"""
	stack = [np.array((3,4,5))]
	while stack:
		x = stack.pop()
		ext = filter(lambda y: y[0] <= 2*M and y[1] <= 2*M , [A.dot(x), B.dot(x), C.dot(x)])
		stack.extend(ext)
		yield x

def pyth_sol_ltN(M):
	"""
	yield all (a,b,c) pythag triples s.t. a,b <= 2*M
	N >= 12
	"""
	for prim_sol in prim_pyth_sol_ltN(M):
		k = 2
		sol = prim_sol
		while sol[0] <= 2*M and sol[1] <= 2*M:
			yield sol
			sol = prim_sol* k
			k += 1

def partition(n):
	"""
	6 --> (1,5), (2,4), (3,3)
	7 --> (1,6), (2,5), (3,4)
	"""
	return [(x,n-x) for x in xrange(1,n/2 + 1)]


sol_count = Counter()

for pyth_sol in pyth_sol_ltN(M):
	a,b,_ = pyth_sol

	# x+y =a , z = b
	for x,y in partition(a):
		z = b
		if x <= z and y <= z and (x,y,z) not in SOLS:
			# print x,y,z
			SOLS.add((x,y,z))
			sol_count[z] += 1

	# x+y = b, z = a
	for x,y in partition(b):
		z = a
		if x <= z and y <= z and (x,y,z) not in SOLS:
			SOLS.add((x,y,z))
			# print x,y,z
			sol_count[z] += 1

totals = [ sum(sol_count[i] for i in xrange(n) ) for n in xrange(1,M)]
for e,i in enumerate(totals):
	if i > 1000000:
		print e,i
		break

# roughly 25 mins to get sol counts up to 200,000, 
# I'd estimate a couple hours for 2,000,000..

from collections import Counter
# sol_count = Counter()

from math import sqrt

def is_square(n):
	return n == int(sqrt(n))**2

def is_sol(x,y,z):
	"""
	1 <= x <= y <= z ints
	"""
	return is_square((x+y)**2 + z**2)



# for x in xrange(1,M):
# 	for y in xrange(x,M):
# 		for z in xrange(y,M):
# 			if is_sol(x,y,z):
# 				sol_count[z] += 1



#