import sys

'''https://www.hackerrank.com/challenges/unbounded-knapsack - medium'''

tests = int(raw_input().strip())
#fish = open('test.txt','r')
#tests = int(fish.readline().strip())
sys.setrecursionlimit(100000)

def recursive(array,index,S):
	if S <= 0:
		return 0
	elif index == 0:
		temp = 0
		while S - array[0] >= 0:
			S -= array[0]
			temp += array[0]
		return temp
	else:
		if S - array[index] >= 0:
			return max(array[index]+recursive(array,index-1,S - array[index]),
					recursive(array,index-1,S),
					recursive(array,index,S-array[index])+array[index])
		else:
			return recursive(array,index-1,S)

for i in xrange(tests):
	n,k = [int(v) for v in raw_input().strip().split()]
	array = [int(v) for v in raw_input().strip().split()]
	#n,k = [int(v) for v in fish.readline().strip().split()]
	#array = [int(v) for v in fish.readline().strip().split()]
	print recursive(array,len(array)-1,k)