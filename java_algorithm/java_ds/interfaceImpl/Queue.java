package java_algorithm.java_ds.interfaceImpl;

public interface Queue<E> {

  // 큐의 가장 마지막에 요소를 추가하는 기능 
  // input - E 자료형의 데이터
  // return - 성공적으로 추가가 되면 true, 아니면 false
  boolean offer(E e);

  // 큐의 첫번째 요소를 삭제하고, 그 요소를 반환하는 기능 
  // return - 삭제된 요소 
  E poll();

  // 큐으 첫번째 요소를 반환하는 기능
  // return - 큐의 첫번째 요소 
  E peek();
  
}
