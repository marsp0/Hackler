#!/bin/python

import sys


n = int(raw_input().strip())
arr = [int(v) for v in raw_input().split()]
summ = 0L

for item in arr:
    summ += item
    
print summ