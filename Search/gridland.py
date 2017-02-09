n,m,k = [int(v) for v in raw_input().strip().split()]
database = {}
for train in xrange(k):
	row, col1, col2 = [int(v) for v in raw_input().strip().split()]
	database[train] = [row-1,col1-1,col2-1]

occupied = {}
lamps = 0
for train in database:
	row, col1, col2 = database[train]
	try:
		#odds are ends, evens are starts
		row_elements = occupied[row]
		for index in xrange(len(row_elements)):
			if col1 < row_elements[index]:
				if index % 2 == 0:
					start = index
					if col2 < row_elements[index+1]:
						row_elements[index] = col1
					else:
						while index < len(row_elements) and col2 > row_elements[index]:
							index += 1
						if (index) % 2 == 0:
							row_elements[index-1] = col2
							temp = start
							while temp < index:
								row_elements.pop(start)
								temp += 1
						else:
							temp = start
							while temp < index:
								row_elements.pop(start)
								temp += 1
							row_elements.insert(start,col1)
					break
				else:
					start = index
					if col2 < row_elements[index]:
						break
					else:
						while index < len(row_elements) and col2 > row_elements[index]:
							index += 1
						if index % 2 == 0:
							row_elements[index-1] = col2
							temp = start
							while temp < index:
								row_elements.pop(start)
								temp += 1
						else:
							temp = start
							while temp < index:
								row_elements.pop(start)
								temp += 1
							row_elements.insert(start,col1)							
					break
					
	except KeyError:
		lamps += (col2 - col1)
		occupied[row] = [col1,col2]
print occupied
not_lamps = 0
for key in occupied:
	for index in xrange(1,len(occupied[key]),2):
		not_lamps += (occupied[key][index] - occupied[key][index-1]) + 1

print n*m - not_lamps