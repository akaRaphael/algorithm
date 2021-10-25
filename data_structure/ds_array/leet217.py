# 217. Contains Duplicate
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      return len(nums) != len(set(nums))

foo = Solution()
print(foo.containsDuplicate(nums = [2,14,18,22,22]))