
#15 mins (but building off p21 - sum of proper divs)
# In [48]: %time %run p23.py
# 4179871
# CPU times: user 3.19 s, sys: 19.5 ms, total: 3.2 s
# Wall time: 3.22 s



from math import sqrt
bound = 28123

# generate all abundant nums < 28123
abundants = set()
#THE FOLLOWING BLOCK FROM p21!
for i in xrange(2,bound):
	total = 1 #start at 1 for 1 always divides
	sqroot = int(sqrt(i)) #check sqrt 
	if i / sqroot == sqroot and i % sqroot == 0:
		total += sqroot
		sqroot -= 1 # decrement to provide proper range
	for j in xrange(2, sqroot + 1):
		if i % j == 0:
			total += j + (i/j)
	if total > i:
		abundants.add(i)

# check each positive int <= 28123
total = 0
for num in xrange(1, bound + 1):
	possible = False
	for i in abundants:
		if num - i in abundants:
			possible = True
			# print num, i, num - i
			break
	if not possible:
		# print num
		total += num

print total