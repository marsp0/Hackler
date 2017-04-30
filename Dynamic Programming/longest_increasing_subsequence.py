'''https://www.hackerrank.com/challenges/longest-increasing-subsequent - MEDIUM'''

n= int(raw_input().strip())
array = []
for i in xrange(n):
	array.append(int(raw_input().strip()))

def longest_increasing_subsequence(array):
    tails = [0] * len(array)
    size = 0
    for x in array:
    	print 'X is ',x
    	print 'tails is', tails
        i, j = 0, size
        print 'i,j is ',i,j
        while i != j:
            m = (i + j) / 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size

print longest_increasing_subsequence(array)