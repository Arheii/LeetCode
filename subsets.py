# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:04:07 2020
Возвращает все возможные перестановки любой длинный
medium
https://leetcode.com/problems/subsets/
@author: Arh
"""

from itertools import permutations, product


class Solution:
    def subsets(self, nums):
        if len(nums) > 1:
            perm = self.subsets(nums[1:])
        else:
            return [[nums[0]], []]
        print(perm)
#        ans = [nums[0]].extend([[nums[0]] + x for x in perm])
        return [[nums[0]] + x for x in perm] + perm
            


print(Solution().subsets([1,2,3]))
