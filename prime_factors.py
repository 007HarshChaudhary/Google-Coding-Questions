# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 20:57:11 2020

@author: Harsh Chaudhary
"""
def gcd(larger, smaller):
    rem = larger%smaller
    larger = smaller
    smaller = rem
    while rem!=0:
        rem = larger%smaller
        larger = smaller
        smaller = rem
    print(larger)



a = int(input())
b = int(input())
larger = max(a, b)
smaller = min(a, b)
gcd(larger, smaller)