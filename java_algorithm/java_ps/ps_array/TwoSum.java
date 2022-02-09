package java_algorithm.java_ps.ps_array;

import java.util.HashMap;
import java.util.Map;

// 2022년 2월 8일 
public class TwoSum { //https://leetcode.com/problems/two-sum/
  public static void main(String[] args) {
    
  }

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
