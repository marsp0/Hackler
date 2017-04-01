tests = int(raw_input().strip())
test_database = []
for i in xrange(tests):
	n,k = [int(v) for v in raw_input().strip().split()]
	test_database.append((n,k))

for test in test_database:
	n,k = test
	if k == 0:
		for i in xrange(1,n+1):
			print i,
		print
		continue
	positions = {key:[] for key in xrange(1,n+1)}
	for number in xrange(1,n+1):
		try:
			if number + k < n+1 and n >= 1:
				positions[number + k].append(number)
		except KeyError:
			pass
		try:
			if number + k < n+1 and n >= 1:
				positions[number - k].append(number)
		except KeyError:
			pass
	print positions
