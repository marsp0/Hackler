'''https://www.hackerrank.com/challenges/countingsort2'''

from collections import defaultdict

n = int(raw_input().strip())
array = [int(v) for v in raw_input().strip().split()]
result = [0 for _ in xrange(100)]
for item in array:
	result[item] += 1

for item in xrange(len(result)):
	if result[item] != 0:
		for i in xrange(result[item]):
			print str(item), 