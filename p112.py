
# 15 mins
# In [41]: %time %run p112.py
# 1587000
# CPU times: user 16.9 s, sys: 106 ms, total: 17 s
# Wall time: 17.1 s


def is_increasing(n):
	str_n = str(n)
	return all( int(a) <= int(b) for a,b in zip(str_n,str_n[1:]))

def is_decreasing(n):
	str_n = str(n)
	return all( int(a) >= int(b) for a,b in zip(str_n,str_n[1:]))

def is_bouncy(n):
	return not (is_increasing(n) or is_decreasing(n))


def bouncy_ratio_ltn(n):
	"""
	return (bouncy,nonbouncy) ratio for all numbers from 1,...,n
	"""
	bouncy = len(filter(is_bouncy,xrange(1,n+1)))
	return (bouncy,n - bouncy)

# bouncy, nonbouncy = 0,2
nonbouncy = 1
total = 1
# total != 100 * nonbouncy
while total != 100 * nonbouncy:
	total += 1
	if is_decreasing(total) or is_increasing(total):
		nonbouncy += 1
print total 