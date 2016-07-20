
# backtrack path! - 23 mins (inspired by tim talk in budapest 2 years ago)
# In [34]: %time %run p18.py
# CPU times: user 2 ms, sys: 906 micros, total: 2.9 ms
# Wall time: 2.13 ms


with open('p67_big.txt','r') as f:
	lines = map(str.strip, f.readlines())
	tree = [map(int, line.split(' ')) for line in lines]

n = len(tree)

for i in xrange(n-2,-1,-1): # start from n-1,n-2,...0
	for j in xrange(i+1):
		subpath = max(tree[i+1][j:j+2])
		tree[i][j] += subpath


