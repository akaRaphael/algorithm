package java_ps.best75.ps_array;

public class LeetCode53 {

    public int maxSubArray(int[] nums) {
        int curn = nums[0];
        int result = nums[0];

        for(int i = 1; i < nums.length; i++) {
            int temp = curn + nums[i];
            curn = Math.max(temp, nums[i]);
            result = Math.max(result, curn);
        }
        return result;
    }
}
