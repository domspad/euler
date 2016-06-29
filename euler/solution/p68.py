

# In [1]: %time %run p68.py
# 28797161103104548
# CPU times: user 6.97 s, sys: 48.3 ms, total: 7.02 s
# Wall time: 7.09 s

# brute force --- 57 mins in and debugging

# gen all perms of 1, 2, 3..., 10
from itertools import permutations

INDICES = [0,2,4,6]
OUTER_INDICES = [0,3,5,7,9]
STRING_INDICES = map(int, list('012324546768981'))
SOLUTIONS = []


def is_sol(perm):
	"""
	given perm of 1,2,...10 is solution to eqs
	checks constraint that perm[0] is lowest of outer nodes
	"""
	if perm[0] != min(perm[i] for i in OUTER_INDICES):
		return False
	const = perm[8] + perm[9] + perm[0]
	return all( sum(perm[i:i + 3]) == const for i in INDICES)

def gen_str(perm):
	"""
	gen 16-17digit string representation of solution
	"""
	return ''.join(map(str, [perm[i] for i in STRING_INDICES]))


def p68():
	for perm in permutations(xrange(1,11)):
		if is_sol(perm):
			magic_str = gen_str(perm)
			if len(magic_str) == 16:
				SOLUTIONS.append(magic_str)
	return max(map(int, SOLUTIONS))


EQS = map(lambda l: map(int,l),map(list,'056,167,278,389,495'.split(',')))
def is_solution(perm10):
	return len(set(map(lambda inds: sum(perm10[i] for i in inds), EQS))) == 1


STRING_INDEXES = map(int, list('056167278389495'))
def gen_string(perm):
	return int(''.join(map(str, (perm[i] for i in STRING_INDEXES))))

# for perm in permutations(xrange(1,11)):
# 	if min(perm[:5]) == perm[0] and is_solution(perm):
# 		print perm, gen_string(perm)

print max(gen_string(perm) for perm in permutations(xrange(1,11))
							if min(perm[:5]) == perm[0] and is_solution(perm))

