package java_ps.ps_tree;

public class LeetCode226 {
    public TreeNode invertTree(TreeNode root) {

        // DFS를 이용한 방법
        // => 재귀를 이용하여 말단노드까지 탐색한다.
        // => 말단 노드부터 비즈니스 로직을 적용
        // => root.left와 root.right에서 root는 동일한 객체다.

        if(root == null) return null;

        invertTree(root.left);
        invertTree(root.right);

        TreeNode newTree = root.right;
        root.right = root.left;
        root.left = newTree;

        return root;
    }
}
