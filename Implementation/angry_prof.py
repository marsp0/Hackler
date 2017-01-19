#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))

    results = [v for v in a if v<=0]
    if len(results) >= k:
        print 'NO'
    else:
        print 'YES'