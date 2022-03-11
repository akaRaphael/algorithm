package java_ps.crack_algo.BST;

public class LeetCode35 {
    public int searchInsert(int[] nums, int target) {

        int mid = nums.length / 2;

        if(target == nums[mid]) return mid;

        if(target > nums[mid]) {
            for(int i = mid; i < nums.length; i ++) {
                if(nums[i] == target) return i;
                else if(target < nums[i]) return i;
            }
            return nums.length;
        }

        if(target < nums[mid]) {
            for(int i = mid; i >= 0; i--) {
                if(target == nums[i]) return i;
                else if(target > nums[i]) return i + 1;
            }

            return 0;
        }
        return 100;
    }
}
