package java_ps.best75.ps_array;

import java.util.HashSet;

public class LeetCode217 {
    public boolean containsDuplicate(int[] nums) {

        HashSet<Integer> set = new HashSet<>();

        for(int num : nums) {
            if(!set.add(num)) {
                return true;
            }
            set.add(num);
        }
        return false;
    }
}
