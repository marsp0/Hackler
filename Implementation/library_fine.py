#!/bin/python

''' https://www.hackerrank.com/challenges/library-fine '''

import sys


d1,m1,y1 = raw_input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

total = 0
if y1 > y2:
    total += 10000
elif m1 > m2 and y1 == y2:
    total += (m1-m2)*500
elif d1 > d2 and m1 == m2 and y1 == y2:
    total += (d1 - d2) * 15

print total