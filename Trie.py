# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 09:21:34 2021

@author: Harsh Chaudhary
"""

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def charToIndex(self, char):
        return ord(char)-ord('a')
    
    def insert(self, word):
        ptr = self.root
        
        for letter in word:
            if ptr.children[self.charToIndex(letter)] is None:
                ptr.children[self.charToIndex(letter)] = TrieNode()
            ptr = ptr.children[self.charToIndex(letter)]
        
        ptr.isEnd = True
    
    def searchPrefix(self, word):
        ptr = self.root
        
        for letter in word:
            if ptr.children[self.charToIndex(letter)] is None:
                return False
            ptr = ptr.children[self.charToIndex(letter)]
        
        return True
    
    def getPrefixNode(self, word):
        ptr = self.root
        
        for letter in word:
            if ptr.children[self.charToIndex(letter)] is None:
                return None
            ptr = ptr.children[self.charToIndex(letter)]
        
        return ptr
        
    
    def getStrings(self, node, res="", final=[]):
        if node.isEnd == True:
            final.append(res)
        
        for i in range(26):
            if node.children[i] is not None:
                res += chr(i+ord('a'))
                self.getStrings(node.children[i], res, final)
                res = res[:-1]
        
        return final
        
        
def process(key, trie):
    node = trie.getPrefixNode(key)
    if node is None:
        return
    
    data = trie.getStrings(node, final=[])
    for i in range(len(data)):
        data[i] = key + data[i]
    
    return data

trie = Trie()
s = "geeips"
contact = ["geeikistest", "geeksforgeeks", "geeksfortest"]
for c in contact:
    trie.insert(c)
    
res = [None]*len(s)

for i in range(len(s)):
    key = s[:i+1]
    res[i] = process(key, trie)
    if res[i] is None:
        res[i] = 0

print(res)