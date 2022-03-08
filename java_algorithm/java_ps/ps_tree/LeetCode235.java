package java_ps.ps_tree;

import java.util.Stack;

public class LeetCode235 {

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

        if(p.val < root.val && q.val < root.val) {
            return lowestCommonAncestor(root.left, p, q);
        }
        else if(p.val > root.val && q.val > root.val) {
            return lowestCommonAncestor(root.right, p, q);
        } else {
            return root;
        }
    }
}
