'''
	https://www.hackerrank.com/challenges/append-and-delete
'''

#!/bin/python

import sys


s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())

common = 0

for i in xrange(len(min(s,t))):
	if s[i] == t[i]:
		common += 1

if ( len(t)+len(s)-2*common ) > k:
	print 'NO'