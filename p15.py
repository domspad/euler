

# explicit formula solution (easiest to do)
# 10 mins from start to finish
# In [1]: %time %run p15.py
# 137846528820
# CPU times: user 1.5 ms, sys: 508 µs, total: 2.01 ms
# Wall time: 1.45 ms

from math import factorial

def choose(n,k):
	return (factorial(n)/(factorial(n-k)*factorial(k)))

def p15():
	return choose(40,20)

print p15()