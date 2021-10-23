# 1672. Richest Customer Wealth
from typing import List

class Solution:
  def maximumWealth(self, accounts: List[List[int]]) -> int:
    result = 0
    for account in accounts:
      temp = sum(account)
      if result < temp:
        result = temp
    return result

foo = Solution()
print(foo.maximumWealth(accounts = [[1,2,3], [3,2,1]]))