# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:29:35 2020

@author: Harsh Chaudhary
"""


def vestigium(arr):
    n=len(arr)
    row=0
    col=0
    
    sum=0
    for i in range(n):
        sum += arr[i][i]
        if len(set(arr[i])) != len(arr[i]):
            row+=1
        map={}
        for j in range(n):
            if arr[j][i] not in map:
                map[arr[j][i]]=None
            else:
                col += 1
                break
    
    print("Case #"+str(t_itr+1)+": ", sum, row, col)


t = int(input())
for t_itr in range(t):
    n = int(input())
    temp=[]
    for i in range(n):
        temp.append(list(map(int, input().rstrip().split())))
    vestigium(temp)