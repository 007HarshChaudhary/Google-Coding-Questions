# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:16:00 2020

@author: Harsh Chaudhary
"""


words = ['majedoc', 'maj', 'mah', 'malan', 'muh', 'molon']


trie = dict()
for word in words:
    temp_dict = trie
    for letter in word:
        temp_dict = temp_dict.setdefault(letter, {})
    temp_dict['*'] = "*"

