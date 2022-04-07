package java_ps.best75.ps_array;

public class LeetCode121 {

    public int maxProfit(int[] prices) {

        int result = 0;
        int current = prices[0];

        for(int i = 1; i < prices.length; i++) {
            if(prices[i] - current < 0) {
                current = prices[i];
            }

            result = Math.max(result, prices[i] - current);
        }
        return result;
    }
}
