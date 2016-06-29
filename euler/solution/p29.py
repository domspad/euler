

# 1 minute (because small enough to brute!)
# In [3]: %time %run p29.py
# CPU times: user 24.3 ms, sys: 2.1 ms, total: 26.4 ms
# Wall time: 25.8 ms
# Out[3]: 9183


print len(set(a**b for a in xrange(2,101) for b in xrange(2,101)))