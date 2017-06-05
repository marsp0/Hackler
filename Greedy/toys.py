'''https://www.hackerrank.com/challenges/priyanka-and-toys - EASY'''

n = int(raw_input().strip())
array = [int(v) for v in raw_input().strip().split()]
array = sorted(array)
result = 1
max_element = array[0] + 4
for index in xrange(1,len(array)):
	if max_element < array[index]:
		result += 1
		max_element = array[index] + 4
print result