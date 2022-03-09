package java_ps.ds_challenge1.ps_array;

public class BestTimetoBuyandSellStock { //https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

  public static void main(String[] args) {
    
  }

  public int maxProfit(int[] prices) {

    int current = prices[0];
    int maxProfit = 0;

    for(int i = 1; i < prices.length; i++) {

      int temp = prices[i] - current;

      if(temp < 0) {
        current = prices[i];
      } else {
        maxProfit = Math.max(maxProfit, temp);
      }
    }

    return maxProfit;
  }
  
}
