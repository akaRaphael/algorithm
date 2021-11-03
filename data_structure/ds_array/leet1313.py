# 1313. Decompress Run-Length Encoded List

from typing import List

class Solution:
  def decompressRLElist(self, nums: List[int]) -> List[int]:
    result = []
    nums.reverse()
    while len(nums) > 1:
      freq = nums.pop()
      val = nums.pop()
      result += ([val]*freq)

    return result

foo = Solution()
print(foo.decompressRLElist(nums = [1,2,3,4]))
        