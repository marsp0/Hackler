#!/bin/python

'''https://www.hackerrank.com/challenges/happy-ladybugs'''

import sys

tests = {}
Q = int(raw_input().strip())
for a0 in xrange(Q):
	n = int(raw_input().strip())
	b = raw_input().strip()
	tests[a0] = b
result = []
for test in tests.values():
	answer = ''
	temp = []
	if len(test) > 1:
		for char in xrange(len(test)):
			try:
				if test[char] == test[char+1] or test[char-1] == test[char]:
					answer = 'YES'
				else:
					answer = 'NO'
					break
			except IndexError:
				if char == 0:
					if test[char] == test[char+1]:
						answer = 'YES'
					else:
						answer = 'NO'
						break
				else:
					if test[char] == test[char-1]:
						answer = 'YES'
					else:
						answer = 'NO'
						break
	if answer == 'YES':
		result.append(answer)
		continue
	underscore = test.count('_')
	if underscore == 0:
		answer = 'NO'
		result.append(answer)
		continue
	temp.append('_')
	for char in test:
		if char not in temp:
			if test.count(char) == 1:
				answer = 'NO'
				break
			temp.append(char)
		answer = 'YES'
	result.append(answer)

for item in result:
	print item