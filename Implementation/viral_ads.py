days = int(raw_input().strip())
start = 5
counter = 0
for ind in xrange(days):

	liked = start//2
	start = liked*3
	counter += liked

print counter