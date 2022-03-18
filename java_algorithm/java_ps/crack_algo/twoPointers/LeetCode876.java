package java_ps.crack_algo.twoPointers;

public class LeetCode876 {
    public ListNode middleNode(ListNode node) {
        ListNode first = node;
        ListNode second = node;

        while(second != null && second.next != null) {
            first = first.next;
            second = second.next.next;
        }

        return first;
    }

//    public ListNode middleNode(ListNode node) {
//
//        int len = ListLength(node);
//
//        if(len < 2) {
//            return node;
//        }
//
//        int mid = len / 2 + 1;
//
//        while(mid > 0) {
//            mid --;
//            node = node.next;
//        }
//        return node;
//    }
//
//    public int ListLength(ListNode node) {
//        int count = 0;
//
//        while(node != null) {
//            count++;
//            node = node.next;
//        }
//
//        return count;
//    }
}
