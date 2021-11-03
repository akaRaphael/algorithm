
# 118. Pascal's Triangle
from typing import List

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    result = []
    for i in range(numRows):
      if i < 2:
        result.append([1] * (i + 1))
      else:
        result.append([1] + [result[i - 1][j] + result[i - 1][j + 1] for j in range(i - 1)] + [1])
    return result

foo = Solution()
print(foo.generate(numRows = 5))