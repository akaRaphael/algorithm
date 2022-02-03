package java_algorithm.java_ps;

public class maximumSubarray { //https://leetcode.com/problems/maximum-subarray/

  public int maxSubArray(int[] nums) {

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