# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:17:43 2020

@author: Harsh Chaudhary
"""

'''
HackerLand National Bank has a simple policy for warning clients about possible fraudulent account 
activity. If the amount spent by a client on a particular day is greater than or equal to  2x
the client's median spending for a trailing number of days, they send the client a 
notification about potential fraud. The bank doesn't send the client any notifications until 
they have at least that trailing number of prior days' transaction data.

Given the number of trailing days d and a client's total daily expenditures for a period of n days, 
find and print the number of times the client will receive a notification over all n days.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def sortMe(start_index, last_index, k):
    dict = {}
    global d, expenditure
    output = [0]* ((d>>1)+2)
    temp = [0]* (k+1)
    last = False
    secondLast = False
    for i in range(start_index, last_index):
        dict[expenditure[i]] = dict.get(expenditure[i], 0) + 1

    temp[0] = dict.get(0, 0)
    for i in range(1, k+1):
        temp[i] = dict.get(i, 0) + temp[i-1]
        if 2*temp[i-1]>d: break
    print(temp)

    for i in range(start_index, last_index):
        if temp[expenditure[i]]<=len(output):
            output[temp[expenditure[i]]-1] = expenditure[i]
            if temp[expenditure[i]-1]==len(output)-1:
                last = True
            if temp[expenditure[i]-1]==len(output)-2:
                secondLast = True
            if last and secondLast:
                return output
        temp[expenditure[i]]-=1

    return output


def activityNotifications(expenditure, d):
    noti = 0
    k = max(expenditure)
    if d==len(expenditure):
        return 0
    for i in range(d, len(expenditure)):
        temp = sortMe(i-d, i, k)
        if d%2==0:
            median = temp[-2]+temp[-1]
        else:
            median = temp[-2]
            median = median << 1
        
        if (expenditure[i]>=median):
            noti+=1
    print (noti)
    return noti

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
################################################################################################
    ################################################################################################
def activityNotifications(expenditure, d):
    noti = 0
    k = max(expenditure)
    if d==len(expenditure):
        return 0
    for i in range(d, len(expenditure)):
        temp = sortMe(i-d, i, k)
        if d%2==0:
            median = temp[-2]+temp[-1]
        else:
            median = temp[-2]
            median = median << 1
        
        if (expenditure[i]>=median):
            noti+=1
    print (noti)
    return noti