#!/bin/python

'''https://www.hackerrank.com/challenges/taum-and-bday'''

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
	black,white = raw_input().strip().split(' ')
	black,white = [long(black),long(white)]
	cost_b,cost_w,cost_conv = raw_input().strip().split(' ')
	cost_b,cost_w,cost_conv = [long(cost_b),long(cost_w),long(cost_conv)]
	result = 0
	if cost_b < cost_w:
		result += black*cost_b
		if cost_w > (cost_conv+cost_b):
			result += (white*cost_conv + white*cost_b)
		else:
			result += cost_w*white
	else:
		result += white*cost_w
		if cost_b > (cost_conv+cost_w):
			result += (black*cost_conv + black*cost_w)
		else:
			result += cost_b*black
	print result