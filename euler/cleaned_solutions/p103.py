
# In [77]: %time %run p103.py
# 255 20313839404245
# CPU times: user 10.5 s, sys: 70.3 ms, total: 10.6 s
# Wall time: 10.7 s


A = set((2,3,4))

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


UB = (20, 31, 38, 39, 40, 42, 45)
U1,U2,U3,U4,U5,U6,U7 = UB

def iter_sets():
	for a1 in xrange(20,U1+1):
		for a2 in xrange(a1+1,U2+1):
			for a3 in xrange(a2+1, U3+1):
				for a4 in xrange(a3+1, U4+1):
					for a5 in xrange(a4+1, U5+1):
						for a6 in xrange(a5+1, U6+1):
							for a7 in xrange(a6+1, U7+1):
								yield set((a1,a2,a3,a4,a5,a6,a7))

# ASSUME lowest element WILL BE 20
for cand in iter_sets():
	if is_special_subset(cand):
		print sum(cand), ''.join(map(str,sorted(cand)))

