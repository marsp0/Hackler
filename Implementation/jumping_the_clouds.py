'''
	https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited
'''

#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))
energy = 100
i = 0
while True:
	energy -= 1
	if c[i] == 1:
		energy -= 2
	if (i + k)%n == 0:
		break
	i += k
print energy

