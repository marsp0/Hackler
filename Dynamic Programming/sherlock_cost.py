'''https://www.hackerrank.com/challenges/sherlock-and-cost'''

tests = int(raw_input().strip())

for test in xrange(tests):
	n = int(raw_input().strip())
	array = [int(v) for v in raw_input().strip().split()]
	s1 = {0:0}
	s2 = {0:0}
	for i in xrange(1,len(array)):
		s1[i] = max(s2[i-1]+abs(1-array[i-1]), s1[i-1])
		s2[i] = max(s1[i-1]+abs(array[i] - 1), s2[i-1]+abs(array[i] - array[i-1]))
	print max(s1[len(array)-1],s2[len(array)-1])