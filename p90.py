# 27 mins
# In [33]: %time %run p90.py
# 1217
# CPU times: user 255 ms, sys: 3.2 ms, total: 258 ms
# Wall time: 258 ms

# In [185]: len(list(imap(lambda x: (set(x[0]),set(x[1])), product(combinations(map(str,xrange(10)),6),combinations(map(str,xrange(10)),6)))))
# Out[185]: 44100

SQUARES = '01,04,09,16,25,36,49,64,81'.split(',')

from itertools import combinations, product,imap

def check_die_num(num, d1, d2):
	g1, g2 = num
	if g1 in d1 and g2 in d2:
		return True
	elif g1 in d2 and g2 in d1:
		return True
	return False

def check_die(d1,d2):
	return all(check_die_num(num,d1,d2) for num in SQUARES)

c = 0
for d1, d2 in imap(lambda x: (set(x[0]),set(x[1])), product(combinations(map(str,xrange(10)),6),combinations(map(str,xrange(10)),6))): # ~44,000 / 2 die pairs
	for d in (d1,d2):
		if '6' in d and '9' not in d:
			d.add('9')
		if '9' in d and '6' not in d:
			d.add('6')
	if check_die(d1,d2):
		c += 1

print c / 2 # double counted because order of die
	
