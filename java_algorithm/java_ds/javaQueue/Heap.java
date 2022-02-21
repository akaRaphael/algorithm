package java_algorithm.java_ds.javaQueue;

import java.util.Arrays;
import java.util.Comparator;
import java.util.NoSuchElementException;

public class Heap<E> { // minHeap 구현

  // 객체를 임의의 순서로 정렬하고 싶을때 compartor를 파라미터로 받아 설정할 수 있다.
  private final Comparator<? super E> comparator; 
  private static final int DEFAULT_CAPACITY = 10; // 최소 크기 

  private int size;

  private Object[] array; 

  public Heap() { // 생성자1 - 초기 공간 할당 x
    this(null);
  }

  public Heap(Comparator<? super E> comparator) { // 생성자2 - 초기 공간 할당 없이 객체 정렬방식 설정 
    this.array = new Object[DEFAULT_CAPACITY];
    this.size = 0;
    this.comparator = comparator;
  }

  public Heap(int capacity) { // 생성자3 - 초기 공간 할당 o
    this(capacity, null);
  }

  public Heap(int capacity, Comparator<? super E> comparator) { // 생성자4 - 초기 공간 할당 및 객체 정렬방식 설정 
    this.array = new Object[capacity];
    this.size = 0;
    this.comparator = comparator;
  }


  private int getParent(int index) {
    return index / 2;
  }

  private int getLeftChild(int index) {
    return index * 2;
  }

  private int getRightChild(int index) {
    return index * 2 + 1;
  }

  private void resize(int newCapacity) { // 크기 재조정을 위한 기능 
    Object[] newArray = new Object[newCapacity];

    for(int i = 1; i <= size; i++) { // 요소를 복사 
      newArray[i] = array[i];
    }

    this.array = null;
    this.array = newArray;
  }

  // add(), 원소 추가 과정  
  // - 배열의 가장 마지막 위치에 새로운 원소를 추가한다.
  // - 단말 노드의 위치에서 부모노드와 크기를 비교하여 swap한다.
  // - minHeap 이므로 부모노드가 자식노드보다 작을 때까지 swap한다.
  // - 부모노드와 비교하는 과정을 거치므로 새로 추가된 노드는 아래에서 위로 올라간다. (상향 선별, sift-up)

  public void add(E value) {

    // 배열이 꽉찬 경우, size + 1이 새로 추가되는 요소가 들어갈 index가 된다.
    // Heap은 index 1번 부터 요소를 채우기 때문에 size == 요소의 갯수가 된다. 
    if(size + 1 == array.length) { 
      resize(array.length * 2);
    }

    siftUp(size + 1, value); // 새로운 요소가 추가될 위치와 값을 매개변수로 받음
    size++;
  }

  public void siftUp(int idx, E target) {

    if(comparator != null) {
      siftUpComparator(idx, target, comparator);
    } else {
      siftUpComparable(idx, target);
    }
  }

  // comparator를 이용한 정렬 
  @SuppressWarnings("unchecked")
  private void siftUpComparator(int idx, E target, Comparator<? super E> comparator) {

    while(idx > 1) { // idx가 root 노드의 idx(= 1)보다 클 때까지만 탐색
      int parentIdx = getParent(idx);
      Object parentVal = array[parentIdx]; // 부모 노드의 값

      // 타겟 노드의 값이 부모보다 크면 반복문 종료 (minHeap 이기 때문)
      // maxHeap을 구하고 싶다면 부호를 <= 로 설정한다. 
      if(comparator.compare(target, (E) parentVal) >= 0) { 
        break;
      }

      // 부모노드가 추가된 요소보다 값이 큰 경우, 현재 index가 가리키는 위치로 부모노드가 이동
      array[idx] = parentVal;
      idx = parentIdx;
    }
    array[idx] = target;
  }

