package java_ps.ds_challenge1.ps_array;

import java.util.Arrays;

// 2022년 2월 9일 
public class MergeSortedArray { // https://leetcode.com/problems/merge-sorted-array/

  public static void main(String[] args) {


    int[] nums1 = {0};
    int[] nums2 = {1};
    int m = 0;
    int n = 1;

    MergeSortedArray foo = new MergeSortedArray();
    foo.merge(nums1, m, nums2, n);

    System.out.println(Arrays.toString(nums1));


  }

  public void merge(int[] nums1, int m, int[] nums2, int n) {
        
    if (m + n > m) {
      for (int i = m; i < m + n; i++) {
        nums1[i] = nums2[i - m];
      }
    }
    Arrays.sort(nums1);
  }
  

}