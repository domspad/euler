

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

