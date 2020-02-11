# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:04:07 2020
Возвращает возможные корректные сочетания скобок
medium
https://leetcode.com/problems/generate-parentheses/
@author: Arh
"""
from itertools import permutations


class Solution:
    def generateParenthesis(self, n):
#        return list(permutations(nums))
        return helped(n, n)
        

def helped(opened, closed):
    ans = []
    if opened:
        ans.extend(['(' + s for s in helped(opened - 1, closed)])
    if opened < closed:
        ans.extend([')' + s for s in helped(opened, closed - 1)])
    if closed == 0:
        ans = [""]
    return ans


        
print(Solution().generateParenthesis(3))