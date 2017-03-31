t1, t2, n = [int(v) for v in raw_input().strip().split()]
memo = {}
memo[1] = t1
memo[2] = t2

def fibonacci(memo,n):
	for i in xrange(1,n+1):
		if i in memo:
			continue
		else:
			memo[i] = memo[i-2] + memo[i-1]**2
fibonacci(memo,n)
print memo[n]