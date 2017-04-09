n,m = [int(v) for v in raw_input().strip().split()]

string_a = [int(v) for v in raw_input().strip().split()]
string_b = [int(v) for v in raw_input().strip().split()]

def longest_common_sequence(string_a, string_b):
	memo = {}
	strings = {}
	for i in xrange(len(string_a)):
		memo[(i,-1)] = 0
		strings[(i,-1)] = ''
	for j in xrange(len(string_b)):
		strings[(-1,j)] = ''
		memo[(-1,j)] = 0
	memo[(-1,-1)] = 0
	strings[(-1,-1)] = ''
	for i in xrange(len(string_a)):
		for j in xrange(len(string_b)):
			if string_a[i] == string_b[j]:
				memo[(i,j)] = 1 + memo[(i-1,j-1)]
				strings[(i,j)] = strings[(i-1,j-1)] + str(string_a[i])
			else:
				memo[(i,j)] = max(memo[(i-1,j)], memo[(i,j-1)])
				if memo[(i-1,j)] > memo[(i,j-1)]:
					strings[(i,j)] = strings[(i-1,j)]
				else:
					strings[(i,j)] = strings[(i,j-1)]
	return memo,strings

memo,strings = longest_common_sequence(string_a, string_b)
print ' '.join(strings[(len(string_a)-1,len(string_b)-1)])