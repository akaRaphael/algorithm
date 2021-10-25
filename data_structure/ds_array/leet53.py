# 53. Maximum Subarray
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
print(foo.maxSubArray(nums = [-1,-2,-3,1]))