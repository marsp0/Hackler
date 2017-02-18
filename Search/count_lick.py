''' https://www.hackerrank.com/challenges/count-luck '''

''' more info on backtracking here : https://en.wikipedia.org/wiki/Backtracking and https://www.cs.bu.edu/teaching/alg/maze/'''
import subprocess
import time
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
	#if you want to animate the process just uncomment these and watch the command line
	#for item in graph:
	#	print item
	#subprocess.call(['clear'])
	#time.sleep(1)
	if start_x < 0 or start_x > len(graph[0])-1 or start_y < 0 or start_y > len(graph)-1:
		return False
	if graph[start_y][start_x] == '*':
		return True
	if graph[start_y][start_x] == 'X':
		return False
	if graph[start_y][start_x] in ('.','M','*'):
		graph[start_y][start_x] = '+'
		path.append((start_y,start_x))
		if find_path(start_x,start_y-1,graph):
			return True
		if find_path(start_x+1,start_y,graph):
			return True
		if find_path(start_x,start_y+1,graph):
			return True
		if find_path(start_x-1,start_y,graph):
			return True
		graph[start_y][start_x] = '.'
		path.pop()
	return False

def check_point(start_x,start_y):
	if start_x < 0 or start_y < 0 or start_y > len(graph)-1 or start_x > len(graph[0])-1:
		return 0
	elif graph[start_y][start_x] in ('X','+','*'):
		return 0
	else:
		return 1

def check_path(path):
	counter = 0
	for item in path:
		start_y,start_x = item
		temp = 0
		temp += check_point(start_x,start_y-1)
		temp += check_point(start_x+1,start_y)
		temp += check_point(start_x,start_y+1)
		temp += check_point(start_x-1,start_y)
		if temp > 0:
			counter += 1
	return counter


results = []
for test in database:
	graph = database[test]
	path = []
	start_x,start_y = starts[test]
	find_path(start_x,start_y,graph)
	print graph
	if impressed[test] == check_path(path):
		results.append('Impressed')
	else:
		results.append('Oops!')

for item in results:
	print item