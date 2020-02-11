# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:04:07 2020
возвращает список произведения всех чисел, кроме i
medium
https://leetcode.com/problems/product-of-array-except-self/
@author: Arh
"""



class Solution:
    def productExceptSelf(self, nums):
        ans = []
        p = 1
        for x in nums:
            ans.append(p)
            p = p * x
        p = 1
        for i in range(1, len(nums) + 1):
            ans[-i] *= p
            p *= nums[-i]
        return ans
            

print(Solution().productExceptSelf([1,2,3,4]))