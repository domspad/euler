

# 15 mins restricted brute
# In [24]: %time %run p32.py
# 45228
# CPU times: user 751 ms, sys: 41.8 ms, total: 793 ms
# Wall time: 788 ms

# 2* 10**5
	# for a in xrange(10):
	# 	for b in xrange(10**4)
	# for a in xrange(100):
	# 	for b in xrange(1000)
# _ * 10 because loop through digits and averege length ~10 chars
# TOTAL = 2000000

prods = []

def is_pan_dig(a,b):
	ab = a*b
	return ''.join(sorted(''.join(map(str, (a,b,ab))))) == '123456789'

for a in xrange(10):
	for b in xrange(10**4):
		if is_pan_dig(a,b):
			print a, b, a*b
			prods.append(a*b)

for a in xrange(100):
	for b in xrange(1000):
		if is_pan_dig(a,b):
			print a, b, a*b
			prods.append(a*b)

print sum(set(prods))