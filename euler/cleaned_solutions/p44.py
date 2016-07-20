
# 6 mins
# In [59]: time %run p44.py
# 5482660
# CPU times: user 18.7 s, sys: 52.2 ms, total: 18.7 s
# Wall time: 18.8 s
# WOW ONLY ONE NUM IN THE PENT_DIFFS SET!, did I GET LUCKY

N = 10000
PENTS = [n*(3*n -1)/2 for n in xrange(1,N+1)]
PENTS_SET = set(PENTS)

PENT_DIFFS = []

for i in xrange(N):
	for j in xrange(i,N):
		p1,p2 = PENTS[i],PENTS[j]
		if p2 + p1 in PENTS_SET and p2 - p1 in PENTS_SET:
			PENT_DIFFS.append(p2-p1)

print min(PENT_DIFFS)