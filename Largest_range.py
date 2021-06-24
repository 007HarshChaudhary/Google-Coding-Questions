# -*- coding: utf-8 -*-
"""
Created on Fri May 22 21:33:21 2020

@author: Harsh Chaudhary
"""
array = [
    19,
    -1,
    18,
    17,
    2,
    10,
    3,
    12,
    5,
    16,
    4,
    11,
    8,
    7,
    6,
    15,
    12,
    12,
    2,
    1,
    6,
    13,
    14
  ]
array.sort()
i_anchor = 0
res = [array[0], array[0]]

for i in range(1, len(array)):
	if array[i]!=array[i-1]+1 and array[i]!=array[i-1] and array[i-1]-array[i_anchor]>=res[1]-res[0]:
		res[0] = array[i_anchor]
		res[1] = array[i-1]
		i_anchor = i
if i_anchor==len(array)-1:
	print (res)
elif array[-1] == array[-2]+1 and array[-1]-array[i_anchor]>res[1]-res[0]:
	res[1] = array[-1]
	res[0] = array[i_anchor]
print (res)