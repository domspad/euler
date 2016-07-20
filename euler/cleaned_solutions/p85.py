

# # closed formula + brute
# In [17]: %time %run p85.py
# CPU times: user 3.72 s, sys: 45.6 ms, total: 3.77 s
# Wall time: 4.12 s
# 2772

def f(m,n):
	return n*(n+1)*m*(m+1)/4



print min(( (m,n) for m in xrange(3000) for n in xrange(m,3000)),
	key=lambda x:abs(2000000 - f(x[0],x[1])))