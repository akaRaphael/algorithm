package java_ps.neetcode;

public class LeetCode238 {
    public int[] productExceptSelf(int[] nums) {

        int[] answer = new int[nums.length];
        int temp = 1;

        for(int i = 0; i < nums.length; i++) {
            answer[i] = temp;
            temp *= nums[i];
        }

        temp = 1;
        for(int j = nums.length - 1; j >= 0; j--) {
            answer[j] *= temp;
            temp *= nums[j];
        }

        return answer;
    }
}
