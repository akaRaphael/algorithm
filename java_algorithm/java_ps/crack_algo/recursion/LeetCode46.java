package java_ps.crack_algo.recursion;

import java.util.LinkedList;
import java.util.List;

public class LeetCode46 {

    List<List<Integer>> result = new LinkedList<>();

    public List<List<Integer>> permute(int[] nums) {
        List<Integer> candidate = new LinkedList<>();
        for(int num : nums) {
            candidate.add(num);
        }

        dfs(new LinkedList<Integer>(), candidate);

        return result;
    }

    private void dfs(List<Integer> permutation, List<Integer> candidate) {
        if(candidate.size() == 0) {
            result.add(permutation);
            return;
        }
        for(Integer num : candidate) {
            List<Integer> tempPermutation  = new LinkedList<>(permutation);
            List<Integer> tempCandidate = new LinkedList<>(candidate);

            tempPermutation.add(num);
            tempCandidate.remove(num);

            dfs(tempPermutation, tempCandidate);
        }
    }
}
