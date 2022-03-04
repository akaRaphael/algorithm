package java_ps.ps_tree;

import java.util.*;

public class LeetCode102 {

    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public List<List<Integer>> levelOrder(TreeNode root) {

        List<List<Integer>> result = new ArrayList<>();

        if(root == null) {
            return result;
        }

        Queue<TreeNode> que = new LinkedList<>();
        que.offer(root);

        while(que.isEmpty() == false) {
            List<Integer> levelList = new ArrayList<>();
            int size = que.size();

            for(int i = 0; i < size; i++) {
                TreeNode node = que.poll();
                levelList.add(node.val);

                if(node.left != null) {
                    que.add(node.left);
                }
                if(node.right != null) {
                    que.add(node.right);
                }
            }
            result.add(levelList);
        }
        return result;
    }
}
