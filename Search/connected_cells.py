''' https://www.hackerrank.com/challenges/connected-cell-in-a-grid 
	This challenge uses an algorithm called FloodFill. More info on it can be found here :
	https://en.wikipedia.org/wiki/Flood_fill
'''

n = int(raw_input().strip())
m = int(raw_input().strip())
graph = []
for row in xrange(n):
	graph.append([int(v) for v in raw_input().strip().split()])

print graph