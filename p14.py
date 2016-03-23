# helpers

def f(n):
	"defined for n > 1 integer"
	if n % 2 == 0:
		return n / 2
	else:
		return 3 * n + 1


# 1 - Brute, recursive

def lenf_rec(n):
	"returns length of f(n) chain for n"
	"defined for n = 1 integer"
	if n == 1:
		return 0
	else:
		return 1 + lenf_rec(f(n))


def longest_chain_rec(N):
	"returns n < N, such that f(n) chain is longest"
	"N > 2"
	current_longest = (2, 1)
	for n in xrange(2,N):
		# compute chain for n
		count = lenf_rec(n)
		# print "{:<30}{:<30}".format(n, count)
		if count > current_longest[1]:
			current_longest = (n, count)
	return current_longest[0]


# 2 - Brute, tail-recursive?
# NO TCO!!!!

def lenf_tail_rec(n):
	"returns length of f(n) chain for n"
	"defined for n = 1 integer"
	def lenf_help(n, count=0):
		if n == 1:
			return count
		else:
			return lenf_help(f(n), count + 1)
	return lenf_help(n)

def longest_chain_tail_rec(N):
	"returns n < N, such that f(n) chain is longest"
	"N > 2"
	current_longest = (2, 1)
	for n in xrange(2,N):
		# compute chain for n
		count = lenf_tail_rec(n)
		# print "{:<30}{:<30}".format(n, count)
		if count > current_longest[1]:
			current_longest = (n, count)
	return current_longest[0]

# 3 - Brute, iter

def lenf_iter(n):
	"returns length of f(n) chain for n"
	"defined for n = 1 integer"
	count = 0
	fn = n
	while fn != 1:
		count += 1
		fn = f(fn)
	return count

def longest_chain_iter(N):
	"returns n < N, such that f(n) chain is longest"
	"N > 2"
	current_longest = (2, 1)
	for n in xrange(2,N):
		# compute chain for n
		count = lenf_iter(n)
		# print "{:<30}{:<30}".format(n, count)
		if count > current_longest[1]:
			current_longest = (n, count)
	return current_longest[0]



# 4 - Brute, iter, memo

import collections
import functools

class memoized(object):
   '''Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned
   (not reevaluated).
   '''
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      if not isinstance(args, collections.Hashable):
         # uncacheable. a list, for instance.
         # better to not cache than blow up.
         return self.func(*args)
      if args in self.cache:
         return self.cache[args]
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__
   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)

@memoized
def lenf_iter_memo(n):
	"returns length of f(n) chain for n"
	"defined for n = 1 integer"
	count = 0
	fn = n
	while fn != 1:
		count += 1
		fn = f(fn)
	return count


def longest_chain_iter_memo(N):
	"returns n < N, such that f(n) chain is longest"
	"N > 2"
	current_longest = (2, 1)
	for n in xrange(2,N):
		# compute chain for n
		count = lenf_iter_memo(n)
		# print "{:<30}{:<30}".format(n, count)
		if count > current_longest[1]:
			current_longest = (n, count)
	return current_longest[0]



# 5 - lenf_rec_memo?

@memoized
def lenf_rec_memo_help(n, count=0):
	if n == 1:
		return count
	else:
		return lenf_rec_memo_help(f(n), count + 1)

def lenf_rec_memo(N):
	return lenf_rec_memo_help(N, 0)

# 5 - OTHER TWEAKS???? (in code list comps...)



#QUESTION function to take funciton?!!
def longest_chain_base(N, lenf):
	"returns n < N, such that f(n) chain is longest"
	"N > 2"
	"lenf(n) is a function to compute length of chain starting at n"
	current_longest = (2, 1)
	for n in xrange(2,N):
		# compute chain for n
		count = lenf(n)
		# print "{:<30}{:<30}".format(n, count)
		if count > current_longest[1]:
			current_longest = (n, count)
	return current_longest[0]

N = 1000000
%time longest_chain_base(N, lenf_rec)
# In [14]: %time longest_chain_base(N, lenf_rec)
# CPU times: user 56.8 s, sys: 372 ms, total: 57.2 s
# Wall time: 57.7 s
# Out[14]: 837799

# 10x smaller, 10X faster
# CPU times: user 4.88 s, sys: 25.2 ms, total: 4.91 s
# Wall time: 4.93 s
# Out[2]: 77031

%time longest_chain_base(N, lenf_tail_rec)
# In [3]: %time longest_chain_base(100000, lenf_tail_rec)
# CPU times: user 5.29 s, sys: 31.4 ms, total: 5.32 s
# Wall time: 5.34 s
# Out[3]: 77031

%time longest_chain_base(N, lenf_iter)
# In [5]: %time longest_chain_base(100000, lenf_iter)
# CPU times: user 3.57 s, sys: 20.4 ms, total: 3.59 s
# Wall time: 3.6 s
# Out[5]: 77031

%time longest_chain_base(N, lenf_iter_memo)
# In [6]: %time longest_chain_base(100000, lenf_iter_memo)
# CPU times: user 3.67 s, sys: 29 ms, total: 3.7 s
# Wall time: 3.71 s
# Out[6]: 77031

# IF YOU RUN A 2nd TIME!!!!
# In [12]: %time longest_chain_base(100000, lenf_iter_memo)
# CPU times: user 223 ms, sys: 7.75 ms, total: 231 ms
# Wall time: 228 ms
# Out[12]: 77031

N = 10000
import sys;sys.setrecursionlimit(10000) #usually 1000
%time longest_chain_base(N, lenf_rec_memo)

