#!/bin/python

import sys


a,b,c,d,e = raw_input().strip().split(' ')
lista = [int(a),int(b),int(c),int(d),int(e)]

aux_list = []
counter = 0
while counter != len(lista):
    temp = 0
    for i in xrange(len(lista)):
        if i != counter:
            temp += lista[i]
    aux_list.append(temp)
    counter += 1
print min(aux_list),  max(aux_list)