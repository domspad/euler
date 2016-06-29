
# 16 mins
# In [10]: %time %run p92.py
# 8581146
# CPU times: user 1min 23s, sys: 925 ms, total: 1min 24s
# Wall time: 1min 25s



def sq_dig(n):
	"""
	n --> sum of digit squares
	"""
	str_n = str(n)
	return sum(map(lambda x: int(x)**2, str_n))

def end_point(n):
	iter_n = n
	while iter_n != 1 and iter_n != 89:
		iter_n = sq_dig(iter_n)
	return iter_n


FIRST_THOU = {1:set(),89:set()}


for i in xrange(1,1000):
	FIRST_THOU[end_point(i)].add(i)

for i in xrange(1000,10000000):
	bel_1000 = sq_dig(i)
	if bel_1000 in FIRST_THOU[1]:
		FIRST_THOU[1].add(i)
	else:
		FIRST_THOU[89].add(i)

print len(FIRST_THOU[89])