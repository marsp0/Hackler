from collections import defaultdict

'''https://www.hackerrank.com/challenges/manasa-and-stones
	thanks to one of the comments i got the linear solution. Otherwise it would have been exponential lel
'''

test_cases = int(raw_input().strip())
results = defaultdict(set)
for test in xrange(test_cases):
	n = int(raw_input().strip())
	a = int(raw_input().strip())
	b = int(raw_input().strip())
	if a>b:
		a,b = b,a
	for i in xrange(n):
		results[test].add(a*(n-i-1) + b*i)

sorted_keys = sorted(results.keys())
for item in sorted_keys:
	sorted_results = sorted(results[item])
	for i in sorted_results:
		print i,
	print