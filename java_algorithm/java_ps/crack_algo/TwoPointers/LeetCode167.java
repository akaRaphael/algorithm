package java_ps.crack_algo.TwoPointers;

public class LeetCode167 {

    public int[] twoSum(int[] numbers, int target) {
        int start = 0;
        int end = numbers.length - 1;

        while(start < numbers.length) {
            int left = target - numbers[start];

            if(numbers[end] == left) break;
            else if(numbers[end] > left) end--;
            else if(numbers[end] < left) start++;
        }
        return new int[] {start + 1, end + 1};
    }
}
