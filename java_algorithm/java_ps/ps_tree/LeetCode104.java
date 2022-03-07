package java_ps.ps_tree;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class LeetCode104 {

//    public int maxDepth(TreeNode root) {
//
//        if (root == null) {
//            return 0;
//        }
//
//        Queue<TreeNode> q = new LinkedList<>();
//        q.offer(root);
//
//        int count = 0;
//
//        while(!q.isEmpty()) {
//            int size = q.size();
//            count += 1;
//
//            for(int i = 0; i < size; i++) {
//                TreeNode node = q.poll();
//
//                if(node.left != null) {
//                    q.add(node.left);
//                }
//
//                if(node.right != null) {
//                    q.add(node.right);
//                }
//            }
//        }
//        return count;
//    }

    // 재귀를 이용한 풀이
    public int maxDepth(TreeNode root) {
        if(root == null) {
            return 0;
        }

        int left = maxDepth(root.left);
        int right = maxDepth(root.right);

        return Math.max(left, right) + 1;
    }
}
