n = int(raw_input().strip())
ints = [int(v) for v in raw_input().strip().split()]
ints = sorted(ints)
counter = 0
database_counters = []
temp = []
for index in xrange(len(ints)):
	if not temp:
		temp.append(ints[index])
		counter = 1
	else:
		if ints[index] - temp[0] in (0,1):
			temp.append(ints[index])
			counter += 1
		else:
			database_counters.append(counter)
			counter = 1
			temp = [ints[index]]

if not database_counters:
	database_counters.append(counter)

print max(database_counters)