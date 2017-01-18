#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))
aux_list = 0
for j in xrange(1, len(a)):
    for i in xrange(j):
        if (a[j]+a[i]) % k == 0:
            aux_list += 1
            
print aux_list
        