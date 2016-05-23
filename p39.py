

# 12 minutes
# In [80]: time %run p39.py
# [(840, 16)]
# CPU times: user 237 ms, sys: 23.8 ms, total: 261 ms
# Wall time: 296 ms

def eq(a,b,p):
	return p*(2*a + 2*b - p) == 2*a*b

def bb(a,p):
	return (p**2 - 2*p*a)/(2*(p-a))

from collections import Counter

def p39():
	c = Counter()
	for p in xrange(1,1000):
		for a in xrange(1,p/2):
			if eq(a,bb(a,p),p):
				c[p] +=1
	print c.most_common(1)

p39()