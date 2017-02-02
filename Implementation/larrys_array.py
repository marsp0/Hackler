test_cases = int(raw_input().strip())
tests = {}
results = []
for test in xrange(test_cases):
	n = int(raw_input().strip())
	array = [int(v) for v in raw_input().strip().split()]
	tests[test] = [n,array]

for test in tests:
	n,array = tests[test]
	index = len(array)-1
	while index > 1:
		print 'Checking if the subpart is sorted - {}'.format(array[index-2:index+1])
		if array[index-2:index+1] == sorted(array[index-2:index+1]):
			index -= 1
			continue
		else:
			print 'The subpart was not sorted'
			temp_dict = {}

			for i in xrange(3):
				print 'Before rotation - {}'.format(array[index-2:index+1])
				array[index-2], array[index-1], array[index] = array[index-1], array[index], array[index-2]
				print 'After rotation - {}'.format(array[index-2:index+1])
				print 'Checking if sorted'
				if array[index-2:index+1] == sorted(array[index-2:index+1]):
					print 'It was, breaking out of inner loop'
					break
				else:
					print 'It was not, saving the subpart in the dict'
					temp_dict[i] = array[index-2:index+1]
					continue
			print'Checking to see if we have tried all rotations'
			if i == 2:
				print 'We have, searching for max element'
				max_element = max(temp_dict[i])
				for key in temp_dict:
					print 'Checking if {} is the max element rotation'.format(array[index-2:index+1])
					if temp_dict[key][2] == max_element:
						print 'It was, breaking'
						array[index-2:index+1] = temp_dict[key]
						break
		index -=1
	print array
	if sorted(array) == array:
		results.append('YES')
	else:
		results.append('NO')
for item in results:
	print item