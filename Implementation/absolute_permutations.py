tests = int(raw_input().strip())
test_database = []
for i in xrange(tests):
	n,k = [int(v) for v in raw_input().strip().split()]
	test_database.append((n,k))

for test in test_database:
	n,k = test
	if k == 0:
		for i in xrange(1,n+1):
			print i,
		print
		continue
	positions = {key:[] for key in xrange(1,n+1)}
	for number in xrange(1,n+1):
		try:
			if number + k < n+1 and n >= 1:
				positions[number + k].append(number)
		except KeyError:
			pass
		try:
			if number + k < n+1 and n >= 1:
				positions[number - k].append(number)
		except KeyError:
			pass
	results = [0] * n
	doubles = []
	placed = {}
	for i in xrange(1,n+1):
		value_list = positions[i]
		if not value_list:
			print -1
			break
		else:
			if len(value_list) == 1:
				results[i-1] = value_list[0]
				placed[value_list[0]] = True
			else:
				doubles.append(i)
	index = 0
	while doubles:
		print index, doubles, results
		try:
			position_number = doubles[index]
			print position_number
			possible_numbers = positions[doubles[index]]
			print possible_numbers
			for item in xrange(len(possible_numbers)):
				print possible_numbers[item], placed, 'dsads'
				if possible_numbers[item] in placed:
					print 'was here'
					if item == 0:
						results[position_number] = possible_numbers[item+1]
						placed[possible_numbers[item+1]] = True
						doubles.pop(index)
					else:
						results[position_number] = possible_numbers[item-1]
						placed[possible_numbers[item-1]] = True
						doubles.pop(index)
			index += 1
		except IndexError:
			index = 0
	print results