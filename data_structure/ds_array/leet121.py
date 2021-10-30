# 121. Best Time to Buy and Sell Stock

from typing import List

def maxProfit(prices: List[int]) -> int:
  buy_price = prices[0]
  profit = 0
  for i in range(1, len(prices)):
    if prices[i] < buy_price:
      buy_price = prices[i]
    else:
      profit = max(profit, prices[i] - buy_price)
  return profit
  
print(maxProfit(prices = [3,2,6,5,0,3]))  