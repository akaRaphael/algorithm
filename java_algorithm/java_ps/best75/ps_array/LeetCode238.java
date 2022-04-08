package java_ps.best75.ps_array;

public class LeetCode238 {

    public int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];
        int initial = 1;

        for(int i = 0; i < nums.length; i ++) {
            ans[i] = initial;
            initial *= nums[i];
        }

        initial = 1;
        for(int i = nums.length - 1; i >= 0; i--) {
            ans[i] *= initial;
            initial *= nums[i];
        }
        return ans;
    }
}
