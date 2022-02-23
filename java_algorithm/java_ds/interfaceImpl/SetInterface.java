package java_algorithm.java_ds.interfaceImpl;

public interface SetInterface<E> {
  
  // Set 자료구조에 요소를 추가하는 기능 
  boolean add(E data);

  // Set 자료구조에서 특정 요소를 삭제하는 기능
  boolean remove(Object data);

  // Set 자료구조에 특정 요소의 존재여부를 확인하는 기능 
  boolean contains(Object data);

  // Set 자료구조가 다른 객체와 동일한지 비교하는 기능 
  boolean equals(Object data);

  // Set 자료구조 내부에 요소의 존재여부를 확인하는 기능
  boolean isEmpty();

  // Set 자료구조의 요소 개수를 반환하는 기능 
  int size();

  // Set 자료구조의 모든 요소를 제거하는 기능 
  void clear();
}
