package java_ps.crack_algo.search;

public class LeetCode617 {

    // 내가 푼 방법
    public TreeNode mergeTrees(TreeNode node1, TreeNode node2) {

        if(node1 == null) {
            return node2;
        }
        else if(node2 == null) {
            return node1;
        }

        mergeNode(node1, node2);

        return node2;
    }

    public void mergeNode(TreeNode node1, TreeNode node2) {

        if(node1 == null) {
            return;
        }
        else if(node1 != null && node2 != null) {
            node2.val += node1.val;
        }
        if(node1.left != null && node2.left == null) {
            node2.left = new TreeNode();
        }
        if(node1.right != null && node2.right == null) {
            node2.right = new TreeNode();
        }
        mergeNode(node1.left, node2.left);
        mergeNode(node1.right, node2.right);
    }

    // 다른 풀이방법 (간결한 코드)
//    public TreeNode mergeTrees(TreeNode node1, TreeNode node2){
//        if(node1 == null & node2 == null) {
//            return null;
//        }
//
//        if(node1 == null && node2 != null) {
//            return node2;
//        }
//
//        if(node1 != null && node2 == null) {
//            return node1;
//        }
//
//        TreeNode result = new TreeNode();
//        result.val = node1.val + node2.val;
//
//        result.left = mergeTrees(node1.left, node2.left);
//        result.right= mergeTrees(node1.right, node2.right);
//
//        return result;
//    }
}
