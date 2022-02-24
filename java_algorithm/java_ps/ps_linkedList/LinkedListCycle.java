import java.util.HashMap;

//Definition for singly-linked list.
class ListNode {
  int val;
  ListNode next;
  ListNode(int x) {
      val = x;
      next = null;
  }
}

public class LinkedListCycle {
  public static void main(String[] args) {}

  // 내가 짠 코드 
  public boolean hasCycle(ListNode head) { 
    // cycle의 존재여부를 판단해라. ==> 힌트는 맨 아래에 있음 
    
    HashMap<ListNode, Integer> hashMap = new HashMap<>();

    while(head != null && head.next != null) {

      if(hashMap.get(head) != null) {
        if(hashMap.get(head) == head.val) {
          return true;
        }
      } else {
        hashMap.put(head, head.val);
        head = head.next;
      }
    }
    return false;
  }

  // 다른 사람의 풀이 
  // => 문제의 제약에 보면 Node.val이 10^5 이하라고 표현했다.
  // => 그러므로 이를 이용하여 푼다. 
  public boolean hasCycle2(ListNode head) {
    while (head != null) {
      if (head.val == 9999999) {
        return true;
      }
      head.val = 9999999;
      head = head.next;
    }
    return false;
  }
  
}

// ==> Cycle이 존재하면 같은 객체를 가리킨다. 