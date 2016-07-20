
# 20 mins - bruet
# SILLY!!! DIDNT EVEN TRY BRUTE AT FIRST
# In [32]: time %run p48.py
# 9110846700
# CPU times: user 93.3 ms, sys: 3.85 ms, total: 97.1 ms
# Wall time: 95.3 ms


def last_10_digits(n):
	"""
	n int
	"""
	return int(str(n)[-10:])



print last_10_digits(sum(last_10_digits(n**n) for n in xrange(1,1001)))



# to smart for own good way...

from math import factorial

def choose(n,k):
	return (factorial(n)/(factorial(n-k)*factorial(k)))

def tri_choose(n,j,k):
	i = n - j - k
	return (factorial(n)/(factorial(k)*factorial(j)*factorial(i)))