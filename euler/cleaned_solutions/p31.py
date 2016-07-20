

 # 50 mins in, gave up on recursive, did "smart brute"
 # In [1]: time %run p31.py
 # CPU times: user 35.5 ms, sys: 5.01 ms, total: 40.5 ms
 # Wall time: 37.6 ms


c = 0
sub = 0
for th in (0,200):
	sub += th
	for oh in xrange(0,201 - sub,100):
		sub += oh
		for f in xrange(0,201 - sub,50):
			sub += f
			for tw in xrange(0,201 - sub,20):
				sub += tw
				for d in xrange(0,201 - sub,10):
					sub += d
					for n in xrange(0,201 - sub,5):
						sub += n
						for pp in xrange(0,201 - sub,2):
							sub += pp
							# last step is just however many p's needed
							# print (th, oh, f, tw, d, n, pp, 200 - sub)
							c += 1
							sub -= pp
						sub -= n
					sub -= d
				sub -= tw
			sub -= f
		sub -= oh
	sub -= th
