
# smart brute -- 36 mins
# In [29]: %time %run p109.py
# 38182
# CPU times: user 7.11 ms, sys: 2.73 ms, total: 9.84 ms
# Wall time: 8.07 ms

from itertools import combinations
from collections import defaultdict


singles = zip(['S{}'.format(i) for i in xrange(1,21)],xrange(1,21)) + [('S25',25)]
doubles = zip(['D{}'.format(i) for i in xrange(1,21)],xrange(2,42,2)) + [('D25',50)]
triples = zip(['T{}'.format(i) for i in xrange(1,21)],xrange(3,63,3))

BOARD = dict(singles+doubles+triples)

COUNTS_WITH_TWO_OR_LESS_DARTS = defaultdict(int)

for v in BOARD.values():
	COUNTS_WITH_TWO_OR_LESS_DARTS[v] += 1

from itertools import combinations_with_replacement

for k1,k2 in combinations_with_replacement(BOARD,2):
	COUNTS_WITH_TWO_OR_LESS_DARTS[BOARD[k1] + BOARD[k2]] += 1

# add 0!
COUNTS_WITH_TWO_OR_LESS_DARTS[0] += 1

def num_checkouts(N):
	"""
	1 < N < 171 is integer
	"""
	if N < 2 or N > 170:
		return 0
	else:
		# count up num ways using each possible double
		subt_doubles = filter(lambda x: x >= 0, [N - value for reg,value in doubles])
		
		total = sum(COUNTS_WITH_TWO_OR_LESS_DARTS[n] for n in subt_doubles)

	return total


assert sum(num_checkouts(n) for n in xrange(2,171)) == 42336

def p109():
	return sum(num_checkouts(n) for n in xrange(100))

print p109()