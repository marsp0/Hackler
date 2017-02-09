'''https://www.hackerrank.com/challenges/missing-numbers'''

n = int(raw_input().strip())
first = [int(v) for v in raw_input().strip().split()]
m = int(raw_input().strip())
second = [int(v) for v in raw_input().strip().split()]

numbers_second = {}
numbers_first = {}
for number in second:
	try:
		numbers_second[number] += 1
	except KeyError:
		numbers_second[number] = 1

for number in first:
	try:
		numbers_first[number] += 1
	except KeyError:
		numbers_first[number] = 1

results = []
for number in numbers_second:
	try:
		if numbers_first[number] != numbers_second[number]:
			results.append(number)
	except KeyError:
		results.append(number)

results = sorted(results)
for item in results:
	print item,