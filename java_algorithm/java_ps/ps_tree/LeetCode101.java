package java_ps.ps_tree;

import java.util.LinkedList;
import java.util.Queue;

public class LeetCode101 {

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

    public boolean isSymmetric(TreeNode root) {

        if(root == null) return false;

        return checkSymmetry(root.left, root.right);
    }

    public boolean checkSymmetry(TreeNode left, TreeNode right) {

        if(left == null && right == null) return true;
        if(left == null || right == null) return false;
        if(left.val != right.val) return false;

        return checkSymmetry(left.left, right.right) && checkSymmetry(left.right, right.left);
    }
}