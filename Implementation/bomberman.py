r,c,n = [int(v) for v in raw_input().strip().split()]
city_map = []
for i in xrange(r):
	row = raw_input().strip()
	temp = []
	for j in row:
		temp.append(j)
	city_map.append(temp)
if n > 1:
	n = n % 4 + 4
time_database = {key:{} for key in xrange(1,n+6)}

for row in xrange(len(city_map)):
	for col in xrange(len(city_map[row])):
		if city_map[row][col] == 'O':
			time_database[3][(row,col)] = True

def plant_field(city_map,time_database,current_time):
	#print current_time, 'planting'
	for row in xrange(len(city_map)):
		for col in xrange(len(city_map[row])):
			if city_map[row][col] == '.':
				time_database[current_time+3][(row,col)] = True
				city_map[row][col] = 'O'

def detonate(city_map,time_database,current_time):
	#print current_time, 'detonate'
	for item in time_database[current_time]:
		row,col = item
		city_map[row][col] = '.'
		to_check = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
		for tile in to_check:
			try:
				row,col = tile
				if row != -1 and col != -1:
					city_map[row][col] = '.'
					del time_database[current_time+2][(row,col)]
			except IndexError:
				continue
			except KeyError:
				continue
if n == 2:
	plant_field(city_map,time_database,n)
elif n == 1:
	pass
elif n%2 == 0:
	plant_field(city_map,time_database,n)
else:
	for i in xrange(2,n+1):
		#print i
		#for item in city_map:
		#	print ''.join(item)
		#print
		#for item in time_database:
		#	print item, time_database[item]
		#print
		if i % 2 == 0:
			plant_field(city_map,time_database,i)
		if time_database[i]:
			detonate(city_map,time_database,i)

for item in city_map:
	print ''.join(item)
#print time_database[198]