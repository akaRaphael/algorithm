package java_algorithm.java_ds;

import java.util.Stack;

public class UseStack {

  public static void main(String[] args) {

    // 1. Stack 선언하기 
    // => Stack 인터페이스는 Vector 인터페이스를 상속받는다. 
    // => Vector는 
    Stack<Integer> intStack = new Stack<>();

    // 2. Stack 값 추가 
    intStack.push(1);
    intStack.push(2);
    intStack.push(3);

    // 3. Stack.pop() => 가장 마지막에 삽입된 요소를 반환 
    System.out.println(intStack.pop());
    

    // 4. Stack.search(Object o) => 특정 요소의 index를 반환  
    System.out.println(intStack.search(3)); // 가장 마지막 요소는 index = -1 을 반환 
    System.out.println(intStack.search(2)); // 가장 마지막 요소 외에는 본래의 index를 반환 
    System.out.println(intStack.search(1)); // 가장 마지막 요소 외에는 본래의 index를 반환 

    // 5. Stack.clear() => 요소 값 전부 삭제 
    intStack.clear();
    
  }
}
