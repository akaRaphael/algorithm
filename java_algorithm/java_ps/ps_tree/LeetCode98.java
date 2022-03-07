package java_ps.ps_tree;

import java.util.ArrayList;
import java.util.Stack;

public class LeetCode98 {

    // Stack을 사용하여 탐색하는 방법
    public boolean isValidBST2(TreeNode root) {
        Stack<TreeNode> parentStack = new Stack();
        double left_child_val = -Double.MAX_VALUE;

        while(!parentStack.isEmpty() || root != null) {
            while(root != null) {
                parentStack.push(root);
                root = root.left; // 왼쪽부터 탐색
            }
            root = parentStack.pop();
            if(root.val <= left_child_val) return false;
            // 최초에 left_child_val는 무조건 root.val 보다 작다.
            // 그러므로 해당 조건은 false이므로 실행되지 않음
            // => 이렇게 만든 이유는 최초의 root가 말단노드 이므로 검증할 필요가 없기 때문임
            // => 왼쪽부터 탐색을 했기 때문에, 최초의 root는 말단노드다.
            // => 그 다음에 Stack에서 나올 노드는 부모노드가 된다.

            left_child_val = root.val; // BST를 검증하기 위해서 최초의 말단노드가 새로운 기준이 됨.
            root = root.right;
        }
        return true;
    }

    public boolean isValidBST(TreeNode root) {

        return checkBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    public boolean checkBST(TreeNode root, long min, long max) {
        if(root == null) {
            return true;
        }

        if(root.val <= min || root.val >= max) {
            return false;
        }

        return checkBST(root.left, min, root.val) && checkBST(root.right, root.val, max);
    }

}
