# https://leetcode.com/study-plan/data-structure/?progress=nn1qgi2
# Leet Code - DS 익히기 14일 챌린지 

from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    
    idx = 0
    while idx < len(nums):
      curn = nums[idx]
      looking = target - curn
      if looking in nums:
        idx2 = nums.index(looking)
        if idx != idx2:
          return [idx, idx2]
        
      idx += 1
          
foo = Solution()
print(foo.twoSum(nums = [0,4,3,0], target = 0))