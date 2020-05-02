# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:57:15 2020

@author: Harsh Chaudhary

"""

# =============================================================================
# def depth():
#     s = input()
#     res = list(s)
#     n = 2*int(max(res)) + len(s)
#     ans = [None for i in range(n)]
#     largest = int(s[0])
#     
#     for i in range(largest):
#         ans[i] = '('
#     ans[largest] = largest
#     for i in range(largest+1, 2*largest+1):
#         ans[i] = ')'
#         
#     for i in range(1, len(res)):
#         if int(res[i])<int(res[i-1]):
#             no = int(res[i-1])-int(res[i])
#             index=None
#             index2=None
#             for j in range(n-1, -1, -1):
#                 if ans[j]==int(res[i-1]):
#                     index=j
#                     break
#             
#             for j in range(index, n):
#                 if no==0:
#                     index2=j
#                     break
#                 if ans[j]==')':
#                     no -= 1
#             ans.insert(index2, int(res[i]))
#         else:
#             no = int(res[i])-int(res[i-1])
#             index=None
#             for j in range(n-1, -1, -1):
#                 if ans[j]==int(res[i-1]):
#                     index=j+1
#                     break
#             count = no
#             while no>0:
#                 ans.insert(index, '(')
#                 no-=1
#                 index+=1
#             
#             ans.insert(index, int(res[i]))
#             index+=1
#             while count>0:
#                 ans.insert(index, ')')
#                 count-=1
#                 index+=1
#             
#     
#     
#     op = ''
#     for i in ans:
#         if i is not None:
#             op += str(i)
#     
#     print("Case #"+str(t_itr)+": "+ op)
# 
# t = int(input())
# t_itr = 1
# while t_itr<=t:
#     depth()
#     t_itr+=1
#     
# 
# =============================================================================
def depth():
    
    s = input()
    op = ''
    op += '('*int(s[0])
    op += s[0]
    
    for i in range(1, len(s)):
        diff = abs(int(s[i-1]) - int(s[i]))
        if int(s[i])<int(s[i-1]):
            op += ')'*diff
        else:
            op += '('*diff
        op += s[i]
            
    op += ')'* (op.count('(') - op.count(')'))
    print("Case #"+str(t_itr)+": "+ op)

t = int(input())
t_itr = 1
while t_itr<=t:
    depth()
    t_itr+=1