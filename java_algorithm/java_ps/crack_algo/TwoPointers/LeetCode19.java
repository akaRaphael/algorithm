package java_ps.crack_algo.TwoPointers;

public class LeetCode19 {

    public ListNode removeNthFromEnd(ListNode head, int n) {
       ListNode head1 = head;
       ListNode head2 = head;

       for(int i = 0; i < n; i++) {
           head1 = head1.next;
       }

       if(head1 == null) {
           return head.next;
       }

       while(head1.next != null) {
           head1 = head1.next;
           head2 = head2.next;
       }

       if(head2.next.next == null) {
           head2.next = null;
       } else {
           head2.next = head2.next.next;
       }

       return head;
    }
}
