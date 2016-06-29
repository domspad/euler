

# brute force 14 mins
# In [4]: %time %run p9.py
# 200 375 425 31875000
# CPU times: user 222 ms, sys: 7.42 ms, total: 229 ms
# Wall time: 229 ms

def is_solution(a,b):
	return (a*b - 1000*a - 1000*b + 500000) == 0


for a in xrange(1,1000):
	for b in xrange(a,1000):
		if is_solution(a,b):
			print a, b, 1000 - a - b, a*b*(1000 - a - b)
