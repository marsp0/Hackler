import sys
q = int(raw_input().strip())
database = []
for i in xrange(q):
	n = int(raw_input().strip())
	matrix = []
	for row in xrange(n):
		m_row = [int(v) for v in raw_input().strip().split()]
		matrix.append(m_row)
	database.append(matrix)

for item in database:
	matrix = item
	col = 0
	results = []
	max_num = 0
	while col < len(matrix[0]):
		sum_col = 0
		for item in matrix:
			sum_col += item[col]
			if max_num < item[col]:
				max_num = item[col]
		col += 1
		results.append(sum_col)
	if sorted([sum(x) for x in matrix]) == sorted(results):
		print 'Possible'
	else:
		print 'Impossible'