import java.util.Comparator;

// Definition for singly-linked list.
class ListNode {
  int val;
  ListNode next;
  ListNode() {}

  ListNode(int val) {
    this.val = val; 
  }
  
  ListNode(int val, ListNode next) {
    this.val = val; this.next = next; 
  }
}

public class MergeTwoSortedLists {

  public static void main(String[] args) {}

  public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

    if(list1 == null) {
      return list2;
    }

    if(list2 == null) {
      return list1;
    }

    ListNode temp = new ListNode(0);
    ListNode curn = temp;

    while(list1 != null && list2 != null) {

      if(list1.val < list2.val) {
        curn.next = list1;
        list1 = list1.next;
      } else {
        curn.next = list2;
        list2 = list2.next;
      }
      curn = curn.next;
    }

    // while 문의 조건이 위배되었을 때 (list1, list2 중 하나가 null)

    if(list1 != null) {
      curn.next = list2;
      list2 = list2.next;
    }

    if(list2 != null) {
      curn.next = list1;
      list1 = list1.next;
    }

    return temp.next; 
  }
}