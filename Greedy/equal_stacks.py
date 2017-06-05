'''https://www.hackerrank.com/challenges/equal-stacks - easy'''

n,k,m = [int(v) for v in raw_input().strip().split()]
array_1 = [int(v) for v in raw_input().strip().split()]
array_1 = list(reversed(array_1))
array_2 = [int(v) for v in raw_input().strip().split()]
array_2 = list(reversed(array_2))
array_3 = [int(v) for v in raw_input().strip().split()]
array_3 = list(reversed(array_3))
sum_1 = sum(array_1)
sum_2 = sum(array_2)
sum_3 = sum(array_3)

while True:
	try:
		#print sum_1 == sum_2 == sum_3
		#print sum_1, sum_2, sum_3
		if sum_1 == sum_2 == sum_3:
			result = sum_1
			break
		else:
			if sum_1 == max(sum_1,sum_3,sum_2):
				sum_1 -= array_1.pop()
			elif sum_2 == max(sum_1,sum_2,sum_3):
				sum_2 -= array_2.pop()
			elif sum_3 == max(sum_1,sum_2,sum_3):
				sum_3 -= array_3.pop()
	except IndexError:
		result = 0
		break
print result
