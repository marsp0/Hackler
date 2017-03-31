#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
height = map(int, raw_input().strip().split(' '))
# your code goes here
counter = 0
for item in height:
	if item > k:
		while item > k:
			counter += 1
			k +=1
print counter