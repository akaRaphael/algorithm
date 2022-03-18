package java_ps.crack_algo.twoPointers;

public class LeetCode189 {

    public void rotate(int[] nums, int k) {
        k = k % nums.length; // 7 나누기 3의 나머지
        reverse(nums, 0, nums.length - 1); // 전체 배열을 reverse
        reverse(nums, 0, k - 1); // k-1 까지의 요소를 reverse
        reverse(nums, k, nums.length - 1); // k부터 마지막 요소까지 reverse
    }

    public void reverse(int[] nums, int start, int end) {
        while(start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}
