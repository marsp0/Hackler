from itertools import permutations

test_cases = int(raw_input().strip())

result_list = []

for i in xrange(test_cases):
	string = raw_input().strip()
	perm = permutations(string)
	condition = True
	while condition:
		temp = perm.next()
		if ''.join(temp) == string:
			try:
				result = ''.join(perm.next())
				condition = False
				if result == string:
					result = 'no answer'
				result_list.append(result)
			except StopIteration:
				continue

for item in result_list:
	print item