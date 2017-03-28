#fish = open('test.txt','r')
#s,n,m = [int(v) for v in fish.readline().strip().split()]
#keyboards = [int(v) for v in fish.readline().strip().split()]
#usbs  = [int(v) for v in fish.readline().strip().split()]

s,n,m = [int(v) for v in raw_input().strip().split()]
keyboards = [int(v) for v in raw_input().strip().split()]
usbs = [int(v) for v in raw_input().strip().split()]

keyboards = sorted(keyboards)
usbs = sorted(usbs)
#print keyboards
#print
#print usbs
if usbs[0] + keyboards[0] > s:
	print -1
else:
	found = False
	max_size = 0
	for j in xrange(len(keyboards)-1,-1,-1):
		for i in xrange(len(usbs)-1,-1,-1):
			#print 'Trying {} and {}'.format(keyboards[j] + usbs[i], s)
			if keyboards[j] + usbs[i] <= s:
				if keyboards[j] + usbs[i] > max_size:
					max_size = keyboards[j] + usbs[i]

print max_size