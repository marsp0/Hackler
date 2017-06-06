'''https://www.hackerrank.com/challenges/mark-and-toys?h_r=next-challenge&h_v=zen - EASY'''

n, k = [int(v) for v in raw_input().strip().split()]
array = [int(v) for v in raw_input().strip().split()]
array = sorted(array)

result = 0
for item in array:
	if k-item >= 0:
		result += 1
		k -= item
	else:
		break

print result