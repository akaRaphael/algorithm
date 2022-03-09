package java_ps.ds_challenge1.ps_tree;

public class LeetCode112 {

    public boolean hasPathSum(TreeNode root, int targetSum) {

        if(root == null) {
            return false;
        }

        if(targetSum - root.val == 0 && root.left == null && root.right == null) {
            return true;
        }

        return (hasPathSum(root.left, targetSum - root.val) ||
                hasPathSum(root.right, targetSum - root.val));
    }
}
