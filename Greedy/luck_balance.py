'''https://www.hackerrank.com/challenges/luck-balance?h_r=next-challenge&h_v=zen - EASY'''

n, k = [int(v) for v in raw_input().strip().split()]
hash_table = {}
for i in xrange(n):
	luck, importance = [int(v) for v in raw_input().strip().split()]
	hash_table[i] = (luck,importance)

array = sorted(hash_table.values(), key = lambda item: item[0])
result = 0
for index in xrange(len(array)-1,-1,-1):
	if array[index][1] == 0:
		result += array[index][0]
	else:
		if k > 0:
			result += array[index][0]
			k -= 1
		else:
			result -= array[index][0]

print result