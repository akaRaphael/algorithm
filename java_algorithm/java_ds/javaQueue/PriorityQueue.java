package java_ds.javaQueue;

import java_ds.interfaceImpl.Queue;
import java.util.Comparator;
import java.util.NoSuchElementException;


public class PriorityQueue<E> implements Queue<E>{

  private final Comparator<? super E> comparator;
  private static final int DEFAULT_CAPACITY = 10;

  private int size;
  private Object[] array;

  public PriorityQueue() {
    this(null);
  }

  public PriorityQueue(Comparator<? super E> comparator) {
    this.array = new Object[DEFAULT_CAPACITY];
    this.size = 0;
    this.comparator = comparator;
  }

  public PriorityQueue(int capacity) {
    this(capacity, null);
  }

  public PriorityQueue(int capacity, Comparator<? super E> comparator) {
    this.array = new Object[capacity];
    this.size = 0;
    this.comparator = comparator;
  }

  private int getParentIdx(int index) {
    return index / 2;
  }

  private int getLeftChildIdx(int index) {
    return index * 2;
  }

  private int getRightChildIdx(int index) {
    return index * 2 + 1;
  }

  private void resize(int newCapacity) {

    Object[] newArray = new Object[newCapacity];

    for (int i = 1; i <= size; i++) {
      newArray[i] = array[i];
    }

    this.array = null;
    this.array = newArray;
  }

  @Override
  public boolean offer(E value) {

    if(size + 1 == array.length) {
      resize(array.length * 2);
    }

    siftUp(size + 1, value);
    size++; 

    return true;
  }

  private void siftUp(int idx, E target) {
    if(comparator != null) {
      siftUpComparator(idx, target, comparator);
    } else {
      siftUpComparable(idx, target);
    }
  }

  @SuppressWarnings("unchecked")
  private void siftUpComparator(int idx, E target, Comparator<? super E> comparator) {

    while(idx > 1) {
      int parentIdx = getParentIdx(idx);
      Object parentVal = array[parentIdx];

      if(comparator.compare(target, (E)parentVal) >= 0) {
        break;
      }

      array[idx] = parentVal;
      idx = parentIdx;
    }
    array[idx] = target;
  }

  @SuppressWarnings("unchecked")
  private void siftUpComparable(int idx, E target) {
    Comparable<? super E> comparable = (Comparable<? super E>) target;

    while(idx > 1) {
      int parentIdx = getParentIdx(idx);
      Object parentVal = array[parentIdx];

      if(comparable.compareTo((E)parentVal) >= 0) {
        break;
      }

      array[idx] = parentVal;
      idx = parentIdx;
    }
    array[idx] = comparable;
  }

  @Override
  public E poll() {
    if(array[1] == null) {
      return null;
    }

    return remove();
  }

  private E remove() {
    if(array[1] == null) {
      throw new NoSuchElementException();
    }

    E result = (E) array[1];
    E target = (E) array[size];

    array[size] = null;
    size--;
    siftDown(1, target);

    return result;
  }

  private void siftDown(int idx, E target) {
    if(comparator != null) {
      siftDownComparator(idx, target, comparator);
    } else {
      siftDownComparable(idx, target);
    }
  }

  private void siftDownComparator(int idx, E target, Comparator<? super E> comparator) {
    array[idx] = null;

    int parentIdx = idx;
    int childIdx;

    while((childIdx = getLeftChildIdx(parentIdx)) <= size) {
      int rightIdx = getRightChildIdx(parentIdx);
      Object childVal = array[childIdx];

      if(rightIdx <= size && comparator.compare((E)childVal, (E)array[rightIdx]) > 0) {
        childIdx = rightIdx;
        childVal = array[childIdx];
      }

      if(comparator.compare(target, (E) childVal) <= 0) {
        break;
      }

    }
    array[parentIdx] = target;

    if(array.length > DEFAULT_CAPACITY && size < array.length / 4) {
      resize(Math.max(DEFAULT_CAPACITY, array.length / 2));
    }
  }

  @SuppressWarnings("unchecked")
  private void siftDownComparable(int idx, E target) {
    Comparable<? super E> comparable = (Comparable<? super E>) target;
    
    array[idx] = null;
    int parentIdx = idx;
    int childIdx; 

    while((childIdx = getLeftChildIdx(parentIdx)) <= size) {
      int rightChildIdx = getRightChildIdx(parentIdx);
      Object childVal = array[childIdx];

      if(rightChildIdx <= size && ((Comparable<? super E>) childVal).compareTo((E) array[rightChildIdx]) > 0) {
        childIdx = rightChildIdx;
        childVal = array[rightChildIdx];
      }

      if(comparable.compareTo((E)childVal) <= 0) {
        break;
      }

      array[parentIdx] = comparable;
      parentIdx = childIdx;
    }

    array[parentIdx] = comparable;

    if(array.length > DEFAULT_CAPACITY && size < array.length / 4) {
      resize(Math.max(DEFAULT_CAPACITY, array.length / 2));
    }
  }

  public int size() {
    return size;
  }


  @Override
  @SuppressWarnings("unchecked")
  public E peek() {
    if(array[1] == null) {
      throw new NoSuchElementException();
    } else {
      return (E)array[1];
    }
  }

  public boolean isEmpty() {
    return size == 0;
  }

  public boolean contains(Object value) {
    for(int i = 1; i <= size; i++) {
      if(array[i] == value) {
        return true;
      }
    }
    return false;
  }

  public void clear() {
    for(int i = 1; i <= size; i++) {
      array[i] = null;
    }
    size = 0;
  }

}