  // Comparable을 이용한 정렬 
  private void siftUpComparable(int idx, E target) {

    // 타겟 노드가 비교될 수 있도록 comparable 객체를 생성 
    Comparable<? super E> comparable = (Comparable<? super E>) target;

    while(idx > 1) {
      int parentIdx = getParent(idx);
      Object parentVal = array[parentIdx];

      // maxHeap을 구하고 싶다면 부호를 <= 로 설정한다.
      if(comparable.compareTo((E)parentVal) >= 0) {
        break;
      }

      array[idx] = parentVal;
      idx = parentIdx;

    }

    array[idx] = comparable;

  }

  // ============== 요소 삭제 
  @SuppressWarnings("unchecked")
  public E remove() {
    if(array[1] == null) { // root가 비어있는 경우 
      throw new NoSuchElementException();
    }

    E result = (E) array[1]; // 반환될 root 값 
    E target = (E) array[size]; // 가장 마지막에 위치한 요소 
    array[size] = null; 

    // root를 삭제하고 target(마지막 요소)을 root로 올려서 비교를 진행 
    // 새로운 root 값을 찾는다. 
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

  // Comparator를 이용한 siftDown
  @SuppressWarnings("unchecked")
  private void siftDownComparator(int idx, E target, Comparator<? super E> comparator) {

    array[idx] = null; // 루트 노드 삭제, idx에는 1이 들어온다. 
    size--;

    int parentIdx = idx;
    int childIdx;

    // 가장 마지막 요소까지 비교를 진행 
    while((childIdx = getLeftChild(parentIdx)) <= size) {

      int rightChildIdx = getRightChild(parentIdx);
      Object childVal = array[childIdx];

      // 오른쪽 자식의 index가 size보다 작으면서,왼쪽 자식이 오른쪽 자식보다 큰 경우
      // 즉, 더 작은 자식노드가 오른쪽 자식인 경우에 교체되야하는 값(childIdx, childVal)을 오른쪽 자식 노드로 변경 
      if(rightChildIdx <= size && comparator.compare((E) childVal, (E) array[rightChildIdx]) > 0) {
        childIdx = rightChildIdx;
        childVal = array[childIdx];
      }

      // 재배치할 노드가 자식 노드보다 작은 값을 가진 경우, 비교 중단. 
      // 현재 위치가 재배치할 노드의 위치가 된다.
      if(comparator.compare(target, (E) childVal) <= 0) {
        break;
      }

      array[parentIdx] = childVal;
      parentIdx = childIdx;
    }

    array[parentIdx] = target;
    
    if(array.length > DEFAULT_CAPACITY && size < array.length / 4) {
      resize(Math.max(DEFAULT_CAPACITY, array.length/2));
    }
  }

  // comparable을 이용한 siftDown
  @SuppressWarnings("unchecked")
  private void siftDownComparable(int idx, E target) {

    Comparable<? super E> comparable = (Comparable<? super E>) target;

    array[idx] = null;
    size--;

    int parentIdx = idx;
    int childIdx;

    while((childIdx = getLeftChild(parentIdx)) <= size) {

      int rightChildIdx = getRightChild(parentIdx);
      Object childVal = array[childIdx];

      if(rightChildIdx <= size && ((Comparable<? super E>) childVal).compareTo((E) array[rightChildIdx]) > 0 ) {
        childIdx = rightChildIdx;
        childVal = array[childIdx];
      }

      if(comparable.compareTo((E) childVal) <= 0) {
        break;
      }

      array[parentIdx] = childVal;
      parentIdx = childIdx;
    }

    array[parentIdx] = comparable;

    if(array.length > DEFAULT_CAPACITY && size < array.length / 4) {
      resize(Math.max(DEFAULT_CAPACITY, array.length / 2));
    }
  }

  public int size() {
    return this.size;
  }

  @SuppressWarnings("uncheckded")
  public E peek() {
    if(array[1] == null) {
      throw new NoSuchElementException();
    }

    return (E) array[1];
  }

  public boolean isEmpty() {
    return size == 0;
  }

  public Object[] toArray() {
    return Arrays.copyOf(array, size + 1);
  }
}
