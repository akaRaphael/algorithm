package java_algorithm.java_ps.ps_array;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class ArrayApp {
  public static void main(String[] args) {

    TwoSum foo = new TwoSum();

    int[] nums = {2, 7, 11, 15};
    int target = 9;

    foo.twoSum2(nums, target);

    
  }
}

class TwoSum { //https://leetcode.com/problems/two-sum/

  public int[] twoSum2(int[] nums, int target) {
    Map<Integer, Integer> indexMap = new HashMap<>();

    int[] result = new int[2];

    for(int i = 0; i < nums.length; i++) {
      if(indexMap.containsKey(target - nums[i])) {
        result[0] = i;
        result[1] = indexMap.get(target-nums[i]);
        break;
      }
      indexMap.put(nums[i], i);
    }
    return result;
  }

  public int[] twoSum(int[] nums, int target) {
    int idx = 0;
    int length = nums.length;

    for(int i = 0; i < length - 1; i++) {
      int firstNum = nums[i];

      for(int j = i + 1; j < length; j++) {
        int secondNum = nums[j];

        if(firstNum + secondNum == target) {
          int[] result = new int[]{i, j};
          return result;
        }
      }
    }
    return null;
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