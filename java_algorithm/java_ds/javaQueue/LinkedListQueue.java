package java_algorithm.java_ds.javaQueue;

import java.util.NoSuchElementException;

import java_algorithm.java_ds.interfaceImpl.Queue;

public class LinkedListQueue<E> implements Queue<E> {

  class Node<E> {
    E data;
    Node<E> next; // 다음 노드를 가리키는 변수 
  
    Node(E data) {
      this.data = data;
      this.next = null;
    } 
  }

  private Node<E> head;
  private Node<E> tail;
  private int size;

  public LinkedListQueue() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  @Override
  public boolean offer(E value) {

    Node<E> newNode = new Node<E>(value);

    if (size == 0) {
      head = newNode;
    } else {
      tail.next = newNode;
    }

    tail = newNode;
    size++;

    return true;
  }

  @Override
  public E poll() {

    if (size == 0) {
      return null;
    }

    E element = head.data;
    Node<E> nextNode = head.next;

    head.data = null;
    head.next = null;

    head = nextNode;
    size--;

    return element;
  }

  public E remove() {
    E element = poll();

    if (element == null) {
      throw new NoSuchElementException();
    }

    return element;
  }

  @Override
  public E peek() {

    if (size == 0) {
      return null;
    }

    return head.data;
  }

  public E element() {
    E element = peek();

    if(element == null) {
      throw new NoSuchElementException();
    }

    return element;
  }

  public int size() {
    return size;
  }

  public boolean isEmpty() {
    return size == 0;
  }

  public boolean contains(Object value) {
    for (Node<E> node = head; node != null; node = node.next) {
      if(value.equals(node.data)) {
        return true;
      }
    }
    return false;
  }

  public void clear() {
    for(Node<E> node = head; node != null;) {

      Node<E> next = node.next;
      node.data = null;
      node.next = null;
      node = next;
    }

    size = 0;
    head = tail = null;
  }
}