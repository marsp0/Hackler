tests = int(raw_input().strip())
for i in xrange(tests):
	a,b,c = [int(v) for v in raw_input().strip().split()]
	if abs(c-b) < abs(c-a):
		print 'Cat B'
	elif abs(c-a) == abs(c-b):
		print 'Mouse C'
	else:
		print 'Cat A'