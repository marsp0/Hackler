#!/bin/python

'''https://www.hackerrank.com/challenges/chocolate-feast'''

import sys


t = int(raw_input().strip())
results = []
for a0 in xrange(t):
	counter = 0
	n,c,m = raw_input().strip().split(' ')
	n,c,m = [int(n),int(c),int(m)]
	wrappers = 0
	counter += n//c
	n = n//c
	while n//m > 0:
		counter += n//m
		wrappers += (n//m + n%m)
		n = wrappers
		wrappers = 0
	results.append(counter)

for item in results:
	print item
