''' https://www.hackerrank.com/challenges/connected-cell-in-a-grid 
	This challenge uses an algorithm called flood_fill. More info on it can be found here :
	https://en.wikipedia.org/wiki/flood_fill
'''

n = int(raw_input().strip())
m = int(raw_input().strip())
graph = []
for row in xrange(n):
	graph.append([int(v) for v in raw_input().strip().split()])

def flood_fill(i,j):
	if i >= n or j >= m or graph[i][j] == -1 or graph[i][j] == 0 or i< 0 or j < 0:
		return 0
	else:
		graph[i][j] = -1
		return 1 + flood_fill(i-1,j-1) + flood_fill(i-1,j) + flood_fill(i-1,j+1) + \
				flood_fill(i,j-1) + flood_fill(i,j+1) + flood_fill(i+1,j-1) + flood_fill(i+1,j) + flood_fill(i+1,j+1)
results = []
for i in xrange(n):
	for j in xrange(m):
		temp = flood_fill(i,j)
		results.append(temp)

print max(results)