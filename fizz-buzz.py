# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:04:01 2020
return range(n), but //3 = 'Fliz' //5 = 'Buzz'
easy
https://leetcode.com/problems/fizz-buzz/
@author: Arh
"""
import numpy as np
class Solution:
    def fizzBuzz(self, n):
        
        ans = list(map(str, range(1, n + 1)))
        ans[2:n + 1:3] = ["Fizz"] * (n // 3)
        ans[4:n + 1:5] = ["Buzz"] * (n // 5)
        ans[14:n+1:15] = ["FizzBuzz"] * (n // 15)
        
        f15 = ['1', '2', 'Fizz', '4', '5', 'Fizz', '7', '8',
               'Fizz', '10', '11', 'Fizz', '13', '14', 'Fizz'] 
        
        f = np.arange(1, 15, dtype=np.string_)
        
        
        return f
    
print(Solution().fizzBuzz(17))