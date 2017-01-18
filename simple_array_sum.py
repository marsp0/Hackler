#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

def get_sum():

	summ = 0
	for item in arr:
		summ += item
	return summ

print get_sum()