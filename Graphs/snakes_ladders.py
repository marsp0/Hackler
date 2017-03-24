import sys

def insert(graph,a,b):
	index_list = [x for x in xrange(a-6,a) if x >= 1]

tests = int(raw_input())
test_database = []
for i in xrange(tests):
	graph = {key:[x for x in xrange(key+1,key+7) if x <= 100] for key in xrange(1,101)}
	ladders = int(raw_input().strip())
	for x in xrange(ladders):
		a,b = [int(v) for v in raw_input().strip().split()]
		insert(graph,a,b)
	snakes = int(raw_input().strip())
	for x in xrange(snakes):
		a,b = [int(v) for v in raw_input().strip().split()]
		print a,b