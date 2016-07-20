
# BY HAND!!!
#20 mins
#

with open('p79_keylog.txt','r') as f:
	CONSTRAINTS = sorted(map(str.strip,f.readlines()))

def satisfies_cons(passcode, cons):
	# a,b,c = cons
	for c in cons:
		idx = passcode.find(c)
		if idx == -1:
			return False
		passcode = passcode[idx+1:]
	return True

passcode = '73162890'

print all(satisfies_cons(passcode,cons) for cons in CONSTRAINTS)