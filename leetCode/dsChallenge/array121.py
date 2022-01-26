# Leet Code - DS 익히기 14일 챌린지 
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    min_num = prices[0]
    diff = 0
    for idx, num in enumerate(prices):
      if num < min_num:
        min_num = num
      elif num > min_num:
        if num - min_num > diff:
          diff = num - min_num
          
    return diff
  
foo = Solution()
print(foo.maxProfit(prices = [7,6,4,3,1]))       


class Solution2:
    def maxProfit2(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
            else:
                profit = max(profit, prices[i] - buy_price)
        return profit
      