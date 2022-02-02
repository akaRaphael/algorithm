package java_algorithm.java_ps;

import java.util.HashSet;

public class containDuplicate {

  // https://leetcode.com/problems/contains-duplicate/
  public static void main(String[] args) {
    
    int [] nums = {1,1,1,3,3,4,3,2,4,2};

    Solution foo = new Solution();
    System.out.println(foo.containsDuplicate(nums));
  }
}

class Solution {
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
