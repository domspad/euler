
# Debugging... 35 mins

ones = [''] + 'one two three four five six seven eight nine'.split()
teens = 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
tens = ['', ''] + 'twenty thirty forty fifty sixty seventy eighty ninety'.split()

def count(i):
	"Returns string length of number"
	if i < 10:
		print i, ones[i]
		return len(ones[i])
	elif i < 20:
		print i, teens[i % 10]
		return len(teens[i % 10])
	elif i < 100:
		print i, tens[i / 10] + ones[i % 10]
		return len(tens[i / 10]) + len(ones[i % 10])
	elif i % 100 == 0:
		print i, ones[i / 100] + 'hundred'
		return len(ones[i / 100] + 'hundred')
	else:
		print i, ones[i/100] + 'hundredand'
		return len(ones[i / 100] + 'hundredand') + count(i % 100)

total = sum(count(n) for n in xrange(1,1000))

total += len('one thousand'.replace(' ',''))
print total

def p17():
	total = sum(count(n) for n in xrange(1,1000))

	# total += len('one thousand'.replace(' ',''))
	print total

p17()