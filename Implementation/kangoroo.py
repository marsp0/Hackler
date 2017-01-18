#!/bin/python

import sys

def kangoroo():

	x1,v1,x2,v2 = raw_input().strip().split(' ')
	x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

	if v2 >= v1:
	    return 'NO'
	else:
		for i in xrange(10000):
			if x1 == x2:
				return 'YES'
			x1 = x1+v1
			x2 = x2+v2
	return 'NO'

print kangoroo()