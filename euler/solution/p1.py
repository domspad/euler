
# brute 1 minute
# CPU times: user 920 µs, sys: 429 µs, total: 1.35 ms
# Wall time: 1.08 ms
# Out[5]: 233168

def p1():
	return sum( filter( lambda x: x % 5 == 0 or x % 3 == 0, xrange(1000)))