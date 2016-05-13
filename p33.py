

#18 mins
# In [16]: time %run p33.py
# 0.01
# CPU times: user 24.8 ms, sys: 2.51 ms, total: 27.3 ms
# Wall time: 26.9 ms

def is_cancelling(ab,cd):
	"""
	10 < ab < cd < 100 integers
	if cancelling a digit from ab and cd results in the same value fraction
	"""
	a,b = map(int,str(ab))
	c,d = map(int,str(cd))
	if b == 0 or d == 0:
		return False

	if a == c:
		if 1.*ab/cd == 1.*b/d:
			return True
	elif a == d:
		if 1.*ab/cd == 1.*b/c:
			return True
	elif b == c:
		if 1.*ab/cd == 1.*a/d:
			return True
	elif b == d:
		if 1.*ab/cd == 1.*a/c:
			return True
	else:
		return False

	# check if either %10 == 0
fracs = []
for ab in xrange(11,100):
	for cd in xrange(ab+1,100):
		if is_cancelling(ab,cd):
			fracs.append((ab,cd))

x,y = reduce(lambda x,y: (x[0]*y[0],x[1]*y[1]), fracs, (1,1))

print 1.*x/y 