# 2011. Final Value of Variable After Performing Operations
from typing import List

class Solution:
  def finalValueAfterOperations(self, operations: List[str]) -> int:
    x = 0
    for operation in operations:
      if "-" in operation:
        x -= 1
      
      if "+" in operation:
        x += 1
    return x

foo = Solution()
print(foo.finalValueAfterOperations(operations = ["++X","++X","X++"]))
