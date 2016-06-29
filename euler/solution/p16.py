

# jeeze brute force...(4 mins)
# In [1]: %time %run p16
# 1366
# CPU times: user 2.12 ms, sys: 655 µs, total: 2.77 ms
# Wall time: 1.98 ms

def p16():
	return reduce(lambda x, y: int(x) + int(y), str(2 ** 1000), 0)

print p16()