package java_ps.ps_linkedList;

public class RemoveLinkedListEle {

    // Definition for singly-linked list.
    static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public static void main(String[] args) {
    }

    public ListNode removeElements(ListNode head, int val) {

        if(head == null) {
            return head;
        }
        ListNode temp = new ListNode(0);
        temp.next = head;

        ListNode slow = temp;
        ListNode fast = head;

        while(fast != null) {
            if(fast.val == val) {
                slow.next = fast.next;
            } else {
                slow = slow.next;
            }
            fast = fast.next;
        }
        return temp.next;
    }
}
