# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:04:01 2020
Вовзращаем, сколько воды мы сможем задержать после дождая данной картой "высот"
hard?
https://leetcode.com/problems/trapping-rain-water/
@author: Arh
"""

class Solution:
    def trap(self, height):
        total_v = 0     # Общий объем
        mid_peak = height.index(max(height))
        
        # looking for left side mountains
        side_peak = 0   # Высота края чаши
        for h in height[:mid_peak + 1]:
            if h > side_peak:
                side_peak = h
            else:
                total_v += side_peak - h
        # looking for right side mountains
        side_peak = 0
        for h in height[:mid_peak-len(height)-1:-1]:
            if h > side_peak:
                side_peak = h
            else:
                total_v += side_peak - h
        
        return total_v
        
    
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))