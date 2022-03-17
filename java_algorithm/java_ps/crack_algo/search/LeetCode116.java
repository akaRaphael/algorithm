package java_ps.crack_algo.search;

import java.util.Stack;

public class LeetCode116 {

    // 문제의 핵심
    // 1. 완전 이진 트리라는 것을 이용할 것
    // 2. 최초의 부모노드를 하나 지정해서 탐색을 시작할 것
    // 3. 가장 우측의 node의 next는 자연스럽게 null 값이 된다는 것

    public Node connect(Node root) {
        if (root == null) return root;

        Node leftNode = root;
        while(leftNode.left != null) {
            Node head = leftNode;
            while(head != null) {
                head.left.next = head.right;
                if(head.next != null) {
                    head.right.next = head.next.left;
                }
                head = head.next;
            }
            leftNode = leftNode.left;
        }
        return root;
    }
}
