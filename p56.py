
# 2 mins
# In [7]: time %run p56.py
# 972
# CPU times: user 662 ms, sys: 12 ms, total: 674 ms
# Wall time: 674 ms

def digit_sum(n):
	return sum(int(d) for d in str(n))	

print max(digit_sum(a**b) for a in xrange(100) for b in xrange(100))