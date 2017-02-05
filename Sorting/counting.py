from collections import defaultdict

n = int(raw_input().strip())
array = [int(v) for v in raw_input().strip().split()]
result = [0 for _ in xrange(100)]
for item in array:
	result[item] += 1

print ' '.join(map(str,result))