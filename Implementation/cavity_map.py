#!/bin/python

import sys


n = int(raw_input().strip())
grid = []
grid_i = 0
row_results = {}
for grid_i in xrange(n):
   grid_t = str(raw_input().strip())
   grid.append(grid_t)

for row in xrange(1,len(grid)-1):
	for column in xrange(1,len(grid[row])-1):
		current_min = int(grid[row][column])
		if int(grid[row][column-1]) >= current_min or  int(grid[row][column+1]) >= current_min or int(grid[row-1][column]) >= current_min or int(grid[row+1][column]) >= current_min:
			continue
		else:
			try:
				row_results[row].append(column)
			except KeyError:
				row_results[row] = [column]
			
for row in row_results:
	temp = ''
	while row_results[row]:
		popped = row_results[row].pop(0)
		print popped
		temp += grid[row][len(temp)-1 : popped] + 'X'
	temp += grid[row][len(temp):]
	grid[row] = ''.join(temp)
print
for item in grid:
	print item