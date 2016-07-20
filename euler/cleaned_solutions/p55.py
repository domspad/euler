

#6 mins
# In [87]: time %run p55.py
# 249
# CPU times: user 271 ms, sys: 7.79 ms, total: 279 ms
# Wall time: 275 ms

def rev_add(n):

	rev_n = int(''.join(d for d in reversed(str(n))))
	return n + rev_n

def is_pal(n):
	str_n = str(n)
	return str_n == ''.join(d for d in reversed(str_n))


def is_lychrel(n):
	for it in xrange(50):
		n = rev_add(n)
		if is_pal(n):
			return False
	return True

print sum(1 for n in xrange(1,10000) if is_lychrel(n))
	