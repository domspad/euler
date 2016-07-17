
"""
examples...

closed form fibonacci
intersect? two segments in plane
perpendicular? two angles
heron's formula
"""


# Motivation
# 	you have a function that is wrong when just using floats!

from math import sqrt,floor

SQ5 = sqrt(5)
PHI = (1 + SQ5)/2

def fib(n):
	return floor( ((PHI ** n)/ SQ5) + 0.5 ) 


# (show that its wrong for f_78!)




# Correct
#

from math import sqrt, floor
import decimal
from decimal import Decimal
decimal.getcontext().prec = 2500

#requires 19 precision to keep correct at fib_78!

SQ5_d = Decimal.sqrt(Decimal(5))
PHI_d = (Decimal(1) + SQ5_d) / Decimal(2)

def fib_dec(n):
	return floor( ((PHI_d**n)/SQ5_d) + Decimal(0.5) )   #could also use 'int' here


# get prec required for different fib

# correct list for first 10000 fibs
CORRECT = [ fib_dec(n) for n in range(10000) ] 

# first number precision correct for each
MIN_PREC = []
min_prec = 1
for e,correct_fib in enumerate(CORRECT):
	# find first min prec for that number
	decimal.getcontext().prec = min_prec
	SQ5_d = Decimal.sqrt(Decimal(5))
	PHI_d = (Decimal(1) + SQ5_d) / Decimal(2)
	guess = fib_dec(e)
	while guess != correct_fib:
		min_prec += 1
		decimal.getcontext().prec = min_prec
		SQ5_d = Decimal.sqrt(Decimal(5))
		PHI_d = (Decimal(1) + SQ5_d) / Decimal(2)
		guess = fib_dec(e)
	print(e, min_prec)
	MIN_PREC.append(min_prec)



import matplotlib.pyplot as plt
import pandas as pd 

ser = pd.Series(MIN_PREC)
ser.plot()
plt.show()
# slope is roughly 0.2094 so roughly each prec digit gets you 5 more fib numbers

################################################################################

# IN SOME PLACES PRECISION WONT HELP YOU!
# e.g are two slopes perpendicular?!?!

import decimal
from decimal import Decimal
decimal.getcontext().prec = 30

def slope(p1,p2=(0,0)):
	x1,y1 = p1
	x2,y2 = p2
	return (y2 - y1)/(x2 -x1)

def perp(x,y):
	m1 = slope((x,y))
	m2 = slope((-y,x))
	return m1 + 1/m2 == 0

def slope_d(p1, p2=(0,0)):
	x1,y1 = p1
	x2,y2 = p2
	return Decimal(y2-y1)/Decimal(x2-x1)


def perp_d(x,y):
	m1 = slope_d((x,y))
	m2 = slope_d((-y,x))
	return m1 + Decimal(1)/m2 == 0




m1 = slope((3,11),(0,0))
m2 = slope((3,11),(14,8))
m1_d = slope_d((3,11),(0,0))
m2_d = slope_d((3,11),(14,8))

FLOAT_WRONG = set()
DECIMAL_WRONG = set()

for y in range(1, 100):
	for x in range(1, y):
		if not perp(x,y):
			FLOAT_WRONG.add((x,y))
		if not perp_d(x,y):
			DECIMAL_WRONG.add((x,y))

#out of 99*98/2 == 4851 (x,y) pairs
	# float --> 1122 wrong!
	# decimal --> 752 wrong! (see below)

best_d = 0
least_wrong = 4851
for d in range(1,300):
	i = 0
	decimal.getcontext().prec = d
	for y in range(1, 100):
		for x in range(1, y):
			if not perp_d(x,y):
				i+=1
	if i < least_wrong:
		best_d, least_wrong = d, i

# best_d --> 142 
# least_wrong --> 752





