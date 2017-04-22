#n = int(raw_input().strip())
fish = open('test.txt','r')
n = int(fish.readline().strip())
database = []

def check(string1, string2, memo):
	if (len(string1)-1,len(string2)-1) in memo:
		return memo[(len(string1)-1,len(string2)-1)]
	else:
		if string1 == '' or string2 == '':
			if string1 == '' and string2:
				if string2[-1] == string2[-1].upper():
					print string2[-1]
			elif string2 == '' and string1:
				if string1[-1] == string1[-1].upper():
					print string1[-1]
			memo[(len(string1)-1,len(string2)-1)] = 0
			return memo[(len(string1)-1,len(string2)-1)]
		elif string1[-1].lower() == string2[-1].lower():
			memo[(len(string1)-1,len(string2)-1)] =  1 + check(string1[:-1],string2[:-1],memo)
			return memo[(len(string1)-1,len(string2)-1)]
		else:
			temp = max(check(string1[:-1],string2,memo), check(string1,string2[:-1],memo))
			memo[(len(string1)-1,len(string2)-1)] = temp
			return memo[(len(string1)-1,len(string2)-1)]

for i in xrange(0,n):
	#string1 = raw_input().strip()
	#string2 = raw_input().strip()
	string1 = fish.readline().strip()
	string2 = fish.readline().strip()
	# key - ith row and jth column in the table
	# value - len of the LCS
	memo = {}
	#already checked is a hashtable in the form
	# key - 'bi' - b is the letter and i is the index
	# value - bool
	check(string1,string2,memo)
	print memo[(len(string1)-1, len(string2)-1)]