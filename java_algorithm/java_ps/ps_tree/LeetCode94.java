package java_ps.ps_tree;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class LeetCode94 {

    public List<Integer> inorderTraversal(TreeNode root) {
        // inorder Traversal(중위순회) = 왼쪽 자식 -> 부모 -> 오른쪽 자식 순으로 순회
        // 반복문을 이용한 풀이

        Stack<TreeNode> stack = new Stack<>();
        List<Integer> result = new ArrayList<>();

        if(root == null) {
            return result;
        }

        TreeNode curn = root;

        while(curn != null || !stack.isEmpty()) {
            while(curn != null) {
                stack.push(curn);
                curn = curn.left;
            }

            curn = stack.pop();
            result.add(curn.val);
            curn = curn.right;
        }

        return result;
    }

    public List<Integer> inorderTraversal2(TreeNode root) {
        // 재귀를 이용한 풀이

        List<Integer> result = new ArrayList<>();

        recursiveTraverse(root, result);

        return result;
    }

    public void recursiveTraverse(TreeNode root, List<Integer> result) {
        if(root == null) {
            return;
        }
        recursiveTraverse(root.left, result);
        result.add(root.val);
        recursiveTraverse(root.right, result);
    }
}
