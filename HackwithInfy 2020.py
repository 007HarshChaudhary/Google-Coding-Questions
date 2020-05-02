# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 09:58:30 2020

@author: Harsh Chaudhary
"""
def solve(main_string, q, query):
    output = []
    for k in query:
        string = main_string.lower()[k[0]-1: k[1]]
        count = 0
        s = 0
        l = s+10
        while l<len(string):
            if sorted(string[s: l+1]) == ['a', 'a', 'c', 'e', 'e', 'h', 'h', 'k', 'r', 'r', 't']:
                count+=1
                break
            s+=1
            l+=1
        while l<len(string)-1:
            l += 1
            s += 1
            if string[l]==string[s-1]:
                count+=1
        output.append(count)
    return output
    
s = input()
q = int(input())
query = [list(map(int, input().split())) for i in range(q)]
out_ = solve(s, q, query)
for v in out_:
    print(v)