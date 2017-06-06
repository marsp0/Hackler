'''https://www.hackerrank.com/challenges/greedy-florist - Medium'''

n, k = [int(v) for v in raw_input().strip().split()]
array = [int(v) for v in raw_input().strip().split()]
array = sorted(array,reverse=True)

counter = k
x = 0
result = 0
for i in xrange(len(array)):
	if counter > 0:
		result += (x+1) * array[i]
		counter -= 1
	else:
		counter = k-1
		x += 1
		result += (x+1) * array[i]

print result