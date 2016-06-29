
# 8 mins
# In [55]: time %run p43.py
# 16695334890
# CPU times: user 10.5 s, sys: 49.1 ms, total: 10.6 s
# Wall time: 10.6 s

def is_substring_div(str_num):
	"""
	return True if num has weird subdigit divisibility property
	num has 10 digits
	"""
	for i,p in enumerate((2,3,5,7,11,13,17)):
		start_idx = i+1
		if int(str_num[start_idx:start_idx+3]) % p != 0:
			return False
	return True

from itertools import permutations

for perm in permutations(map(str,xrange(10))):
	str_num = ''.join(perm)

print sum(int(''.join(perm)) for perm in permutations(map(str,xrange(10)))
						if is_substring_div(''.join(perm)))