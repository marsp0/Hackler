tests = int(raw_input().strip())
database = {}
results = []
for test in xrange(tests):
	n,k = [int(v) for v in raw_input().strip().split()]
	array = [int(v) for v in raw_input().strip().split()]
	database[test] = (k,array)

for test in database:
	curr = 0
	prefix = []
	k,array = database[test]
	for index in xrange(len(array)):
		curr = (array[index]%k + curr)%k
		prefix.append(curr)
	print prefix