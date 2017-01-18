#!/bin/python

import sys


len_ints,len_rotations,index = raw_input().strip().split(' ')
len_ints,len_rotations,index = [int(len_ints),int(len_rotations),int(index)]
a = map(int,raw_input().strip().split(' '))

for x in xrange(len_rotations):
	a.insert(0,a.pop())


for a0 in xrange(index):
    m = int(raw_input().strip())
    print a[m]