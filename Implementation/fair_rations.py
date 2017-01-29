#!/bin/python

'''https://www.hackerrank.com/challenges/fair-rations'''

import sys


N = int(raw_input().strip())
B = map(int,raw_input().strip().split(' '))
counter = 0
for index in xrange(len(B)):
	try:
		if B[index] % 2 == 1:
			B[index] += 1
			B[index+1] += 1
			counter += 2
	except IndexError:
		counter = 'NO'
print counter