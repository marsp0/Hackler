'''https://www.hackerrank.com/challenges/two-arrays?h_r=next-challenge&h_v=zen - EASY'''

tests = int(raw_input().strip())
database = []
for test in xrange(tests):
	n,k = [int(v) for v in raw_input().strip().split()]
	array_1 = [int(v) for v in raw_input().strip().split()]
	array_2 = [int(v) for v in raw_input().strip().split()]
	database.append((k,array_1,array_2))

for test in database:
	k,array_1,array_2 = test
	array_2 = sorted(array_2,reverse=True)
	array_1 = sorted(array_1)
	result = False
	for i in xrange(len(array_1)):
		if array_1[i] + array_2[i] < k:
			result = 'NO'
			break
	if not result:
		result = 'YES'
	print result