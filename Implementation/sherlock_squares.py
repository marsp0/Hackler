'''
	https://www.hackerrank.com/challenges/sherlock-and-squares
'''

import math

test_cases = int(raw_input().strip())
tests = []
results = [0 for _ in xrange(test_cases)]



for i in xrange(test_cases):
	start, end = [int(v) for v in raw_input().strip().split()]
	tests.append((start,end))

for i in xrange(len(tests)):
	start,end = tests[i]

	start_root = int(math.ceil(math.sqrt(start)))
	end_root = int(math.sqrt(end))

	for number in xrange(start_root, end_root+1):
		results[i] += 1

	

for item in results:
	print item
