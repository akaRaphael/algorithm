# 1929. Concatenation of Array
from typing import List

class Solution:
  def getConcatenation(self, nums: List[int]) -> List[int]:
    return nums * 2


f = Solution()
print(f.getConcatenation(nums = [1,2,3]))