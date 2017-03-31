test_cases = int(raw_input().strip())
tests = {}
results = []
for test in xrange(test_cases):
	n = int(raw_input().strip())
	array = [int(v) for v in raw_input().strip().split()]
	tests[test] = [n,array]


for test in tests:
	n,array = tests[test]
	for i in xrange(n-3):
		print 'dsa'
		if sorted(array[i:i+3]) == array[i:i+3]:
			continue
		else:
			max_number = max(array[i:i+3])
			while True:
				array[i:i+3] = array[i+1:i+3].append(array[i])
				if array[i:i+3][-1] == max_number:
					if sorted(array[i:i+3]) == array[i:i+3]:
						break
					else:
						print 'No'
						break
	print array
	if sorted(array) == array:
		print 'Yes'