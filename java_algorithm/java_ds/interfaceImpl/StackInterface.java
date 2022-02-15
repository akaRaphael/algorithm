package java_algorithm.java_ds.interfaceImpl;

public interface StackInterface<E> {

  // 1. 스택의 맨 위에 요소를 추가하는 기능
  // param - 추가될 요소, return - 스택에 추가된 요소 
  E push (E item);

  // 2. 스택의 맨 위의 요소를 제거하고, 제거한 요소를 반환하는 기능
  // return - 제거된 요소 
  E pop();

  // 3. 스택의 맨 위의 요소를 반환하는 기능 (제거 x)
  // return - 스택의 맨 위의 요소
  E peek();

  // 4. 스택 내부에 특정 요소가 맨 위에서부터 몇번째에 존재하는지 알려주는 기능 
  // param - 검색할 요소, return - 특정 요소의 위치 
  int search(Object value)

  // 5. 스택 내부 요소의 갯수를 반환하는 기능 
  // return - 스택 내부 요소의 갯수 
  int size();

  // 6. 스택 내부의 모든 요소를 제거하는 기능 
  void clear();

  // 7. 스택 내부에 요소의 존재유무를 알려주는 기능 
  // return - 요소가 없다면 true, 요소가 있다면 false
  boolean empty();
  

}
