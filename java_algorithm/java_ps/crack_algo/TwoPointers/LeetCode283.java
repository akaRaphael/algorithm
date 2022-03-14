package java_ps.crack_algo.TwoPointers;

public class LeetCode283 {

    public void moveZeroes(int[] nums) {
        if(nums.length < 2) {
            return;
        }

        int left = 0;
        int right = 1;

        while(right < nums.length) {
            if(nums[left] == 0) {
                if(nums[right] != 0) {
                    nums[left] = nums[right];
                    nums[right] = 0;
                    left++;
                    right++;
                }
                else {
                    right++;
                }
            }
            else {
                left ++;
                if(left == right) {
                    right ++;
                }
            }
        }
    }
}
