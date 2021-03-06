
# brute force and non-float arithmetic for accuracy!
# In [3]: %time %run p94.py
# 518408346
# CPU times: user 21min 59s, sys: 5.03 s, total: 22min 4s
# Wall time: 22min 14s


from math import sqrt 

#WRONG
# In [115]: %time %run p94.py
# 508904531
# CPU times: user 14min 9s, sys: 2.72 s, total: 14min 12s
# Wall time: 14min 15s



def is_integer(x):
	return float(int(x)) == x

def has_integer_area(a,b,c):
	s = (a + b + c)/2.
	return is_integer(sqrt(s*(s-a)*(s-b)*(s-c)))

def is_square(n):
	"""
	n > 2
	"""
	return int(sqrt(n))**2 == n


def is_ap1(a):
	v = ((a+1)**2)*(3*(a**2)-(2*a)-1)
	return v % 16 == 0 and is_square(v)

def is_am1(a):
	v = ((a-1)**2)*(3*(a**2)+(2*a)-1)
	return v % 16 == 0 and is_square(v)


# c = 0
# B = int((10**4)/3.) + 1 # *5from b-1
# for a in xrange(1,B):
# 	if has_integer_area(a,a,a+1):
# 		print a,a,a+1
# 		c += 1
# 		# print a,a,a+1
# 	if has_integer_area(a,a,a-1): #ASSUMES BOTH CANNOT BE TRUE
# 		print a,a,a-1
# 		c += 1
# 		# print a,a, a-1
# print c
			# 1 1 2
			# 5 5 6
			# 17 17 16
			# 65 65 66
			# 241 241 240
			# 901 901 902
			# 3361 3361 3360
			# 12545 12545 12546
			# 46817 46817 46816
			# 174725 174725 174726
			# 302828 302828 302829
			# 417175 417175 417176
			# 490240 490240 490239

c = 0
perim_sum = 0
tris = []
B = int((10**9)/3.) + 1 #probably ~30 mins
for a in xrange(1,B):
	if is_am1(a):
		print a,a,a-1
		tris.append((a,a,a-1))
		c += 1
		perim_sum += (3*a)-1
	if is_ap1(a): 
		print a,a,a+1
		tris.append((a,a,a+1))
		c += 1
		perim_sum += (3*a)+1
# print c - 2  #(counts 1,1,0 as solution)
print perim_sum - 6 #(counts 1,1,0 and 1,1,2 as solutions)

		# 5 5 6
		# 17 17 16
		# 65 65 66
		# 241 241 240
		# 901 901 902
		# 3361 3361 3360
		# 12545 12545 12546
		# 46817 46817 46816
		# 174725 174725 174726
		# 652081 652081 652080
		# 2433601 2433601 2433602
		# 9082321 9082321 9082320
		# 33895685 33895685 33895686
		# 126500417 126500417 126500416