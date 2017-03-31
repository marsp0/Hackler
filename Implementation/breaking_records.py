n = int(raw_input().strip())
games = [int(v) for v in raw_input().strip().split()]
lowest = 0
lowest_score = games[0]
highest = 0
highest_score = games[0]
for item in games:
	if item  < lowest_score:
		lowest += 1
		lowest_score = item
	if item > highest_score:
		highest_score = item
		highest += 1

print highest, lowest