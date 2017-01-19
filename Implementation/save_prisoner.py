test_cases = int(raw_input())
save = []
for case in xrange(test_cases):
	prisoners, sweets, starting = [int(v) for v in raw_input().split()]
	if sweets+starting-1 <= prisoners:
		save.append(sweets+starting - 1)
	else:
		save.append((sweets+starting)%prisoners - 1)

for item in save:
	print item