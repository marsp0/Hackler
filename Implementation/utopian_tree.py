#!/bin/python

import sys


t = int(raw_input().strip())
arr = []
for a0 in xrange(t):
    current = 1
    n = int(raw_input().strip())
    for i in xrange(0,n-1,2):
        current *= 2
        current += 1
    if n%2 == 1:
    	current *= 2
    arr.append(current)

for item in arr:
	print item