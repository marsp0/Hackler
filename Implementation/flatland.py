#!/bin/python
'''https://www.hackerrank.com/challenges/flatland-space-stations'''
import sys
from math import ceil

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
c = map(int,raw_input().strip().split(' '))

def quick(array):

	if len(array) <= 1:
		return array
	else:
		less = []
		more =  []
		same = []
		pivot = array[0]

		for item in array:
			if item < pivot:
				less.append(item)
			elif item > pivot:
				more.append(item)
			else:
				same.append(item)

		less = quick(less)
		more = quick(more)

		return less + same + more

c = quick(c)
current_max = 0
for index in xrange(1,len(c)):
	if c[index] - c[index-1] > current_max:
		current_max = c[index] - c[index-1]

current_max = int(ceil(current_max//2))
if current_max == 1:
	current_max = 1

if c[0] - 1 > current_max:
	current_max = c[0]
if n - c[-1] > current_max:
	current_max = n-c[-1]-1
print c
print current_max