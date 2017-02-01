'''https://www.hackerrank.com/challenges/s10-weighted-mean'''

n = int(raw_input().strip())
array = [int(v) for v in raw_input().strip().split()]
weights = [int(v) for v in raw_input().strip().split()]
multiplication_array = []
for i in xrange(n):
	multiplication_array.append(array[i]*weights[i])

print '%.1f' % (sum(multiplication_array)/float(sum(weights)))