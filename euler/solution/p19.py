
#20 minutes for solution
# In [16]: %time %run p19.py
# 171
# CPU times: user 3.02 ms, sys: 1.83 ms, total: 4.86 ms
# Wall time: 3.37 ms

increments = map(int, '31 28 31 30 31 30 31 31 30 31 30 31'.split(' '))

start = 1 # Jan 1st, 1901 was a Tuesday == 1 mod(7)

counts = 0
for i in xrange(1901, 2001):
	if i % 4 == 0 : #no other checks needed for this range
		increments[1] = 29
	else:
		increments[1] = 28
	for ee, inc in enumerate(increments):
		if start == 6:
			counts += 1
		start += inc
		start %= 7

print counts