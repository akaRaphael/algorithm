# 1480. Running Sum of 1d Array
from typing import List

class Solution:
  def runningSum(self, nums: List[int]) -> List[int]:
    count = 0
    result = []
    for num in nums:
      count += num
      result.append(count)
    return result

foo = Solution()
print(foo.runningSum(nums = [1,2,3,4]))