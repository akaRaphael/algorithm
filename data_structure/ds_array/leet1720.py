# 1720. Decode XORed Array
from typing import List

class Solution:
  def decode(self, encoded: List[int], first: int) -> List[int]:
    arr = [first]
    for i in range(len(encoded)):
      arr.append(arr[i] ^ encoded[i])
    return arr
        
foo = Solution()
foo.decode(encoded = [1,2,3], first = 1)