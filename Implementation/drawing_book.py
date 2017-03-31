n = int(raw_input().strip())
p = int(raw_input().strip())
if n - 1 == p and n % 2 == 1:
	print 0
elif n-1 == p and n % 2 == 0:
	if p != 1:
		print 1
	else:
		print 0
elif p == n :
	print 0
else:
	if p <= n/2:
		print p/2
	else:
		print (n-p)/2