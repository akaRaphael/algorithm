package java_ps.ps_array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PascalsTriangle { //https://leetcode.com/problems/pascals-triangle/

  public static void main(String[] args) {
    
  }

  public List<List<Integer>> generate(int numRows) {

    List<List<Integer>> result = new ArrayList<>();
    List<Integer> array = new ArrayList<>();

    array.add(1);
    result.add(array);
    
    for (int i = 1; i < numRows; i++) {
      array = new ArrayList<>();
      array.add(1);

      for(int j = 1; j < i; j++) {
        int el = result.get(i - 1).get(j - 1) + result.get(i - 1).get(j);
        array.add(el);
      }

      array.add(1);
      result.add(array);
    }

    return result;

  }
  
}
