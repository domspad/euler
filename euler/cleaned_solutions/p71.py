

N = 1000

def gcd(a,b):
	"""
	a >= 0 int
	b > a int
	"""
	while a != 0 and a != 1:
		a, b = b - ((b / a) * a), a
	if a == 0:
		return b
	elif a == 1:
		return 1
	else:
		print "uh-oh!"

def red_frac_list(N):
	"""
	returns all reduced fracs up to denom == N
	"""
	return [ float(a)/b for b in range(2,N)
					    for a in range(1,b)
					    if gcd(a,b) == 1 ]

def brute_p71(N):
	sorted_red_fracs = sorted(red_frac_list(N))
	idx = sorted_red_fracs.index(3.0/7)
	return sorted_red_fracs[idx - 1]

## code didn't finish even after 20 mins
# 20 mins in finished started running

###############################################################

def closest_frac(f, n):
	"""
	0 < f < 1 float
	2 <= n int
	"""
	k = int(f * n)
	return k if k != f * n else k -1



def iter_p71(N):
	sofar = (0,1)
	for n in xrange(2,N):
		num = closest_frac(3./7, n=n)
		a,b = sofar
		if a * n < num * b : # then a/b < num/n < f
			sofar = (num, n)
	return sofar

# In [3]: %time iter_p71(N=1000000)
# CPU times: user 783 ms, sys: 18.6 ms, total: 802 ms
# Wall time: 794 ms
# Out[3]: (428570, 999997)



# 40 mins finished started running

