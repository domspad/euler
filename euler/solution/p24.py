
# 1 - brute force
# In [34]: %time brute_nth_perm(1000000)
# CPU times: user 7.72 s, sys: 31.6 ms, total: 7.75 s
# Wall time: 7.75 s
# Out[34]: '2783915460'

def next_perm(perm):
    """
    assumes uniq chars in perm
    returns next perm or chars according to alphabetical order
        if "largest" already raises error
    perm: string of chars > 0
    """
    # find first index smaller than previous (from right)
        # raise error if not found
    for i in xrange(len(perm)-2,-1,-1):
        if perm[i] < perm[i+1]:
            break
    if i == 0 and perm[0] >= perm[1]:
        raise Exception('this is the last perm')

    # swap out for next largest index in the previous subset
    # resort remaining subset from small to high
    for j in xrange(len(perm)-1,i,-1):
        if perm[i] < perm[j]:
            break
    new_perm = perm[:i] + perm[j] + ''.join(sorted(perm[i:j] + perm[j+1:]))

    return new_perm


def brute_nth_perm(N,chars=None):
    """
        N > 0
    """

    # set up perms first value
    if chars is None:
        perm = ''.join(map(str,xrange(10)))
    else:
        perm = ''.join(sorted(chars))

    # iterate until Nth perm
    for i in xrange(1, N):
        perm = next_perm(perm)

    return perm

# TESTS
try:
    next_perm('cba')
    assert(False) # should never run
except Exception:
    pass
assert(next_perm('abcde') == 'abced')
assert(next_perm('0321') == '1023')



# 2 - direct compute - factorial digits
# In [82]: %time direct_nth_perm(1000000)
# CPU times: user 48 µs, sys: 16 µs, total: 64 µs
# Wall time: 52 µs
# Out[82]: '2783915460'

#BUTTTTT LOTS of bugs, +1.5 hours to imp and dev
# also not valid for as many cases.. (not for chars)

def fact_id(N, ndig):
    """
    get factid of Nth perm with ndigs (e.g. 3 digits == '021')
    N > 1 int and < ndig!
    ndig in (1,2, ..., 10) int
    """
    id_list = []
    n = N-1 #to account for numbering starting at 0
    tfac = reduce(lambda x, y: x*y, range(1,ndig+1))

    if N > tfac:
        raise Exception('There is no {}th perm with {} digits!'.format(N, ndig))

    for i in xrange(ndig):

        tfac = tfac / (ndig-i)
        ki = (n / tfac)
        id_list.append(ki)
        n -= ki*tfac

    return ''.join(map(str,id_list))

# Really hard to debug with loop
# range in tfac boundary
# range in for loop
# named ndig and n mixed up
# one off error with N

def parse_id(fid):
    """
    parse fid into the corresponding permutation
    """
    dig_list = range(len(fid))
    perm_list = []
    for dig in fid:
        perm_list.append(dig_list.pop(int(dig)))
    return ''.join(map(str,perm_list))

def direct_nth_perm(N,ndig=10):
    """
    returns the Nth perm of the first ndig digits
    N > 1 int
    ndig in (1,2, ..., 10) int
    """
    return parse_id(fact_id(N,ndig))

assert(fact_id(1,6) == '000000')

