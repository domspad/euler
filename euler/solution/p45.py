

# 5 mins
# In [66]: time %run p45.py
# set([1, 40755, 1533776805])
# CPU times: user 1.08 s, sys: 101 ms, total: 1.18 s
# Wall time: 1.17 s


TRIS = set(n*(n+1)/2 for n in xrange(1,1000000))
PENTS = set(n*(3*n - 1)/2 for n in xrange(1,1000000))
HEXS = set(n*(2*n-1) for n in xrange(1,1000000))

print TRIS & PENTS & HEXS