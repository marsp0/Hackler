#Input from the exercise
input_str = raw_input().strip()

#we separate string into and make it a list
separated_list = []
for element in input_str:
	separated_list.append(element)

memo = {}
temp_sum = 0
for i in xrange(len(separated_list)):
	temp_sum += int(separated_list[i])
	memo[(i+1,0)] = temp_sum
	memo[(0,i+1)] = temp_sum
	memo[(i,i)] = 0

memo[(0,0)] = 0
memo[(0,len(separated_list))] = temp_sum 
memo[(len(separated_list),0)] = temp_sum 
memo[(len(separated_list), len(separated_list))] = 0

lower_result = temp_sum
higher_result = temp_sum
flag = False
for i in xrange(len(separated_list)+1):
	for j in xrange(len(separated_list)+1):
		if i == j or (i,j) in memo:
			if i ==j:
				flag = True
			continue
		if j > i:
			if flag == True:
				memo[(i,j)] = memo[(i-1,len(separated_list))] + int(''.join(separated_list[i-1:j]))
				flag = False
			else:
				memo[(i,j)] = memo[(i,j-1)] + int(''.join(separated_list[i-1:j]))

print memo[len(separated_list)-1, len(separated_list)]