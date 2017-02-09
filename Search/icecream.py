trips = int(raw_input().strip())
database = {}

def find_choice(array,number,excluded):
	for index in xrange(len(array)):
		if index != excluded:
			if array[index] == number:
				return index
	return False

for trip in xrange(trips):
	m = int(raw_input().strip())
	n = int(raw_input().strip())
	array = [int(v) for v in raw_input().strip().split()]
	database[trip] = (m,array)
results = []
for trip in database:
	m,array = database[trip]
	to_find = m - array[0]
	excluded = 0
	index = 1
	while True:
		result = find_choice(array,to_find, excluded)
		if result == False:
			to_find = m - array[excluded+1]
			excluded += 1
		else:
			results.append([excluded+1,result+1])
			break

for item in results:
	print ' '.join(map(str,item))