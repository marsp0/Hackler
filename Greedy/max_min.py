'''https://www.hackerrank.com/challenges/angry-children - MEDIUM'''

import sys

n = int(raw_input().strip())
k = int(raw_input().strip())
array = []
for i in xrange(n):
	array.append(int(raw_input().strip()))
array = sorted(array)
min_difference = sys.maxint
for index in xrange(len(array)-(k-1)):
	if array[index+k-1] - array[index] < min_difference:
		min_difference = array[index+k-1] - array[index]

print min_difference