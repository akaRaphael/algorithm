package java_ps.crack_algo.recursion;

public class LeetCode206 {

    public ListNode reverseList(ListNode head) {
        return reverse(head, null);
    }

    public ListNode reverse(ListNode head, ListNode newHead) {

        if(head == null) return newHead;

        ListNode next = head.next;
        head.next = newHead;
        newHead = head;
        head = next;

        return reverse(head, newHead);
    }
}
