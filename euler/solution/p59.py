
# 18 mins
# brute
# In [60]: %time %run p59.py
# ('g', 'o', 'd')
# 107359
# CPU times: user 4.23 s, sys: 28.6 ms, total: 4.26 s
# Wall time: 4.29 s

ABCS = 'abcdefghijklmnopqrstuvwxyz'

ASCII = { c: 97+i for i,c in enumerate(ABCS)}
NUM = {97+i: c for i,c in enumerate(ABCS)}

from itertools import product

#get msg
with open('p59_cipher.txt','r') as f:
	msg = map(int,f.read().strip().split(','))

def decrypt(msg, key):
	"""
	key len 3
	"""
	idx = 0
	dec_bites = map(lambda x: str(unichr(x)),[b ^ ASCII[key[i % 3]] for i,b in enumerate(msg)])
	return ''.join(dec_bites)


for key in product(ABCS,ABCS,ABCS):
	dec_msg = decrypt(msg, key)
	if 'the' in dec_msg and 'and' in dec_msg and 'that' in dec_msg:
		print key
		print sum(map(lambda x:ord(x),decrypt(msg,key)))
		break




