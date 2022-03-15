package java_ps.crack_algo.TwoPointers;

public class LeetCode19 {

    public ListNode removeNthFromEnd(ListNode head, int n) {
       ListNode head1 = head;
       ListNode head2 = head;

       // 만약 n이 2라면, head1을 2칸 앞선 위치에서 시작한다.(for문)
       // head2를 head1의 노드가 남은만큼 next로 이동시키면 2만큼 남은 위치에서 head2는 멈추게 된다.(while문)
       // 즉, 이렇게 하면 head2.next가 지워야하는 node를 가리키게 된다. (마지막 if~else문)
       // 이 원리를 이용하여 푸는 문제다.
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
