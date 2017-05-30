m,n = [int(v) for v in raw_input().strip().split()]
database = []
for i in xrange(m):
	row = raw_input().strip()
	temp = []
	for j in xrange(len(row)):
		temp.append(row[j])
	database.append(temp)

up_matrix = [[0 for _ in xrange(len(database[0]))] for _ in xrange(len(database))]
left_matrix = [[0 for _ in xrange(len(database[0]))] for _ in xrange(len(database))]

for i in xrange(m):
	for j in xrange(n):
		if database[i][j] == 'x':
			up_matrix[i][j] = -1
			left_matrix[i][j] = -1


for i in xrange(1,len(database)):
	for j in xrange(len(database[0])):
		if up_matrix[i][j] != -1:
			up_matrix[i][j] = up_matrix[i-1][j] + 1
for i in xrange(len(database)):
	for j in xrange(1,len(database[0])):
		if left_matrix[i][j] != -1:
			left_matrix[i][j] = left_matrix[i][j-1] + 1

for row in up_matrix:
	print row
print
for row in left_matrix:
	print row