




# being "smart" (just a calculator) 11min (including brute force impr)
# == product of smallest power of all primes under n!
# In [9]: 16*9*5*7*11*13*17*19
# Out[9]: 232792560


#Brute force ~ 11 mins
# In [5]: %time p5()
# CPU times: user 6min 32s, sys: 3.11 s, total: 6min 35s
# Wall time: 6min 41s
# Out[5]: 232792560

def p5():
	
	n = 2520
	while True:
		if all( n % i == 0 for i in xrange(2,21) ):
			return n
		if n % 100000 == 0:
			print n
		n += 1 



# no faster?
def p5_2():
	
	n = 2520
	while True:
		if all( n % i == 0 for i in range(20,1,-1) ):
			return n
		if n % 100000 == 0:
			print n
		n += 1 



def p5_2():
	
	n = 2520
	while True:
		if all( n % i == 0 for i in range(20,1,-1) ):
			return n
		if n % 100000 == 0:
			print n
		n += 1 
