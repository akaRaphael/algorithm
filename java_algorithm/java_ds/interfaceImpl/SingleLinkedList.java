package java_algorithm.java_ds.interfaceImpl;

import java.util.NoSuchElementException;

public class SingleLinkedList<E> implements List<E> {

  class Node<E> {
    E data;
    Node<E> next; // 다음 노드의 위치를 나타내는 참조데이터
  
    Node(E data) {
      this.data = data;
      this.next = null; 
    }
  }

  private Node<E> head; // 시작 노드 
  private Node<E> tail; // 마지막 노드 
  private int size; // 요소의 갯수 

  // 1. 생성자 
  public SingleLinkedList() {
    this.head = head;
    this.tail = tail;
    this.size = 0;
  }

  // 2. search(int index) - 특정 위치의 노드를 탐색하여 반환
  private Node<E> search(int index) {

    // index 범위를 벗어나는 경우 
    if(index < 0 || index >= size) {
      throw new IndexOutOfBoundsException();
    }

    Node<E> node = head; // head 노드부터 탐색을 시작 

    for(int i = 0; i < index; i++) {
      node = node.next; // 삭제할 노드 (index로 접근할 수 없으므로 next를 사용하여 접근)
    }

    return node;
  }

  // 3. addFirst(E value) - head 위치에 새로운 노드를 삽입
  public void addFirst(E value) {

    Node<E> newNode = new Node<E>(value);
    newNode.next = head;
    head = newNode;
    size++; 

    // 연결리스트에 추가한 노드 뿐이라면, 마지막 노드를 시작노드로 설정
    if(head.next == null) {
      tail = head;
    }
  }

  // 4. addList(E value) - tail 위치에 새로운 노드를 삽입
  public void addLast(E value) {
    
    Node<E> newNode = new Node<E>(value);

    if(size == 0) { // 만약 기존 연결리스트에 노드가 존재하지 않는 경우 
      addFirst(value);
      return;
    }

    tail.next = newNode;
    tail = newNode;
    size ++;

  }

  // 5. add(E value) - 마지막 위치에 새로운 노드를 삽입
  @Override
  public boolean add(E value) {
    addLast(value);
    return true;
  }


  // 6. add(int index, E value) - 특정 위치에 새로운 노드를 삽입 
  @Override
  public void add(int index, E value) {

    // index 범주에서 벗어나는 경우
    if(index > size || index < 0) {
      throw new IndexOutOfBoundsException();
    }

    // index가 head의 위치를 가리키는 경우 
    if(index == 0) {
      addFirst(value);
      return;
    }

    // index가 tail의 위치를 가리키는 경우 
    if(index == size){
      addLast(value);
      return;
    }

    // 연결 리스트의 중간에 새로운 노드가 삽입되는 경우 
    Node<E> prevNode = search(index - 1); // 추가 위치의 이전 노드 
    Node<E> nextNode = prevNode.next; // 추가 하려는 위치의 노드 (새로 추가되는 노드의 다음 노드가 된다.) 
    Node<E> newNode = new Node<E>(value); // 추가되는 새로운 노드 생성 

    prevNode.next = null;
    prevNode.next = newNode;
    newNode.next = nextNode;
    size ++;

  }

  // 7. remove() - head 노드를 삭제 
  public E remove() {

    Node<E> headNode = head;

    // 연결리스트에 아무 노드도 없는 경우 
    if (headNode == null) {
      throw new NoSuchElementException();
    }

    // 삭제된 노드를 반환하기 위한 변수 
    E element = headNode.data;

    // head의 다음 노드 == 삭제 후 head가 될 노드 
    Node<E> nextNode = head.next;

    // head 노드의 데이터를 모두 삭제 
    head.data = null;
    head.next = null;

    // head 노드의 다음 노드를 head 노드로 변경 
    head = nextNode;
    size --; // 요소의 갯수를 감소 

    // 삭제한 노드가 연결 리스트의 유일한 노드였을 경우 
    if(size == 0) {
      tail = null;
    }

    // 삭제된 노드의 값을 반환 
    return element; 
  }

