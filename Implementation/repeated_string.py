#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())

count = 0
if 'a'*len(s) == s:
	count =  n
else:
	count = s.count('a')*(n//len(s))
	count += s[:n%len(s)].count('a')
print count