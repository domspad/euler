# FIXME: K5 gives some false positives.... the third one is actual answer

# GOT IT! WITH up to primes6.txt (from the website ... so first 6million primes up to 100,000,000)
# TOTAL TIME ROUGHLY... 3 hours to think and program and solve
# In [1]: %time %run p60.py
# CPU times: user 8min 27s, sys: 1.08 s, total: 8min 29s
# Wall time: 8min 29s

# In [12]: sorted(K5, key=lambda x:sum(x))
# Out[12]:
# [(1483, 1993, 3457, 5869, 8209),
#  (1399, 3037, 3433, 4987, 8461),
#  (13, 5197, 5701, 6733, 8389),            <---- ACTUAL ANSWER (the two above had a couple False! still)
#  (1973, 4877, 5711, 8291, 8573)]

# SEEE
# from itertools import permutations
# ans =sorted(K5, key=lambda x:sum(x))[:10][2]
# concs = map(lambda x: conc(x[0],x[1]), list(permutations(ans, 2)))
# map(lambda x: x in PRIMES, concs)


# read in PRIMES list from the first 6 primes<n> files from https://primes.utm.edu/lists/small/millions/
    # # download a bunch of files
    #     wget URL1 URL2
    # # unzip them
    #     unzip "*.zip"
    # # cut the first n lines
    # # concatenate them into one large file


PRIMES = map(int, open('primes1.txt', 'r').read().split())
PRIMES_SET = set(PRIMES)

from math import log10
def num_digit(a):
    """
    Return number of digits in integer a>0

    In [4]: %timeit log10(123456789)
    10000000 loops, best of 3: 64.5 ns per loop

    In [7]: %timeit int(log10(123456789))
    10000000 loops, best of 3: 178 ns per loop

    In [6]: %timeit len(str(123456789))
    10000000 loops, best of 3: 177 ns per loop
    """
    return int(log10(a))

MOST_DIGITS = num_digit(PRIMES[-1])


def conc(a, b):
    """
    Return the int given by concatenating the digits of a and b
    """
    return int(str(a) + str(b))

def has_edge(p,q):
    """
    return true if concatenating p,q in either order is prime number
    """
    return (conc(p, q) in PRIMES_SET) and (conc(q, p) in PRIMES_SET)


# create edge_dict (smaller only point to larger)
from collections import defaultdict
from math import sqrt
edge_dict = defaultdict(set)
THRESH = sqrt(PRIMES[-1])

for i, p in enumerate(PRIMES):
    if p < THRESH:  # only build its edges if we can check any numbers bigger than it
        #only check for up to number of digits we can check
        spare_digits = MOST_DIGITS - num_digit(p)
        for j in xrange(i + 1, len(PRIMES)):
            q = PRIMES[j]
            if num_digit(q) > spare_digits:
                break
            if has_edge(p, q):
                edge_dict[p].add(q)


# create K_3 set
# set of 3-tuples (in increasing order of all 3-prime pairs that conc to make primes)

K3 = set()

sorted_edge_dict_keys = edge_dict.keys()
sorted_edge_dict_keys.sort()

for i, p in enumerate(sorted_edge_dict_keys):
    for j in xrange(i + 1, len(sorted_edge_dict_keys)):
        q = sorted_edge_dict_keys[j]
        rs = filter(lambda x: x > p and x > q, edge_dict[p] & edge_dict[q])
        # compare edge sets
        # only take if bigger than both p,q (auto because of constraint on edge_dict!)
        for r in rs:
            K3.add((p, q, r))


# create K_n+1 from K_n and edge_dict
from operator import and_

def build_Knp1(Kn):
    Knp1 = set()
    for n_set in Kn:
        rs = reduce(and_, (edge_dict[pi] for pi in n_set), edge_dict[n_set[-1]])
        for r in rs:
            Knp1.add(n_set + (r,))
        # unpack all elements
    return Knp1


K4 = build_Knp1(K3)
K5 = build_Knp1(K4)


