#!/bin/python

'''https://www.hackerrank.com/challenges/2d-array'''

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

for item in reversed(arr):
	print item,