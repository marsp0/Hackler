#!/bin/python

import sys


a = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

a = [int(v) for v in raw_input().split()]
b = [int(v) for v in raw_input().split()]

alice = 0
bob = 0

for i in xrange(3):
	if a[i] < b[i]:
		bob += 1
	elif a[i] > b[i]:
		alice += 1
	else:
		pass

print alice, bob