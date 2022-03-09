package java_ps.ds_challenge1.ps_tree;

public class LeetCode101 {

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
