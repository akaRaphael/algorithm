package java_ps.crack_algo.bst;

public class LeetCode704 {

    public int search(int[] nums, int target) {
       int endIndex = nums.length - 1;
       int mid = 0;
       int start = 0;

       while(start <= endIndex) {
           mid = (start + endIndex) / 2;

           if(target == nums[mid]) {
               return mid;
           }

           if(target > nums[mid]) {
               start = mid + 1;
           }
           else {
               endIndex = mid - 1;
           }
       }
       return -1;
    }
}
