n = int(raw_input().strip())
andrea = []
maria = []
for i in xrange(n):
	andrea.append(int(raw_input().strip()))
m = int(raw_input().strip())
for j in xrange(m):
	maria.append(int(raw_input().strip()))
game_type = raw_input().strip()
result_maria = 0
result_andrea = 0
if game_type == 'Even':
	start = 0
else:
	start = 1
for i in xrange(start,n,2):
	result_andrea += (andrea[i] - maria[i])
	result_maria += (maria[i] - andrea[i])

if result_maria > result_andrea:
	print 'Maria'
else:
	print 'Andrea'