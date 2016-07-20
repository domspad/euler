

# 7 mins (but no concrete proof that it ends after power 30)
# In [26]: %time %run p63.py
# 49
# CPU times: user 2.84 ms, sys: 1.39 ms, total: 4.23 ms
# Wall time: 3.07 ms

count = 0
for power in xrange(1,40):
	i = 1
	val = i**power
	while len(str(val)) < power + 1:
		if len(str(val)) == power:
			# print i, power, val
			count += 1
		i += 1
		val = i**power

print count