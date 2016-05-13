
# 9 mins but without proof with upperbound past which not possible
	# NEVERMIND PROOF!
		# because largest possible digit is 9! ~ 10^6, so if N digit number then sum of digits <= N * 1e6, putting upperbound of N ~ 8 digits 

# In [19]: time %run p34.py
# 40730
# CPU times: user 4min 20s, sys: 1.39 s, total: 4min 22s
# Wall time: 4min 24s

from math import factorial
dig_fact = dict(zip(map(str,xrange(10)),map(factorial,xrange(10))))

magic_nums = []
for n in xrange(10,100000000):
	digits = list(str(n))
	if n % 1000000 == 0 :
		print n
	if n == sum(dig_fact[i] for i in digits):
		magic_nums.append(n)
		print '\t', n

print sum(magic_nums)