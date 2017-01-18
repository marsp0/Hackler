#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

forward_counter = 0
backward_counter = n - 1

diag_1 = 0
diag_2 = 0

for row in a:
	diag_1 += row[forward_counter]
	diag_2 += row[backward_counter]
	forward_counter += 1
	backward_counter -= 1

print abs(diag_2 - diag_1)
