package java_ps.ds_challenge1.ps_array;

import java.util.HashSet;

// 2022년 2월 2일
public class ContainsDuplicate { // https://leetcode.com/problems/contains-duplicate/

  public static void main(String[] args) {
    
  }

  public boolean containsDuplicate(int[] nums) {

    HashSet<Integer> foo = new HashSet<>();

    for (int i : nums) {
      if (!foo.add(i)) {
        return true;
      }
    }
    return false;
  }

  
}
