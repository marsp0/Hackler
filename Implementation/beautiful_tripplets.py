
'''https://www.hackerrank.com/challenges/beautiful-triplets'''

n, d = [int(v) for v in raw_input().strip().split()]
#array = [int(v) for v in raw_input().strip().split()]
array = [int(v) for v in open('test.txt').read().strip().split()]
#print array
counter = 0
for index in xrange(len(array)):
	current = index
	try:
		end = index + 2*d+ 1
		array[end+1]
	except IndexError:
		end = len(array)
	for j in xrange(index+1, end):
		if array[j] == array[current] + d:
			for x in xrange(j+1,end):
				#print x, current
				if array[x] == array[current] + 2*d:
					counter += 1

print counter