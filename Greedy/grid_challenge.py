'''https://www.hackerrank.com/challenges/grid-challenge - EASY'''

tests = int(raw_input().strip())
test_database = []
for test in xrange(tests):
	rows = int(raw_input().strip())
	database = []
	for i in xrange(rows):
		database.append(raw_input())
	database[0] = sorted(database[0])
	test_database.append(database)

for test in test_database:
	database = test
	break_statement = False
	result = 'NO'
	for i in xrange(1,len(database)):
		database[i] = sorted(database[i])
		for j in xrange(len(database[i])):
			if database[i][j] < database[i-1][j]:
				break_statement = True
				result = 'NO'
		if break_statement:
			break
	if not break_statement:
		result = 'YES'
	print result