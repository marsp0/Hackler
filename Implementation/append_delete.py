'''
	https://www.hackerrank.com/challenges/append-and-delete
'''

#NOTE : this could be refactored heavily, did the challenge when was in the aeroport in Bucharest. We can use the idea of odd/even strings that are not common and the odd/even k
#!/bin/python

import sys


s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())

not_common = 0
if len(s) < len(t):
	min_str = s
	max_str = t
else:
	min_str = t
	max_str = s
for i in xrange(len(min_str)):
	if s[i] != t[i]:
		not_common = len(max_str) - i
		break
if len(s) != len(t):
	not_common += len(max_str) - len(min_str)

if not_common == 0:
	print 'Yes'
elif len(s) != len(t):
	if min_str + max_str[len(min_str):] == max_str:
		if k % 2 == 0 and not_common % 2 == 0:
			print 'Yes'
		else:
			if len(max_str[len(min_str):]) == k:
				print 'Yes'
			elif (k - not_common) % 2 == 0:
				print 'Yes'
			elif not_common % 2 == 0 and k % 2 == 1:
				print 'Yes'
			elif not_common % 2 == 1 and k % 2 == 0:
				if not_common*2 + len(min_str) * 2 <= k:
					print 'Yes'
				else:
					print 'No'
			else:
				print 'No'
	else:
		if abs(not_common + (not_common - len(max_str)-len(min_str))) == k:
			print 'Yes'
		else:
			print 'No'
else:
	if 2*not_common == k:
		print 'Yes'
	else:
		if k > 2*not_common:
			print 'Yes'
		else:
			print 'No'