  // 8. remove(int index) - 특정 위치의 노드를 삭제 
  @Override
  public E remove(int index) {

    // 삭제할 노드가 head 노드인 경우 
    if(index == 0) {
      return remove();
    }

    // index 범주를 벗어난 경우 
    if(index >= size || index < 0) {
      throw new IndexOutOfBoundsException();
    }

    // 특정 위치의 노드를 삭제
    Node<E> prevNode = search(index - 1); // 삭제할 노드의 이전 노드 
    Node<E> removedNode = prevNode.next; // 삭제할 노드 
    Node<E> nextNode = removedNode.next; // 삭제할 노드의 다음 노드 

    E element = removedNode.data; // 삭제할 노드의 값을 반환할 변수 

    // 삭제할 노드 이전과 다음 노드의 연결설정 
    prevNode.next = nextNode;

    // 삭제할 노드의 데이터를 모두 삭제 
    removedNode.data = null;
    removedNode.next = null;
    size --;

    return element;

  }

  // 9. 특정 데이터를 가진 노드를 삭제
  @Override
  public boolean remove(Object value) {

    Node<E> prevNode = head; // 탐색의 시작점이 될 노드 
    boolean hasValue = false; // 탐색할 때 해당 데이터를 가진 노드의 존재여부를 표시 
    Node<E> node = head; // 탐색으로 삭제할 노드가 담길 객체 

    for (; node != null; node = node.next) {
      if(value.equals(node.data)) { // value와 일치하는 데이터를 가진 노드를 탐색
        hasValue = true;
        break;
      }

      prevNode = node;
    }

    // 일치하는 노드가 없는 경우 (연결 리스트에 노드가 아예 없는 경우)
    if (node == null) {
      return false;
    }

    // 삭제 하려는 노드(node)가 head 노드인 경우 
    if(node.equals(head)) {
      remove();
      return true;
    }

    else {
      // 삭제될 노드(node) 이전과 다음 노드의 연결 설정 
      prevNode.next = node.next;

      node.data = null;
      node.next = null;
      size --;

      return true;
    }
  }

  // 10. get(int index) - 특정 위치의 노드가 가진 data를 반환 
  @Override
  public E get(int index) {
    return search(index).data;
  }

  // 11. set(int index, E value) - 특정 위치의 노드가 가진 값을 교체
  @Override
  public void set(int index, E value) {
    Node<E> targetNode = search(index);
    targetNode.data = null;
    targetNode.data = value;
  }

  // 12. indexOf(Object value) - 특정 데이터를 가진 노드의 index를 반환 
  public int indexOf(Object value) {

    int index = 0;

    for (Node<E> node = head; node != null; node = node.next) {
      if (value.equals(node.data)){
        return index;
      }
      index ++;
    }

    // 특정 데이터를 가진 노드가 없는 경우
    return -1;
  }

  // 13. contains(Object value) - 특정 데이터를 가진 노드의 존재여부를 반환 
  @Override
  public boolean contains(Object value) {
    return indexOf(value) >= 0;
  }

  // 14. size() - 연결 리스트를 구성하는 노드의 갯수를 반환 
  @Override
  public int size() {
    return size;
  }

  // 15. isEmpty() - 연결 리스트에 노드의 존재여부를 반환
  @Override
  public boolean isEmpty() {
    return size == 0;
  }

  // 16. clear() - 연결 리스트의 모든 노드를 삭제
  @Override
  public void clear() {
    for(Node<E> node = head; node != null; node = node.next) {
      Node<E> nextNode = node.next; // 노드의 참조 데이터까지 삭제해야하므로 미리 다음 노드를 저장한다.
      node.data = null;
      node.next = null;
      node = nextNode; 
    }

    head = tail = null;
    size = 0;
  }
}
