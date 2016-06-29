

# 3 mins
# In [1]: time %run p53.py
# 4075
# CPU times: user 61.8 ms, sys: 5.67 ms, total: 67.5 ms
# Wall time: 64.7 ms

from math import factorial

def choose(n,k):
	return (factorial(n)/(factorial(n-k)*factorial(k)))


print sum([1 for n in xrange(1,101) for k in xrange(n+1) if choose(n,k) > 1000000])
