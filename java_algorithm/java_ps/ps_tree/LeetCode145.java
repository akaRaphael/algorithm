package java_ps.ps_tree;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class LeetCode145 {
    // Post Traverse(후위순회) = 왼쪽 자식 -> 오른쪽 자식 -> 부모
    // 재귀를 사용하면 이대로 코딩하면 된다.

    // Definition for a binary tree node.
    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public List<Integer> postorderTraversal(TreeNode root) {
        // 재귀를 이용한 풀이

        List<Integer> result = new ArrayList<>();
        dfs(root, result);

        return result;
    }

    public void dfs(TreeNode root, List<Integer> result) {
        if(root == null) {
            return;
        }
        dfs(root.left, result);
        dfs(root.right, result);
        result.add(root.val);
    }

    public List<Integer> postorderTraversal2(TreeNode root) {
        // 반복문을 이용한 풀이

        Stack<TreeNode> visited = new Stack<>();
        List<Integer> result = new ArrayList<>();

        if(root == null) {
            return result;
        }

        visited.push(root);

        while(visited.isEmpty() == false) {
            TreeNode curn = visited.pop();
            result.add(0, curn.val); // 역순으로 저장한다.
            if(curn.left != null) {
                visited.push(curn.left);
            }
            if(curn.right != null) {
                visited.push(curn.right);
            }
        }
        return result;
    }
}
