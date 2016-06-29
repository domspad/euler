

# determine intercepts (48 mins from start to finish)
# In [35]: %time %run p102.py
# 228
# CPU times: user 16.9 ms, sys: 1.79 ms, total: 18.6 ms
# Wall time: 25.8 ms

with open('p102_triangles.txt', 'r') as f:
	lines = map(str.strip, f.readlines())
	coords = [map(int, line.split(',')) for line in lines]

def y_int(x1,y1,x2,y2):
	""" return y intercept (0,b) if line between points crosses y-axis
	"""
	if min(x1,x2) <= 0 and max(x1,x2) >= 0:
		return ((y2 - y1) * (0 - x2) / (x2 - x1)) + y2
	else:
		return None

def x_int(x1,y1,x2,y2):
	""" return y intercept (0,b) if line between points crosses y-axis
	"""
	return y_int(y1,x1,y2,x2)

	# if min(y1,y2) <= 0 and max(y1,y2) >= 0:
	# 	return ((x2 - x1) * (0 - y2) / (y2 - y1)) + x2
	# else:
	# 	return None

c = 0
for x1,y1,x2,y2,x3,y3 in coords:
	x_intercepts = [] 
	y_intercepts = []

	a = x_int(x1,y1,x2,y2)
	if a is not None:
		x_intercepts.append(a)
	a = x_int(x1,y1,x3,y3)
	if a is not None:
		x_intercepts.append(a)
	a = x_int(x3,y3,x2,y2)
	if a is not None:
		x_intercepts.append(a)

	a = y_int(x1,y1,x2,y2)
	if a is not None:
		y_intercepts.append(a)
	a = y_int(x1,y1,x3,y3)
	if a is not None:
		y_intercepts.append(a)
	a = y_int(x3,y3,x2,y2)
	if a is not None:
		y_intercepts.append(a)

	if min(len(x_intercepts),len(y_intercepts)) > 0:
		if 0 <= max(x_intercepts) and 0 >= min(x_intercepts) and 0 <= max(y_intercepts) and 0 >= min(y_intercepts):
			c += 1

print c

