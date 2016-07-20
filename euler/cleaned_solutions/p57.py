
#8 mins
# In [18]: time %run p57.py
# 153
# CPU times: user 8.8 ms, sys: 2.09 ms, total: 10.9 ms
# Wall time: 10.2 ms

start = (3,2)

def next_expansion(frac):
	n,d = frac
	n += d
	n,d = d,n
	n += d
	return (n,d)

t = 0
for i in xrange(1000):
	if len(str(start[0])) > len(str(start[1])):
		t += 1
	start = next_expansion(start)

print t