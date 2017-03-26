n,k = [int(v) for v in raw_input().strip().split()]
queen_row, queen_col = [int(v) for v in raw_input().strip().split()]
obstacles = {key:[] for key in xrange(1,n+1)}
for i in xrange(k):
	row,col = [int(v) for v in raw_input().strip().split()]
	obstacles[row].append(col)
