


# 6 mins (already solved with p103)
# 73702
# CPU times: user 1.1 s, sys: 24.9 ms, total: 1.13 s
# Wall time: 1.17 s



from itertools import combinations
import time

# with this brute check -- roughly <3ms per run on TRUE set with 7 elements
def is_special_subset(A):
	"""
	REQ: A non-empty collection of positive ints
	THEN:
		true if for all non-empty disjoint B,C subsets of A
			1) S(B) != S(C)
			2) if |B| > |C|, then S(B) > S(C)
	"""
	st = time.time()
	card_a = len(A)
	for card_b in xrange(1,card_a):
		for B in combinations(A, card_b):
			s_b = sum(B)
			A_B = A - set(B)
			card_a_b = len(A_B)
			for card_c in xrange(1, min(card_b + 1, card_a_b + 1)): # all nonempty subsets C with |C| <= |B|
				for C in combinations(A_B, card_c):
					s_c = sum(C)
					if (card_b > card_c and s_b <= s_c) or s_b == s_c:
						# print time.time() - st
						return False
	# print time.time() - st
	return True


def parse_set(line):
	return set(map(int,line.split(',')))

with open('p105_sets.txt','r') as f:
	sets = [parse_set(line) for line in f]


total = 0
for e, sett in enumerate(sets):
	# print 'running {}'.format(e)
	if is_special_subset(sett):
		total += sum(sett)

print total