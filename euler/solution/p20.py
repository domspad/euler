
# less than a minute

n = reduce(lambda x,y: x*y, xrange(1,101), 1)
print sum(map(int,list(str(n))))