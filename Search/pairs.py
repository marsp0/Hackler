'''https://www.hackerrank.com/challenges/pairs'''

n, k = [int(v) for v in raw_input().strip().split()]
array = [int(v) for v in raw_input().strip().split()]

hash_table = {key:0 for key in array}
pairs = 0
for number in array:
	to_find = number + k
	try:
		hash_table[to_find]
		pairs += 1
	except KeyError:
		continue

print pairs