package java_ps.crack_algo.recursion;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class LeetCode77 {

    public List<List<Integer>> combine(int n, int k) {

        List<List<Integer>> result = new LinkedList<>();
        if(k == 0) {
            result.add(new LinkedList<>());
            return result;
        }
        backtrack(1, new LinkedList<Integer>(), n, k, result);
        return result;
    }

    public void backtrack(int start, LinkedList<Integer> current, int n, int k, List<List<Integer>> result) {
        if(current.size() == k) {
            result.add(new LinkedList<>(current));
        }
        for(int i = start; i <= n && current.size() < k; i++) {
            current.add(i);
            backtrack(i + 1, current, n, k, result);
            current.removeLast();
        }
    }
}
