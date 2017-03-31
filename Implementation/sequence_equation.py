n = int(raw_input().strip())
numbers = [int(v) for v in raw_input().strip().split()]

results = {key: None for key in xrange(1,n+1)}
for index in xrange(len(numbers)):
	to_save = numbers[numbers[index]-1]
	results[to_save] = index+1

for i in xrange(1,len(numbers)+1):
	print results[i]