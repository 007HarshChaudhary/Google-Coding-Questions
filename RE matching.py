# -*- coding: utf-8 -*-
"""
Created on Tue May 19 18:22:35 2020

@author: Harsh Chaudhary
"""

import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return isMatch(s, p)
def isMatch(text, pattern):
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (isMatch(text, pattern[2:]) or
                    first_match and isMatch(text[1:], pattern))
    else:
        return first_match and isMatch(text[1:], pattern[1:])

    

