

# 1 hour -- precomputed a_i's, then backwards algorithm to compute convergents
# In [55]: %time %run p65.py
# 272
# CPU times: user 1.89 ms, sys: 966 µs, total: 2.86 ms
# Wall time: 2.13 ms

e_as= [2,1]
for i in xrange(100-2):
	if i % 3 == 0:
		e_as.append(2+(i/3)*2)
	else:
		e_as.append(1)


def expand_back(i):
	"""
	calculate ith convergent by backwards solving
	"""
	partial_frac = [1,e_as[i-1]]
	for j in reversed(xrange(i-1)):
		partial_frac[0] += partial_frac[1]*e_as[j]
		partial_frac = [partial_frac[1],partial_frac[0]]
	return (partial_frac[1],partial_frac[0]) # one too many flips


print sum(map(int,str(expand_back(100)[0])))