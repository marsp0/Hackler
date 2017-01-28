#!/bin/python

'''https://www.hackerrank.com/challenges/service-lane'''

import sys


n,t = raw_input().strip().split(' ')
n,t = [int(n),int(t)]
width = map(int,raw_input().strip().split(' '))
tests = []
results = []
for a0 in xrange(t):
    i,j = raw_input().strip().split(' ')
    i,j = [int(i),int(j)]
    tests.append((i,j))

for test in tests:
	i,j = test
	current_min = 3
	for index in xrange(i,j+1):
		if width[index] < current_min:
			current_min = width[index]
	results.append(current_min)

for item in results:
	print item