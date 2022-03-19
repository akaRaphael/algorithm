package java_ps.crack_algo.recursion;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class LeetCode46 {

    List<List<Integer>> result = new LinkedList<>();

    public List<List<Integer>> permute(int[] nums) {
        dfs(nums, new LinkedList<>());
        return result;
    }

    public void dfs(int[] nums, List<Integer> candidate) {
        if(candidate.size() == nums.length){
            result.add(new LinkedList<>(candidate));
            return;
        }

        for(int i = 0; i < nums.length; i++) {
            if(candidate.contains(nums[i]) == false) {
                candidate.add(nums[i]);
                dfs(nums, candidate);
                candidate.remove(candidate.size() - 1);
            }
        }
    }
}
