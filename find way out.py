# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:06:49 2020

@author: Harsh Chaudhary
"""

def way(string):
    op = ''
    for i in string:
        if i is 'S':
            op += 'E'
        else:
            op += 'S'
    print('Case #{}: {}'.format(t_itr, op))


t = int(input())
t_itr = 1
while t>=t_itr:
    n = int(input())
    n = input()
    way(n)
    t_itr += 1