package java_algorithm.java_ds.javaQueue;

import java.util.NoSuchElementException;

import java_algorithm.java_ds.interfaceImpl.Queue;

public class ArrayQueue<E> implements Queue<E>{

  private static final int DEFUALT_CAPACITY = 64; 

  private Object[] array; // 요소가 담길 배열(queue)
  private int size; // 요소의 갯수 

  private int front;
  private int rear;

  public ArrayQueue() { // 초기값 할당 x
    this.array = new Object[DEFUALT_CAPACITY];
    this.size = 0;
    this.front = 0;
    this.rear = 0;
  }

  public ArrayQueue(int capacity) { // 초기값 할당 o 
    this.array = new Object[capacity];
    this.size = 0;
    this.front = 0;
    this.rear = 0;
  }

  // 큐의 크기를 재할당한다.(크기의 증감은 매개변수에 의해 결정됨)
  private void resize(int newCapacity) { 
    int arrayCapacity = array.length;

    Object[] newArray = new Object[newCapacity];

    for (int i = 1, j = front + 1; i <= size; i++, j++) {
      newArray[i] = array[j % arrayCapacity];
    }

    this.array = null;
    this.array = newArray;

    front = 0; // 새 배열에는 index 1번부터 요소가 추가되므로 front는 0번 index에 위치한다.
    rear = size;

  }

  @Override
  public boolean offer(E item) {

    if((rear + 1) % array.length == front) { // 큐가 꽉 차있는 경우 
      resize(array.length * 2);
    }

    rear = (rear + 1) % array.length;
    array[rear] = item;
    size++;

    return true;
  }

  @Override
  public E poll() { 
    // 첫번째 요소를 삭제하고 반환한다.
    // 삭제할 요소가 없는 경우 null 반환 

    if (size == 0) {
      return null;
    }

    front = (front + 1) % array.length; // 프론트를 한칸 앞으로 옮김

    @SuppressWarnings("unckecked")
    E item = (E) array[front];

    array[front] = null;
    size--;

    // 큐의 크기가 64보다 크지만, 요소의 갯수가 전체 크기의 4분의1 만큼만 존재하는 경우
    if(array.length > DEFUALT_CAPACITY && size < (array.length / 4)) {
      resize(Math.max(DEFUALT_CAPACITY, array.length / 2));
    }

    return item;
  }

  public E remove() {

    // 첫번째 요소를 삭제하는 기능
    // 만약 요소가 존재하지 않으면 NoSuchElementException 발생 

    E item = poll();

    if (item == null) {
      throw new NoSuchElementException();
    }

    return item;
  }

  @Override
  public E peek() { // 큐의 첫번째 요소를 반환하는 기능 

    if (size == 0) {
      return null;
    }

    @SuppressWarnings("unchecked")
    E item = (E) array[(front + 1) % array.length]; 
    // => 만약 front가 큐의 마지막 index에 위치하는 경우, 0번 index가 반환되어야 한다. 

    return item;
  }

  public E element() { // 큐에 요소가 존재하는지 확인하는 기능 
    E item = peek();

    if (item == null) {
      throw new NoSuchElementException();
    }

    return item;
  }

  public int size() { // 큐 요소의 갯수를 반환하는 기능 
    return size;
  }

  public boolean isEmpty() {
    return size == 0;
  }

  public boolean contains(Object value) { // 특정 요소의 존재여부를 반환하는 기능 

    int start = (front + 1) % array.length;

    for (int i = 0, idx = start; i < size; i ++, idx = (idx + 1) % array.length) {
      if(array[idx].equals(value)) {
        return true;
      }
    }

    return false;

  }

  public void clear() { // 큐의 모든 원소를 삭제 
    
    for (int i = 0; i < array.length; i++) {
      array[i] = null;
    }

    front = rear = size = 0;
  }
  
}
