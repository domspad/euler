
# brute force with generator (5 mins)
# In [77]: %time %run p25.py
# 4782
# CPU times: user 58.1 ms, sys: 5.87 ms, total: 64 ms
# Wall time: 60.7 ms

def fibonnaci():
	a, b = 0, 1
	while True:
		yield b
		a, b = b, a + b

g = fibonnaci()

i = 1
n = next(g)
while len(str(n)) < 1000:
	i += 1
	n = next(g)
print i, n