'''https://www.hackerrank.com/challenges/ctci-coin-change - HARD'''

target,m = [int(v) for v in raw_input().strip().split()]
coins = [int(v) for v in raw_input().strip().split()]
coins = sorted(coins)

dp = [[0] * target for _ in xrange(len(coins))]
for i in xrange(len(coins)):
	for j in xrange(target):
		if i == 0:
			if (j+1) % coins[0] == 0:
				dp[i][j] = 1
			else:
				dp[i][j] = 0
		else:
			#print i,j+1
			if coins[i] == j+1:
				result = dp[i-1][j] + 1
			elif coins[i] > j+1:
				result = dp[i-1][j]
			else:
				result = dp[i-1][j] + dp[i][j-coins[i]]
			dp[i][j] = result
print dp[-1][-1]