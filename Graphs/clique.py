from math import ceil, floor
import sys

tests = int(raw_input().strip())
#fish = open('test.txt','r')
#tests = int(fish.readline())
temp = []
for i in xrange(tests):
	n,m = [float(v) for v in raw_input().strip().split()]
	#n,m = [float(int(v)) for v in fish.readline().split()]
	result = sys.maxsize
	r = n - 1
	squared_n = n*n
	while result > m:
		result = (squared_n - (n%r)*int(ceil(n/float(r))**2) - (r - (n%r))*int(n/r)**2)/2					
		if result >= m:
			r = r - 1
		r = int(r)
		n = int(n)
	temp.append(r+1)

for item in temp:
	print item