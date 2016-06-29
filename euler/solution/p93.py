
# 73 mins
# In [172]: %time %run p93.py
# (1, 2, 5, 8)
# CPU times: user 2.28 s, sys: 36.9 ms, total: 2.32 s
# Wall time: 2.33 s


from operator import mul, add, sub
from itertools import combinations, product, permutations
from collections import defaultdict

def div(a,b):
	return float(a)/b

OPS = (mul, add, sub, div)
POSSIBLE_VALS = defaultdict(set)

for combo in permutations(xrange(10), 4):
	for ops in product(OPS,OPS,OPS):
		#hard code the 5 unique orders?!
		op1,op2,op3 = ops
		a,b,c,d = combo
		scombo = tuple(sorted(combo))
		try:
			POSSIBLE_VALS[scombo].add(op3(op2(op1(a,b),c),d))
		except ZeroDivisionError:
			# print ops, combo, 0
			pass
		try:
			POSSIBLE_VALS[scombo].add(op3(op1(a,op2(b,c)),d))
		except ZeroDivisionError:
			# print ops, combo, 1
			pass
		try:
			POSSIBLE_VALS[scombo].add(op2(op1(a,b),op3(c,d)))
		except ZeroDivisionError:
			# print ops, combo, 2
			pass
		try:
			POSSIBLE_VALS[scombo].add(op1(a,op3(op2(b,c),d)))
		except ZeroDivisionError:
			# print ops, combo, 3
			pass
		try:
			POSSIBLE_VALS[scombo].add(op1(a,op2(b,op3(c,d))))
		except ZeroDivisionError:
			# print ops, combo, 4
			pass

#NOW HAVE ALL
for key in POSSIBLE_VALS:
	POSSIBLE_VALS[key] = set(map(lambda x: int(x), filter(lambda x: x == float(int(x)) and x >= 1, POSSIBLE_VALS[key])))


N_SET = {}
for key in POSSIBLE_VALS:
	i = 1
	ss = POSSIBLE_VALS[key]
	while i in ss:
		i += 1
	N_SET[key] = i

print sorted(N_SET.iteritems(), key=lambda x: x[1],reverse=True)[0][0]
