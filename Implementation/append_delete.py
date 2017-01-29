'''
	https://www.hackerrank.com/challenges/append-and-delete
'''

#!/bin/python

import sys


s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())

common = 0

for i in xrange(min(len(t),len(s))):
	if s[i] == t[i]:
		common += 1

if (len(t)+len(s)-2*common ) > k:
	print 'No'
elif (len(s)+len(t)-2*common)%2 == k%2:
	print 'Yes'
elif (len(s) + len(t) - k) < 0:
	print 'Yes'
else:
	print 'No'