package java_algorithm.java_ds.interfaceImpl;

import java.util.NoSuchElementException;

public class DLinkedList<E> implements List<E> { // 이중연결리스트 구현

  class Node<E> {

    E data;
    Node<E> next;
    Node<E> prev;
  
    Node(E data) {
      this.data = data;
      this.next = null;
      this.prev = null;
    }
  }

  private Node<E> head;
  private Node<E> tail;
  private int size;

  public DLinkedList() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  private Node<E> search(int index) {

    if(index >= size || index < 0) {
      throw new IndexOutOfBoundsException();
    }

    // 뒤에서부터 탐색하는 경우 
    if( index > (size / 2)) {

      Node<E> node = tail;
      for(int i = size - 1; i > index; i--) {
        node = node.prev;
      }

      return node;
    } 
    
    else { // 앞에서부터 탐색 

      Node<E> node = head;
      for(int i = 0; i < index; i++) {
        node = node.next;
      }
      return node;
    }
  }

  private void addFirst(E value) {

    Node<E> newNode = new Node<E>(value);
    
    if(head != null) {
      head.prev = newNode;
      newNode.next = head;
      head = newNode;
    }

    if(head == null) {
      head = newNode;
    }

    if(head.next == null) {
      tail = head;
    }
    
    size++;
  }

  @Override
  public boolean add(E value) {
    addLast(value);
    return true;
  }

  public void addLast(E value) {
    Node<E> newNode = new Node<>(value);

    if(size == 0) {
      addFirst(value);
      return;
    }

    tail.next = newNode;
    newNode.prev = tail;
    tail = newNode;
    size++;

  }

  public void add(int index, E value) {

    if(index >= size || index < 0) {
      throw new IndexOutOfBoundsException();
    }

    if (index == 0) {
      addFirst(value);
      return;
    }

    if (index == size) {
      addLast(value);
      return;
    }

    Node<E> prevNode = search(index - 1); // 추가 위치의 이전 노드
    Node<E> nextNode = prevNode.next; // 추가 위치의 노드 
    Node<E> newNode = new Node<>(value); // 추가 될 노드 

    prevNode.next = null;
    nextNode.prev = null;

    prevNode.next = newNode;
    newNode.prev = prevNode;
    newNode.next = nextNode;
    nextNode.prev = newNode;

    size++;
  }

  public E remove() {

    Node<E> headNode = head;

    if(head == null) {
      throw new NoSuchElementException();
    }

    E element = head.data; // 반환될 head노드의 값을 저장 
    Node<E> nextNode = head.next; // head 노드 다음노드

    head.data = null;
    head.next = null;

    if(nextNode != null) {
      nextNode.prev = null;
    }

    head = nextNode;
    size--;

    if(size == 0) {
      tail = null;
    }

    return element;
  }

  @Override
  public E remove(int index) {

    if(index >= size || index < 0) {
      throw new IndexOutOfBoundsException();
    }

    if (index == 0) {
      return remove();
    }

    Node<E> prevNode = search(index - 1);
    Node<E> removedNode = prevNode.next;
	  Node<E> nextNode = removedNode.next;

    E element = removedNode.data;
    
    prevNode.next = null;
    removedNode.next = null;
    removedNode.prev = null;
    removedNode.data = null;
		
    if(nextNode != null) {
      nextNode.prev = null;
        
      nextNode.prev = prevNode;
      prevNode.next = nextNode;
    } else {	 
      tail = prevNode;
    }

    size--;  
    return element;
  }

  @Override
  public boolean remove(Object value) {

    Node<E> prevNode = head;
    Node<E> node = head;

    // 삭제할 값과 동일한 값을 가진 노드 찾기 
    for(; node != null; node = node.next) { 
      if (value.equals(node.data)) {
        break;
      }
      prevNode = node;
    }

    // 노드가 발견되지 않았다면 false 반환 
    if(node == null) {
      return false;
    }

    if(node.equals(head)) {
      remove();
      return true;
    } 
    
    else {

      Node<E> nextNode = node.next;

      prevNode.next = null;
      node.data = null;
      node.next = null;
      node.prev = null;

      if(nextNode != null) {
        nextNode.prev = null;
        nextNode.prev = prevNode;
        prevNode.next = nextNode;
      }
      else {
        tail = prevNode;
      }

      size--;
      return true;
    }
  }

  @Override
  public E get(int index) {
    return search(index).data;
  }

  @Override
  public void set(int index, E value) {
    Node<E> node = search(index);
    node.data = null;
    node.data = value;
  }

  @Override
  public int indexOf(Object value) { // 정방향 탐색
    
    int index = 0;
    for (Node<E> node = head; node != null; node = node.next) {
      if(value.equals(node.data)) {
        return index;
      }
      index ++;

    }
    return -1;

  }

  public int lastIndexOf(Object value) { // 역방향 탐색
    
    int index = size;
    for(Node<E> node = tail; node != null; node = node.prev) {
      index--;
      if(value.equals(node.data)) {
        return index;
      }
    }
    return -1;
  }

  @Override
  public boolean contains(Object item) {
    return indexOf(item) >= 0;
  }

  @Override
  public int size() {
    return size;
  }

  @Override
  public boolean isEmpty() {
    return size == 0;
  }

  @Override
  public void clear() {

    for(Node<E> node = head; node != null;) {
      Node<E> nextNode = node.next;
      node.data = null;
      node.next = null;
      node.prev = null;
      node = nextNode;
    }

    head = tail = null;
    size = 0;
    
  }
}