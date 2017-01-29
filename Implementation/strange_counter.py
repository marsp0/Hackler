#!/bin/python
'''https://www.hackerrank.com/challenges/strange-code'''

import sys
from math import ceil, log

t = int(raw_input().strip())

column = ceil(log(float(t)/3+1,2))
numbers_col = 3*(2**(column-1))
start_index = numbers_col - 2
print int(numbers_col - ( t - start_index ))