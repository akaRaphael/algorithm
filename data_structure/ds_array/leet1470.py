# 1470. Shuffle the Array
from typing import List

class Solution:
  def shuffle(self, nums:List[int], n: int) -> List[int]:
    mid = n
    left = nums[:mid]
    right = nums[mid:]  
    result = []

    for i in range(len(left)):
      result.append(left[i])
      result.append(right[i])
    
    return result

foo = Solution()
print(foo.shuffle(nums = [1,2,3,4,4,3,2,1], n = 4))