'''https://www.hackerrank.com/challenges/stockmax - MEDIUM'''

tests = int(raw_input().strip())
#fish = open('test.txt','r')
#tests = int(fish.readline().strip())
database = []
for i in xrange(tests):
	n = int(raw_input().strip())
	#n = int(fish.readline().strip())
	array = [int(v) for v in raw_input().strip().split()]
	#array = [int(v) for v in fish.readline().strip().split()]
	result = 0
	while array:
		max_value = max(array)
		max_index = array.index(max_value)
		if max_index != 0:
			sum_before = sum(array[:max_index])
			result += len(array[:max_index])*max_value - sum_before
		else:
			result += 0
		array  = array[max_index+1:]
	database.append(result)

for item in database:
	print item