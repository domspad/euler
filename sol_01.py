"""
(something that takes at most 1 minute)
All answers up to 100 million

"""

from math import sqrt

def solve(M=10**7):
	"""
	Print all answers up to M
	"""
	print ("Finding all integer solutions 0 < b,r < {} "
		   "for b**2 - b - 2*b*r - r**2 +r == 0").format(M)
	m = 10 ** 12
	for m in xrange(1,M):
		b = int(m / sqrt(2)) + 1
		r = m - b
		if b**2 - b - 2*b*r - r**2 +r == 0:
			print m


if __name__ == '__main__':
	solve()