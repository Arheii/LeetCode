# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 20:53:14 2020

@author: Arh
"""

def twoSum(nums, target):
    set_nums = set(nums)
    for x in set_nums:
        if (target - x) in set_nums:
            ind_1 = nums.index(x)
            try:
                ind_2 = 1 + ind_1 + nums[ind_1 + 1:].index(target - x)
                break
            except ValueError:
                ind_2 = False
    else:
        ind_2 = False

    if ind_2:
        return [ind_1, ind_2]