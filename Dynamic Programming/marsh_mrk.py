m,n = [int(v) for v in raw_input().strip().split()]
database = []
for i in xrange(m):
	row = raw_input().strip()
	temp = []
	for j in xrange(len(row)):
		temp.append(row[j])
	database.append(temp)

marsh_database = {}
for i in xrange(m):
	for j in xrange(n):
		if database[i][j] == 'x':
			marsh_database[(i,j)] = True

def is_rekt(database,marsh_database,max_value,top_row,top_col,bot_row,bot_col):
	a = bot_row - top_row
	b = bot_col - top_col
	perim = (2*(a) + 2*(b))
	if perim > max_value:
		border_list = []
		border_list.extend([(top_row,x) for x in xrange(top_col,top_col+bot_col)])
		border_list.extend([(bot_row,x) for x in xrange(top_col,top_col+bot_col)])
		for i in xrange(top_row, bot_row+1):
			border_list.append((i,top_col))
			border_list.append((i,bot_col))
		for item in border_list:
			if item in marsh_database:
				return False
		return perim

def get_rekt(database,marsh_database):
	max_value = 0
	for i in xrange(len(database)):
		for j in xrange(len(database[0])):
			for k in xrange(i+1,len(database)):
				for m in xrange(j+1,len(database[0])):
					if i == 2 and j == 3:
					result = is_rekt(database,marsh_database,max_value,i,j,k,m)
					if result:
						max_value = result
	return max_value

max_value = get_rekt(database,marsh_database)

if max_value == 0:
	print 'impossible'
else:
	print max_value