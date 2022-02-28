package java_ps.ps_linkedList;

public class ReversedLinkedList {

    //Definition for singly-linked list.
     static class ListNode {
          int val;
          ListNode next;
          ListNode() {}
          ListNode(int val) { this.val = val; }
          ListNode(int val, ListNode next) { this.val = val; this.next = next; }
     }

    public ListNode reverseList(ListNode head) {
         if(head == null) {
             return head;
         }

         ListNode prev = null;
         ListNode curn = head;
         ListNode nexn = head;
         while(curn != null) {
             nexn = nexn.next;
             curn.next = prev;
             prev = curn;
             curn = nexn;
         }

         head = prev;
         return prev;
     }
}
