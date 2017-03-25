n = int(raw_input().strip())
database = {key:0 for key in xrange(1,6)}
birds = [int(v) for v in raw_input().strip().split()]
for bird in birds:
	database[bird] += 1

print database
max_element = database[1]
temp = None
for item in database:
	if database[item] > max_element:
		max_element = database[item]
		temp = item

print temp