#!/bin/python

'''https://www.hackerrank.com/challenges/hackerland-radio-transmitters'''

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
x = map(int,raw_input().strip().split(' '))

x = sorted(x)
transmitters = 0
current = None
prev_current = None
starting = 0
index = 0
while index < n:
	try:
		if current == None:
			if x[starting] + k >= x[index+1]:
				index += 1
			else:
				current = index
				transmitters += 1
		else:
			if x[current] + k >= x[index+1]:
				index += 1
			else:
				prev_current = current
				current = None
				starting = index+1
	except IndexError:

		if current != None:
			if x[current] + k >= x[index]:
				break
			else:
				transmitters += 1
				break
		else:
			if prev_current == None:
				transmitters += 1
				break
			else:
				if x[prev_current] + k >= x[index]:
					break
				else:
					transmitters += 1
					break
 
print transmitters