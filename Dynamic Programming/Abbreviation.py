#n = int(raw_input().strip())
fish = open('test.txt','r')
n = int(fish.readline().strip())
database = []
for i in xrange(0,n):
	#str_1 = raw_input().strip()
	#str_2 = raw_input().strip()
	str_1 = fish.readline().strip()
	str_2 = fish.readline().strip()
	# key - ith row and jth column in the table
	# value - len of the LCS
	memo = {}
	#already checked is a hashtable in the form
	# key - 'bi' - b is the letter and i is the index
	# value - bool
	already_checked = {}
	counter = 0
	for i in xrange(len(str_1)):
		if str_1[i] == str_1[i].upper():
			counter += 1
	print counter
	for i in xrange(len(str_1)):
		for j in xrange(len(str_2)):
			if str_1[i].lower() == str_2[j].lower():
				if i == 0 or j == 0:
					memo[(i,j)] = 1
				else:
					memo[(i,j)] = memo[(i-1,j-1)] + 1
				key = '{}{}'.format(str_1[i].lower(),i)
				if not key in already_checked:
					#print key
					already_checked[key] = True
			else:
				try:
					if memo[(i-1,j)]> memo[(i,j-1)]:
						temp = (i-1,j)
					else:
						temp = (i,j-1)
					memo[(i,j)] = memo[temp]
				except KeyError:
					memo[(i,j)] = 1
				#print str_1[i], i, '1'
				if str_1[i] == str_1[i].upper():
					#print str_1[i], i, '2'
					key = '{}{}'.format(str_1[i].lower(),i)
					if not key in already_checked:
						already_checked[key] = True
	l1 = len(str_1)-1
	l2 = len(str_2)-1
	if memo[(l1,l2)] == len(str_2) and len(already_checked) == len(str_2):
		result = 'YES'
	else:
		result = 'NO'
	print result
	#print str_1, str_2
	print len(already_checked), len(str_2), len(str_1)
	print