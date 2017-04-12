input_str = raw_input().strip()
separated_list = []
for element in input_str:
	separated_list.append(element)

memo = {}
temp_sum = 0
for i in xrange(len(separated_list)):
	temp_sum += int(separated_list[i])
	memo[(int(separated_list[i]),0)] = temp_sum
	memo[(0,int(separated_list[i]))] = temp_sum
	memo[(i,i)] = 0

memo[(0,0)] = 0

'''lower_result = temp_sum
higher_result = temp_sum
for i in xrange(len(separated_list)):
	for j in xrange(len(separated_list)):
		if i == j or (i,j) in memo:
			continue
		'''

print len(memo)
print memo
