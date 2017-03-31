n,o = [int(v) for v in raw_input().strip().split()]
row,col = [int(v) for v in raw_input().strip().split()]
obstacles = {}
for i in xrange(o):
	r,c = [int(v) for v in raw_input().strip().split()]
	obstacles[(r,c)] = True

straight_lines = [(row-1,col),(row,col+1),(row+1,col),(row,col-1)]
diagonal_lines = [(row-1,col+1),(row+1,col+1),(row+1,col-1),(row-1,col-1)]
counter = 0 
for item in straight_lines:
	r,c = item
	if r != row:
		if r < row:
			while r > 0:
				if (r,c) in obstacles:
					break
				else:
					counter += 1
					r -= 1
		else:
			while r < n+1:
				if (r,c) in obstacles:
					break
				else:
					r += 1
					counter += 1
	else:
		if c < col:
			while c > 0:
				if (r,c) in obstacles:
					break
				else:
					counter += 1
					c -= 1
		else:
			while c < n+1:
				if (r,c) in obstacles:
					break
				else:
					counter += 1
					c += 1

for item in diagonal_lines:
	r,c = item
	if r < row:
		if c < col:
			while c > 0 and r > 0:
				if (r,c) in obstacles:
					break
				else:
					counter += 1
					r -= 1
					c -= 1
		else:
			while c < n+1 and r > 0:
				if (r,c) in obstacles:
					break
				else:
					counter+=1
					r -= 1
					c += 1
	else:
		if c < col:
			while c > 0 and r < n+1:
				if (r,c) in obstacles:
					break
				else:
					counter += 1
					r += 1
					c -= 1
		else:
			while c < n+1 and r < n+1:
				if (r,c) in obstacles:
					break
				else:
					counter += 1
					r += 1
					c += 1

print counter