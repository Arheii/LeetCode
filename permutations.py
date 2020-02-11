# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:04:07 2020
Возвращрает все возможные перестановки. что-то какая то легкая херня в медиум
medium
https://leetcode.com/problems/permutations/
@author: Arh
"""
from itertools import product

from collections import Counter
class Solution:
    def permute(self, nums):
        return list(product(nums))
        


        
print(Solution().permute([1,2,3]))