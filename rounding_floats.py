
import decimal
from decimal import Decimal

from math import sqrt, floor

decimal.getcontext().prec = 300

SQRT5 = Decimal.sqrt(Decimal(5))
PHI = (Decimal(1) + SQRT5) / Decimal(2)


# In [11]: int??
# Docstring:
# int(x=0) -> int or long
# int(x, base=10) -> int or long
# Convert a number or string to an integer, or return 0 if no arguments
# are given.  If x is floating point, the conversion truncates towards zero.

def fib(n):
	return int(((PHI**n)/SQRT5) + Decimal(0.5) )

def floor_fib(n):
	return int(floor(((PHI**n)/SQRT5) + Decimal(0.5) ))

#ALSO floor_fib is wrong!
fib(78) == floor_fib(78) #False!