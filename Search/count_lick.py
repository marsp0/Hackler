''' https://www.hackerrank.com/challenges/count-luck '''

''' more info on backtracking here : https://en.wikipedia.org/wiki/Backtracking and https://www.cs.bu.edu/teaching/alg/maze/'''

tests = int(raw_input().strip())
database = {}
impressed = {}
starts = {}
for test in xrange(tests):
	n, m = [int(v) for v in raw_input().strip().split()]
	temp = []
	for y in xrange(n):
		row = [v for v in raw_input().strip()]
		try :
			starts[test]
		except KeyError:
			try:
				x = row.index('M')
				starts[test] = (x,y)
			except ValueError:
				pass
		temp.append(row)
	impressed[test] = int(raw_input().strip())
	database[test] = temp

def find_path(start_x,start_y,graph):
	print start_y,start_x
	for item in graph:
		print item
	if start_x < 0 or start_x > len(graph[0])-1 or start_y < 0 or start_y > len(graph)-1:
		print 'outside of graph'
		return False
	if graph[start_y][start_x] == '*':
		print 'Goal'
		return True
	if graph[start_y][start_x] == 'X':
		print 'Wall'
		return False
	if graph[start_y][start_x] in ('.','M'):
		graph[start_y][start_x] = '+'
		for item in graph:
			print item
		print 'going north'
		if find_path(start_x,start_y-1,graph):
			return True
		print 'going east'
		if find_path(start_x+1,start_y,graph):
			return True
		print 'going south'
		if find_path(start_x,start_y+1,graph):
			return True
		print 'going west'
		if find_path(start_x-1,start_y,graph):
			return True
	print 'Turning it down'
	graph[start_y][start_x] = 'X'
	return False

for test in database:
	graph = database[test]
	start_x,start_y = starts[test]
	find_path(start_x,start_y,graph)
	print graph