#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

counter = 0
keep_track = []
for index in xrange(n):
    for x in xrange(n):
        if c[x] == c[index] and (index not in keep_track and x not in keep_track) and x != index:
            counter += 1
            keep_track.extend([x,index])
            break
            
print counter
            