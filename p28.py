
# 10 minutes - quick iter experiementing to get endpoints right
# In [3]: %time %run p28.py
# 669171001
# CPU times: user 3.62 ms, sys: 2.32 ms, total: 5.94 ms
# Wall time: 3.95 ms

c = 1
N = 1001
end = N*N
step = 2
total = 1

while True:
	for i in xrange(4):
		c += step
		total += c
	step += 2
	if c >= end:
		break

print total