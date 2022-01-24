# Leet Code - DS 익히기 14일 챌린지 
# https://leetcode.com/problems/contains-duplicate/

from typing import List

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
  
  
foo = Solution()
print(foo.containsDuplicate(nums = [1,1,2,3,4,5]))