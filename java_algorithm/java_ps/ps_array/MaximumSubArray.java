package java_ps.ps_array;

// 2022년 2월 7일 
public class MaximumSubArray { //https://leetcode.com/problems/maximum-subarray/
  public static void main(String[] args) {
    
  }

  public int maximumSubArray(int[] nums) {

    int current = nums[0];
    int result = nums[0];

    for ( int i = 1; i < nums.length; i++ ) {
      int temp = current + nums[i];
      current = (temp > nums[i]) ? temp : nums[i];
      result = (result > current) ? result : current;
    }
    return result;
  }

}
