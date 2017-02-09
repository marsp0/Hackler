from collections import defaultdict

'''https://www.hackerrank.com/challenges/gridland-metro'''


n,m,k = [int(v) for v in raw_input().strip().split()]
database = {}
for train in xrange(k):
	row, col1, col2 = [int(v) for v in raw_input().strip().split()]
	database[train] = [row-1,col1-1,col2-1]
occupied = {}

for train in database:
	row, col1, col2 = database[train]
	#print occupied
	try:
		#print occupied[row][0] > col1
		if col1 <= occupied[row][1]:	
			if col1 < occupied[row][0]:
				occupied[row][0] = col1
			if col2 > occupied[row][1]:
				#print 'was here'
				occupied[row][1] = col2
		else:
			occupied[row].extend([col1,col2])
	except KeyError:
		occupied[row] = [col1, col2]

no_lamps = 0
for row in occupied.values():
	for number in xrange(0,len(row),2):
		no_lamps += row[number+1] - row[number] + 1

print n*m - no_lamps