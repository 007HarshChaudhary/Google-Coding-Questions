# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:19:53 2020

@author: Harsh Chaudhary
"""
'''
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced
back to him through his handwriting. He found a magazine and wants to know if 
he can cut out whole words from it and use them to create an untraceable replica of his ransom note.
The words in his note are case-sensitive and he must use only whole words available in the magazine.
He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate 
his ransom note exactly using whole words from the magazine; otherwise, print No.

For example, the note is "Attack at dawn". The magazine contains only "attack at dawn".
The magazine has all the right words, but there's a case mismatch. The answer is .
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    mag_dict = {}
    note_dict = {}

    for word in magazine:
        if word not in mag_dict:
            mag_dict[word] = 1
        else:
            mag_dict[word] += 1

    for word in note:
        if word not in note_dict:
            note_dict[word] = 1
        else:
            note_dict[word] += 1
    
    for key in note_dict:
        if key not in mag_dict or mag_dict[key]<note_dict[key]:
            print ('No')
            return
    
    print ('Yes')
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
