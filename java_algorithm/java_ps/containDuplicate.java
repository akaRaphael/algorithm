package java_algorithm.java_ps;

import java.util.HashSet;

public class containDuplicate { // https://leetcode.com/problems/contains-duplicate/

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