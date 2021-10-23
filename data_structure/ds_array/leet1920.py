# 1920. Build Array from Permutation
from typing import List

class Solution:
  def buildArray(self, nums: List[int]) -> List[int]:
    ans = [0] * len(nums)
    for i in range(len(nums)):
      ans[i] = nums[nums[i]]
    return ans

f = Solution()
print(f.buildArray(nums = [0,2,1,5,3,4]))