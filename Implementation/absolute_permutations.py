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
	elif n % k != 0:
		print -1
		continue
	elif n % 2 == 1:
		print -1
		continue

	results = [0] * (n+1)
	for i in xrange(1,len(results)):
		if results[i] == 0:
			results[i] = i+k
			results[i+k] = i
	for i in xrange(len(results)):
		if i != 0:
			print results[i],
	print