from math import ceil, floor
import sys

tests = int(raw_input().strip())
#fish = open('test.txt','r')
#tests = int(fish.readline())
temp = []
for i in xrange(tests):
	n,m = [float(v) for v in raw_input().strip().split()]
	#n,m = [float(int(v)) for v in fish.readline().split()]
	r = floor(n*float(n) / (n*n - 2*m))
	squared_n = n*n
	while True:
		result = (squared_n - (n%r)*int(ceil(n/float(r))**2) - (r - (n%r))*int(n/r)**2)/2
		r = r + 1
		if result >= m or r > n:
			break
		r = int(r)
		n = int(n)
	temp.append(r-1)

for item in temp:
	print int(item)


#m * 2/n^2 = (r-1)/r
#m * 2/n^2 = 1 - 1/r
#1 - 2m/ n^2= 1/r
#r = n^2/n^2 - 2m