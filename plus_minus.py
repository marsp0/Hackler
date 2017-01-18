#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

negative = 0.0
positive = 0.0
zero = 0.0

for item in arr:
    if item < 0:
        negative += 1
    elif item > 0:
        positive += 1
    else:
        zero += 1
        
print positive/n
print negative/n
print zero/n