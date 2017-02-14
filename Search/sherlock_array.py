'''https://www.hackerrank.com/challenges/sherlock-and-array'''

tests = int(raw_input().strip())
database = {}
for test in xrange(tests):
	n = int(raw_input().strip())
	array = [int(v) for v in raw_input().strip().split()]
	database[test] = array
results = []
for test in database:
	temp = 'NO'
	array = database[test]
	left = 0
	right = sum(array)
	previous = 0
	for index in xrange(len(array)):
		current = array[index]
		left += previous
		right -= current
		if left == right:
			temp = 'YES'
			break
		previous = current
	results.append(temp)
for item in results:
	print item