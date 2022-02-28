package java_ps.ps_linkedList;

public class LeetCode83 {

     //Definition for singly-linked list.
     static class ListNode {
         int val;
         ListNode next;
         ListNode() {}
         ListNode(int val) { this.val = val; }
         ListNode(int val, ListNode next) { this.val = val; this.next = next; }
     }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(1);
        head.next.next = new ListNode(2);
        head.next.next.next = new ListNode(3);
        head.next.next.next.next = new ListNode(3);

        LeetCode83 foo = new LeetCode83();
        foo.deleteDuplicates(head);
    }

    public ListNode deleteDuplicates(ListNode head) {
         if(head == null) {
             return head;
         }

         ListNode prev = head;
         ListNode curn = head.next;
         ListNode result = prev;

         while(curn != null) {
             if(prev.val == curn.val) {
                 if(curn.next != null) {
                     prev.next = curn.next;
                 } else {
                     prev.next = null;
                 }
             }
             else {
                 prev = prev.next;
             }
             curn = curn.next;
         }
         return result;
    }
}
