n, m, k = [int(v) for v in raw_input().strip().split()]
database_fishes = {}
graph = {key : [] for key in xrange(n)}
purchased_fish = {}
for index in xrange(n):
	temp = [int(v) for v in raw_input().strip().split()]
	fishes = temp[1:]
	database_fishes[index] = fishes

for index in xrange(m):
	a,b,c = [int(v) for v in raw_input().strip().split()]
	graph[a-1].append((b-1,c))
	graph[b-1].append((a-1,c))

print graph
print database_fishes