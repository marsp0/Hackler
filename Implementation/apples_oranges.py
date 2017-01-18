#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

apples = 0
oranges = 0
for index in xrange(len(apple)):
    if apple[index] > 0 and (apple[index]+a <= t and apple[index]+a >= s):
        apples += 1
for index in xrange(len(orange)):
    if orange[index] < 0 and (orange[index]+b <= t and orange[index]+b >= s):
        oranges += 1

print apples
print oranges
