
# brute with log magic!
In [7]: %time %run p99.py
line  709
CPU times: user 18.9 ms, sys: 918 µs, total: 19.8 ms
Wall time: 20.6 ms

from math import log
with open('p99_data.txt','r') as f:
	nums = [map(int,p.split(',')) for p in f.read().split('\n')]

print 'line ', nums.index(max(nums, key=lambda x:log(x[0])*x[1])) + 1