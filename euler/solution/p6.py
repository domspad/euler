

# In [3]: %time p6() 	1 min
# CPU times: user 40 µs, sys: 17 µs, total: 57 µs
# Wall time: 47.9 µs
# Out[3]: 25164150

def p6():
	return sum(xrange(101)) ** 2 - sum( i**2 for i in xrange(101))