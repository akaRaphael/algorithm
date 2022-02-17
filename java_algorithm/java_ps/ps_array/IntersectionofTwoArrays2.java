package java_algorithm.java_ps.ps_array;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class IntersectionofTwoArrays2 { // https://leetcode.com/problems/intersection-of-two-arrays-ii/

  public static void main(String[] args) {

    IntersectionofTwoArrays2 foo = new IntersectionofTwoArrays2();

    int[] nums1 = {4,9,5};
    int[] nums2 = {4,4,9,9};
    System.out.println(foo.intersect(nums1, nums2));
  }
  
  public int[] intersect(int[] nums1, int[] nums2) {

    HashMap<Integer, Integer> map = new HashMap<>();
    List<Integer> list = new ArrayList<>();

    for (int i : nums1) {
      if(map.containsKey(i)){
        map.put(i, map.get(i) + 1);
      } else {
        map.put(i, 1);
      }
    }

    for (int i : nums2) {
      if(map.containsKey(i) && map.get(i) >= 1){
        list.add(i);
        map.put(i, map.get(i) - 1); // 중복을 제거하기 위해서 1 감소 시킴
      } 
    }
    
    return list.stream().mapToInt(e -> e).toArray();

  }
  
}


