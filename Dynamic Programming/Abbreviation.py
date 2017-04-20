n = int(raw_input().strip())
for i in xrange(0,n,2):
	str_1 = raw_input().strip()
	str_2 = raw_input().strip()
	# key - ith row and jth column in the table
	# value - [x,y] where x is the length of the longest substring
	#						y is the length of capital letters
	memo = {}
	already_checked = {}
	for i in xrange(len(str_1)):
		for j in xrange(len(str_2)):
			if str_1[i].lower() == str_2[j].lower():
				if i == 0 or j == 0:
					memo[(i,j)] = [1,1]
				else:
					memo[(i,j)] = [memo[(i-1,j-1)][0] + 1, memo[(i-1,j-1)][1] + 1]
				already_checked[j] = True
			else:
				try:
					if memo[(i-1,j)][0] > memo[(i,j-1)][0]:
						temp = (i-1,j)
					else:
						temp = (i,j-1)
					memo[(i,j)] = memo[temp]
					if str_1[i] == str_1[i].upper() and not j in already_checked:
						print already_checked
						memo[(i,j)][1] += 1
				except KeyError:
					memo[(i,j)] = [1,1]

l1 = len(str_1)-1
l2 = len(str_2)-1

print memo[(l1,l2)]
if memo[(l1,l2)][0] != len(str_2) or memo[(l1,l2)][0] != memo[(l1,l2)][1]:
	result = 'NO'
else:
	result = 'YES'
print result
