# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:47:19 2020
return single one element from list
easy
https://leetcode.com/problems/single-number/
@author: Arh
"""

from collections import Counter
class Solution:
    def singleNumber(self, nums) -> int:
        for i in range(len(nums)):
            x = nums.pop()
            try:
                nums.remove(x)
            except ValueError:
                return x

        
        
    
        
sol = Solution().singleNumber([4,1,2,1,2])
print(sol)