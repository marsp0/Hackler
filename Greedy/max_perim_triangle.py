'''https://www.hackerrank.com/challenges/maximum-perimeter-triangle - Easy'''

n = int(raw_input().strip())
array = [int(v) for v in raw_input().strip().split()]
array = sorted(array,reverse=True)
result = None
for index in xrange(len(array)-2):
	if array[index] < (array[index+1]+array[index+2]):
		result = [array[index+2],array[index+1],array[index]]
		break
if result:
	for item in result:
		print item,
else:
	print -1
