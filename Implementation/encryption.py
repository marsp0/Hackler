#!/bin/python

'''https://www.hackerrank.com/challenges/encryption'''

import sys
from math import floor, ceil, sqrt


s = raw_input().strip()
lower, upper = int(floor(sqrt(len(s)))), int(ceil(sqrt(len(s))))

result = []
for i in xrange(0,len(s), upper):
	result.append(s[i:i+upper])
print result
j = 0
while j < upper:
	temp = ''
	i = 0
	while i <= lower:
		try:
			temp += result[i][j]
		except IndexError:
			pass
		i += 1
	print temp, 
	j += 1