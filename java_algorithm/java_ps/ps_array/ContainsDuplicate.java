package java_algorithm.java_ps.ps_array;

import java.util.HashSet;

// 2022년 2월 2일
public class ContainsDuplicate { // https://leetcode.com/problems/contains-duplicate/

  public static void main(String[] args) {
    
  }

  public boolean containsDuplicate(int[] nums) {

    HashSet<Integer> foo = new HashSet<>();

    for (int i : nums) {
      if (!foo.add(i)) {
        return false;
      }
    }
    return true;
  }

  
}
