# https://leetcode.com/problems/maximum-subarray/
# Leet Code - DS 익히기 14일 챌린지 

from typing import List

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    current = nums[0]
    result = nums[0]
    for i in range(1, len(nums)):
      current = max(current + nums[i], nums[i])
      result = max(current, result)
    return result
  
foo = Solution()
print(foo.maxSubArray(nums = [5,4,-1,7,8]))
print(foo.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))