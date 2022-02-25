package java_ds.javaQueue;

import java.util.NoSuchElementException;

import java_ds.interfaceImpl.Queue;

public class ArrayDeque<E> implements Queue<E> {

  private static final int DEFAULT_CAPACITY = 64;

  private Object[] array; // 요소를 담을 배열
  private int size; // 요소의 갯수

  private int front; // 시작 위치를 나타냄 (front + 1 위치부터 데이터가 있음)
  private int rear; // 끝 위치를 나타냄 (rear 위치에 데이터가 있음)

  public ArrayDeque() { // 초기 크기 할당 x
    this.array = new Object[DEFAULT_CAPACITY];
    this.size = 0;
    this.front = 0;
    this.rear = 0;
  }

  public ArrayDeque(int capacity) { // 초기 크기 할당 o
    this.array = new Object[capacity];
    this.size = 0;
    this.front = 0;
    this.rear = 0;
  }

  private void resize(int newCapacity) {

    int arrayCapacity = array.length;
    Object[] newArray = new Object[newCapacity];

    // i = newArray의 인덱스
    // j = 기존 array의 인덱스
    for(int i = 1, j = front + 1; i <= size; i++, j++) {
      newArray[i] = array[j % arrayCapacity];
    }

    this.array = null;
    this.array = newArray;

    front = 0;
    rear = size;

  }

  @Override
  public boolean offer(E item) {
    return offerLast(item);
  }

  public boolean offerLast(E item) {

    if((rear + 1) % array.length == front) {
      resize(array.length * 2);
    }

    rear = (rear + 1) % array.length;
    array[rear] = item;

    size++;

    return true;
  }

  public boolean offerFirst(E item) {
    if((front - 1 + array.length) % array.length == rear) {
      resize(array.length * 2);
    }

    array[front] = item;
    front = (front - 1 + array.length) % array.length;
    size++;

    return true;
  }

  @Override
  public E poll() {
    return pollFirst();
  }

  public E pollFirst() {
    if(size == 0) {
      return null;
    }

    front = (front + 1) % array.length; // front + 1 위치에 데이터가 있다.
    
    @SuppressWarnings("unchecked")
    E item = (E) array[front];

    array[front] = null;
    size--;

    if(array.length > DEFAULT_CAPACITY && size < (array.length / 4)) {
      resize(Math.max(DEFAULT_CAPACITY, array.length / 2));
    }

    return item;
  }

  public E remove() {
    return removeFirst();
  }

  public E removeFirst() {
    E item = pollFirst();

    if (item == null) {
      throw new NoSuchElementException();
    }

    return item;
  }

  public E pollLast() {

    if(size == 0) {
      return null;
    }

    @SuppressWarnings("unchecked")
    E item = (E) array[rear];

    array[rear] = null;
    rear = (rear - 1 + array.length) % array.length;
    size--;

    if(array.length > DEFAULT_CAPACITY && size < (array.length / 4)) {
      resize(Math.max(DEFAULT_CAPACITY, array.length / 2));
    }

    return item;

  }

  public E removeLast() {
    E item = pollLast();

    if(item == null) {
      throw new NoSuchElementException();
    }

    return item;
  }

  @Override
  public E peek() {
    return peekFirst();
  }

  public E peekFirst() {
    if(size == 0) {
      return null;
    }

    @SuppressWarnings("unchecked")
    E item = (E) array[(front + 1) % array.length];

    return item;
  }

  public E peekLast() {
    if(size == 0) {
      return null;
    }

    @SuppressWarnings("unchecked")
    E item = (E) array[rear];

    return item;
  }

  public E element() {
    return getFirst();
  }

  public E getFirst() {
    E item = peek();

    if(item == null) {
      throw new NoSuchElementException();
    }

    return item;
  }

  public E getLast() {
    E item = peekLast();

    if(item == null) {
      throw new NoSuchElementException();
    }

    return item;
  }

  public int size() {
    return size;
  }

  public boolean isEmpty() {
    return size == 0;
  }

  public boolean contains(E item) {

    int start = (front + 1) % array.length;

    for (int i = 0, idx = start; i < size; i++, idx = (idx + 1) % array.length) {
      if (item.equals(array[idx])) {
        return true;
      }
    }
    return false;
  }

  public void clear() {
    if(size == 0) {
      return;
    }

    int start = (front + 1) % array.length;

    for (int i = 0; i < array.length; i++) {
      array[i] = null;
    }

    front = rear = size = 0;

  }
  
}
