'''https://www.hackerrank.com/challenges/countingsort3'''

n = int(raw_input().strip())
array = []
#get the input
for i in xrange(n):
	number, string = raw_input().strip().split()
	array.append(int(number))
#create the result array
result = [0 for v in xrange(100)]
#count the items
for item in array:
	result[item] += 1

counter  = 0
for item in xrange(len(result)):
	counter += result[item]
	print counter,