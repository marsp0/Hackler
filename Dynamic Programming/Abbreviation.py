'''https://www.hackerrank.com/challenges/abbr'''

import sys

sys.setrecursionlimit(100000)

#n = int(raw_input().strip())
fish = open('test.txt','r')
n = int(fish.readline().strip())

def checker(string1,string2,memo):
	if (len(string1)-1,len(string2)-1) in memo:
		return memo[(len(string1)-1,len(string2)-1)]
	else:
		if len(string2) > len(string1):
			memo[(len(string1)-1,len(string2)-1)] = False
			return False
		elif string1 == '':
			if string2 == '':
				memo[(0,0)] = True
				return True	
			memo[(0,len(string2)-1)] = False
			return False
		elif string2 == '':
			for item in string1:
				if item == item.upper():
					memo[(len(string1)-1,0)] = False
					return False
			memo[(len(string1)-1,0)] = True
			return True
		elif string1[-1] == string1[-1].upper():
			if string1[-1] != string2[-1]:
				memo[(len(string1)-1,len(string2)-1)] = False
				return False
			else:
				memo[(len(string1)-1,len(string2)-1)] = checker(string1[:-1],string2[:-1],memo)
				return memo[(len(string1)-1,len(string2)-1)]
		else:
			if string1[-1].lower() == string2[-1].lower():
				without = checker(string1[:-1],string2,memo)
				with_ = checker(string1[:-1],string2[:-1],memo)
				if without:
					memo[(len(string1)-1, len(string2)-1)] = without
					return without
				memo[(len(string1)-1, len(string2)-1)] = with_
				return with_
			else:
				memo[(len(string1)-1,len(string2)-1)] = checker(string1[:-1],string2,memo)
				return memo[(len(string1)-1,len(string2)-1)]


for i in xrange(0,n):
	#string1 = raw_input().strip()
	#string2 = raw_input().strip()
	string1 = fish.readline().strip()
	string2 = fish.readline().strip()
	memo = {}
	checker(string1,string2,memo)
	if memo[(len(string1)-1,len(string2)-1)]:
		print 'YES'
	else:
		print 'NO'