# -*- coding: utf-8 -*-
"""
Created on Sat May  2 09:48:37 2020

@author: Harsh Chaudhary
"""
a = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
res=""
for char in a:
    if char.isalpha() and char.islower():
        res += chr(abs(ord(char)-219))
    else:
        res += char