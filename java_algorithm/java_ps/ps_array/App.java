package java_algorithm.java_ps.ps_array;

import java.util.HashSet;

public class App {
  public static void main(String[] args) {
    
  }
}

class MaximumSubarray { //https://leetcode.com/problems/maximum-subarray/

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

class ContainsDuplicate { // https://leetcode.com/problems/contains-duplicate/

  public boolean containsDuplicate(int[] nums) {

    HashSet<Integer> flag = new HashSet<>();

    for (int i : nums) {
      if (!flag.add(i)) {
        return true;
      }
    }
    return false;
  }

}
