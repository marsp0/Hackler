from math import ceil, floor
import sys

tests = int(raw_input().strip())
#fish = open('test.txt','r')
#tests = int(fish.readline())
for i in xrange(tests):
	n,m = [float(v) for v in raw_input().strip().split()]
	#n,m = [float(int(v)) for v in fish.readline().split()]
	result = sys.maxsize
	r = n - 1
	while result > m:
		result = (n*n - (n%r)*int(ceil(n/r)**2) - (r - (n%r))*int(n/r)**2)/2
		r -= 1
		r = int(r)
		n = int(n)
		print result, 'result'
	print r + 1