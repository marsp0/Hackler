'''https://www.hackerrank.com/challenges/sam-and-substrings - medium'''

from collections import defaultdict

number = raw_input().strip()
prev_s_i = 0
prev_t_i = 0
mod = 10**9 + 7
for i in xrange(len(number)):
	s_i = (10*prev_s_i + (i+1)*int(number[i]) )%mod
	t_i = (prev_t_i + s_i) % mod
	#print s_i, t_i
	prev_t_i = t_i
	prev_s_i = s_i

print t_i % mod