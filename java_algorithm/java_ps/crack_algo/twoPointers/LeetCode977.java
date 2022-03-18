package java_ps.crack_algo.twoPointers;

public class LeetCode977 {
    
    public int[] sortedSquares(int[] nums) {
        int len = nums.length;
        int[] result = new int[len];
        int start = 0;
        int end = len - 1;
        int idx = len - 1;

        while(start <= end) {
            int a = nums[start] * nums[start];
            int b = nums[end] * nums[end];

            if(a > b) {
                result[idx] = a;
                idx--;
                start++;
            }
            else {
                result[idx] = b;
                idx--;
                end--;
            }
        }
        return result;
    }
}
