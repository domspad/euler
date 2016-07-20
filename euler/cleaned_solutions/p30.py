

# 5 minutes - brute force and sheer luck
# In [24]: %time %run p30.py
# 443839
# CPU times: user 7.84 s, sys: 42 ms, total: 7.88 s
# Wall time: 7.92 s

# In [188]: len(xrange(10, 1000000))
# Out[188]: 999990

# notice that there IS an upperbound such that it cant be true, but didnt try to analytically find it

def is_5th_power_sum(num):
	"""
	Return if is sum of 5th power of digits
	"""
	return num == sum(map(lambda x: int(x)**5 ,list(str(num))))

def p30():
	fifth_powers = []
	for i in xrange(10, 1000000):
	    if is_5th_power_sum(i):
	        fifth_powers.append(i)
	return sum(fifth_powers)

print p30()