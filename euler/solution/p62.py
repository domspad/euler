
#17 mins
# In [16]: %time %run p62.py
# 127035954683
# CPU times: user 2.14 s, sys: 47.8 ms, total: 2.19 s
# Wall time: 2.2 s

from collections import Counter, defaultdict

def are_perms(p1, p2):
	"""
	p1,p2 are strings
	"""
	return Counter(p1) == Counter(p2)

CUBES = [str(c**3) for c in xrange(1,100000)]

dig_counts = defaultdict(list)

for c in CUBES:
	dig_counts[tuple(sorted(Counter(c).items()))].append(int(c))

mins = []
for dig_count in dig_counts:
	if len(dig_counts[dig_count]) == 5:
		mins.append(min(dig_counts[dig_count]))

print min(mins)