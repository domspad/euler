

# 5 minutes
# In [21]: time %run p36.py
# 872187
# CPU times: user 1.61 s, sys: 11.9 ms, total: 1.62 s
# Wall time: 1.63 s

def is_pal(string):
	"""
	Return whether is a palindrome
	"""
	return string == ''.join(reversed(string))


print sum(n for n in xrange(1,10**6) if is_pal(str(n)) and is_pal(bin(n)[2:]))