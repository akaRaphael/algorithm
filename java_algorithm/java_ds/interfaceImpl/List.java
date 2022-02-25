package java_ds.interfaceImpl;

public interface List<E> { // List 인터페이스를 직접 구현해보자. 

  // add(E value) - 리스트에 요소를 추가하는 기능 
  // 중복 요소가 존재하는 경우 false, 중복 요소가 없는 경우 true를 반환 
  boolean add(E value);

  // add(int index, E value) - 리스트의 특정 위치에 요소를 추가하는 기능 
  void add(int index, E value);

  // remove(int index) - 리스트의 특정 위치의 요소를 삭제하는 기능, 삭제된 요소를 반환한다. 
  E remove(int index);

  // remove(Object value) - 리스트의 특정 요소를 삭제하는 기능, 동일 요소 존재 시 처음 검색된 요소만 삭제 
  // 삭제에 실패한 경우 false, 성공한 경우 true를 반환 
  boolean remove(Object value);

  // get(int index) - 리스트의 특정 위치의 요소를 반환하는 기능. 
  E get(int index);

  // set(int index, E value) - 특정 위치의 요소를 교체하는 기능. 
  void set(int index, E value);

  // contains(Object value) - 리스트에 특정 요소의 존재여부를 반환하는 기능
  boolean contains(Object value);

  // indexOf(Object value) - 리스트의 특정 요소의 index를 반환하는 기능  
  // 해당 요소가 없는 경우 -1을 반환한다. 
  int indexOf(Object value);

  // size() - 리스트가 가진 요소의 갯수를 반환하는 기능  
  int size();

  // isEmpty() - 리스트가 비어있는 경우 true를, 요소가 있다면 false를 반환하는 기능 
  boolean isEmpty();

  // clear() - 리스트의 요소를 모두 삭제하는 기능
  public void clear();
  
}