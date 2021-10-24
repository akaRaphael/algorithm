# 1365. How Many Numbers Are Smaller Than the Current Number
from typing import Counter, List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
      freq = Counter(nums)
      return freq

foo = Solution()
print(foo.smallerNumbersThanCurrent(nums = [8,1,2,2,3]))