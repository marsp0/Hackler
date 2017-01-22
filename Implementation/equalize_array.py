'''https://www.hackerrank.com/challenges/equality-in-a-array'''

from collections import defaultdict

n = int(raw_input().strip())
c = [int(v) for v in raw_input().strip().split()]
result = defaultdict(int)
for item in c:
	result[item] += 1

current_max = 0
for item in result:
	if result[item] > current_max:
		current_max = result[item]

print len(c) - current_max

