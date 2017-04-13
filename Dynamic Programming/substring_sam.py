import math

#Input from the exercise
input_str = raw_input().strip()
#input_str = open('test.txt','r').read()

#we separate string into and make it a list
separated_list = []
for element in input_str:
	separated_list.append(element)

memo = {}
temp_sum = 0
for i in xrange(len(separated_list)):
	temp_sum += int(separated_list[i])
	memo[(0,i+1)] = temp_sum
	memo[(i,i)] = 0

memo[(0,0)] = 0
memo[(0,len(separated_list))] = temp_sum 
memo[(len(separated_list), len(separated_list))] = 0

mod_value = int(math.pow(10,9)+7)
flag = False
result = temp_sum
#for i in xrange(len(separated_list)+1):
#	for j in xrange(len(separated_list)+1):
#		if i == j or (i,j) in memo:
#			continue
#		if j > i:
#			result = (result + int(input_str[i-1:j])) % mod_value
#			print result

result = {-1:0}
for i in xrange(len(separated_list)):
	print i
	temp = 10*result[i-1] + (i+1)*int(separated_list[i]) % mod_value
	result[i] = temp


print sum(result.values()) % mod_value