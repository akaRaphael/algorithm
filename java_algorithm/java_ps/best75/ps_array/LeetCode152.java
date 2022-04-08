package java_ps.best75.ps_array;

public class LeetCode152 {

    public int maxProduct(int[] nums) {

        int curn = 1;
        int maxNum = Integer.MIN_VALUE;
        int result = Integer.MIN_VALUE;

        for(int i = 0; i < nums.length; i++) {
            curn = 1;
            maxNum = Integer.MIN_VALUE;
            for(int j = i; j < nums.length; j++) {
                curn *= nums[j];
                maxNum = Math.max(curn, maxNum);
                if(curn == 0) {
                    curn = 1;
                }
            }
            result = Math.max(result, maxNum);
        }
        return result;
    }
}
