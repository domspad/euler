
# 20 mins to solution
# In [32]: %time %run p21.py
# 31626
# CPU times: user 133 ms, sys: 5.04 ms, total: 138 ms
# Wall time: 136 ms

from math import sqrt
# list of sum of divisors
divisor_sums = [0,0] # start with 0 and 1's sum of proper divisors for index purposes
for i in xrange(2,10000):
	total = 1 #start at 1 for 1 always divides
	sqroot = int(sqrt(i)) #check sqrt 
	if i / sqroot == sqroot and i % sqroot == 0:
		total += sqroot
		sqroot -= 1 # decrement to provide proper range
	for j in xrange(2, sqroot + 1):
		if i % j == 0:
			total += j + (i/j)
	divisor_sums.append(total)

# check amicable numbers
amicable_sum = 0
for num, its_sum in enumerate(divisor_sums):
	if num == 0 or num == 1 or num == its_sum:
		continue
	if its_sum < len(divisor_sums) and divisor_sums[its_sum] == num:
		# print num, its_sum
		amicable_sum += (num + its_sum)

amicable_sum /= 2 # because added all pairs twice!
print amicable_sum