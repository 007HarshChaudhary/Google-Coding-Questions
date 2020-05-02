# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:28:35 2020

@author: Harsh Chaudhary
"""
def parenting(arr):
    dict = {}
    for i in range(len(arr)):
        dict[i+1] = arr[i]
    activity_list = sorted(dict.items(), key=lambda k: k[1][0])

    
    map = {'J': [activity_list[0][0]],
           'C': [activity_list[1][0]]}

    str1 = [None for i in range(len(arr))]

    for t in activity_list[2:]:

        j_current = map['J'][-1]
        c_current = map['C'][-1]
        
        if t[-1][0]>=dict[j_current][-1]:
            map['J'].append(t[0])
        elif t[-1][0]>=dict[c_current][-1]:
            map['C'].append(t[0])
        else:  
            print("Case #"+str(t_itr)+": "+ "IMPOSSIBLE")
            return
    

    for i in map['J']:
        str1[i-1] = 'J'
    for i in map['C']:
        str1[i-1] = 'C'
    op = ''
    for i in str1:
        if i is not None:
            op += str(i)
            
    print("Case #"+str(t_itr)+": "+ op)
    
                 
t = int(input())
t_itr = 1
while t_itr<=t:
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    parenting(arr)
    t_itr+=1
