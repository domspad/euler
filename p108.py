
# 3 iterations of smart brute before even guess+check the sols by hand! (related to factorization of n)
# 95 mins
# In [78]: num_sols(2*2*3*3*5*7*11*13)
# Out[78]: 1013
# In [79]: 2*2*3*3*5*7*11*13
# Out[79]: 180180


# all fracs are (x,y) == x/y


def equal(f1, f2):
	"""
	True if fraction f1 == fraction f2
	"""
	a,b = f1
	c,d = f2
	return a*d == b*c

assert equal((18,72),(1,4))


def is_solution(x,y,n):
	return equal((x+y,x*y),(1,n))

assert is_solution(6,12,4)


def y_given_x(x,n):
	flx = float(x)
	return (n*flx)/(flx - n)

def is_int(f):
	return float(int(f)) == f

# n = 11
# for n in xrange(2, 1000):
# 	SOLS = []	
# 	for x in xrange(n+1,(n*(n+1))+1):
# 		flx = float(x)
# 		if is_int((n*flx)/(flx-n)):
# 			SOLS.append((x, (n*flx)/(flx-n)))
# 	if len(SOLS) > 1000
	# cand_y = y_given_x(x,n)
	# if cand_y > 0 and is_int(cand_y):
	# 	print "YES", x, cand_y
	# else:
	# 	print x, cand_y

def num_sols(n):
	c = 0
	for x in xrange(n+1, (2*n) + 1):
		y = y_given_x(x,n)
		if is_int(y):
			c += 1
			# print '\t',x,y
	# print '\t', c
	return c 


n = 70000
nsols = num_sols(n)
xs = [n]
ys = [nsols]
while nsols <= 1000:
	n += 1
	nsols = num_sols(n)
	print n,nsols
	xs.append(n)
	ys.append(nsols)


# DEGUGGING WITH GRAPHS RECIPE
import pandas as pd 
import matplotlib.pyplot as plt 

fig, ax = plt.subplots(nrows=1,ncols=1,sharex=False,sharey=False)
ser = pd.Series(data=ys, index=xs)
ser.plot(ax=ax,kind='line',title=None,logx=False,logy=False,loglog=True)
	# - 'line' : line plot (default)
#     - 'bar' : vertical bar plot
#     - 'barh' : horizontal bar plot
#     - 'hist' : histogram
#     - 'box' : boxplot
#     - 'kde' : Kernel Density Estimation plot
#     - 'density' : same as 'kde'
#     - 'area' : area plot
#     - 'pie' : pie plot
plt.show()


### where are we bumping up?

largest = 3
largest_n = 4 
n = 5
nsols = num_sols(n)
BUMPUP_VAL = [largest]
BUMPUP = [largest_n]
while nsols < 200:
	n += 1
	nsols = num_sols(n)
	if nsols > largest:
		largest, largest_n = nsols, n
		BUMPUP.append(largest_n)
		BUMPUP_VAL.append(largest)




# smarter iter?
#YES
# In [3]: BUMPUP
# Out[3]: [4, 6, 12, 24, 30, 60, 120, 180, 210, 360, 420, 840, 1260, 1680, 2520, 4620]
