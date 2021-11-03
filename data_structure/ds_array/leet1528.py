# 1528. Shuffle String
from typing import List

class Solution:
  def restoreString(self, s: str, indices: List[int]) -> str:
    temp = [0] * len(indices)
    for i in range(len(indices)):
      temp[indices[i]] = s[i]
    return "".join(temp)
    

foo = Solution()
print(foo.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
