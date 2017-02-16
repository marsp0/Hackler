''' https://www.hackerrank.com/challenges/count-luck '''

''' more info on backtracking here : https://en.wikipedia.org/wiki/Backtracking and https://www.cs.bu.edu/teaching/alg/maze/'''

tests = int(raw_input().strip())
database = {}
impressed = {}
starts {}
goals = {}
for test in xrange(tests):
	n, m = [int(v) for v in raw_input().strip().split()]
	temp = []
	for x in xrange(n):
		row = raw_input().strip().split()
		try :
			starts[test]
		except KeyError:
			y = row.find('M')
			starts[test] = (x,y)
		try:
			goals[test]
		except KeyError:
			y = row.find('*')
			goals[test] = (x,y)
		temp.append(row)
	impressed[test] = int(raw_input().strip())
	database[test] = temp

def find_path(start_x,start_y,goal_x,goal_y,graph):
	pass

results = []
for test in database:
	graph = database[test]
	start_x,start_y = starts[test]
	goal_x,goal_y = goals[test]
	counter = find_path(start_x,start_y,goal_x,goal_y,graph)
	results.append(counter)