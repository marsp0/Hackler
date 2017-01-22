#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
current_cloud = 0
jumps = 0
while current_cloud < len(c)-1:
	if current_cloud+2 < (len(c) -1) and c[current_cloud+2] == 1 :
		current_cloud += 1
		jumps += 1
	else:
		current_cloud += 2
		jumps += 1
print jumps