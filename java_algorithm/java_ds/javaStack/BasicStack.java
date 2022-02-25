package java_ds.javaStack;

import java.util.Arrays;
import java.util.EmptyStackException;

import java_ds.interfaceImpl.StackInterface;

public class BasicStack<E> implements StackInterface<E> {

  private static final int DEFAULT_CAPACITY = 10; // 최소 크기 
  private static final Object[] EMPTY_ARRAY = {}; // 빈 스택(= 배열) 

  private Object[] array; // 요소를 담을 스택
  private int size; // 요소의 갯수를 표시할 변수 

  // 생성자1 - 초기 공간 할당 x 
  public BasicStack() {
    this.array = EMPTY_ARRAY;
    this.size = 0;
  }

  // 생성자2 - 초기 공간 할당 수행 
  public BasicStack(int capacity) {
    this.array = new Object[capacity];
    this.size = 0;
  }

  // resize() - 동적할당을 위한 메서드 
  private void resize() {

    // 빈 스택인 경우 (값 비교)
    if(Arrays.equals(array, EMPTY_ARRAY)) {
      array = new Object[DEFAULT_CAPACITY];
      return;
    }

    int arrayCapacity = array.length; // 현재 스택의 크기 

    // 용량이 가득 찬 경우 
    if(size == arrayCapacity) {
      int newSize = arrayCapacity * 2;

      // 기존의 스택을 복사하여 새로운 용량을 할당 => 깊은 복사 
      array = Arrays.copyOf(array, newSize);
      return;
    }

    // 용량의 절반 미만을 사용하는 경우 
    if(size < (arrayCapacity / 2)) {
      int newCapacity = (arrayCapacity / 2);

      // 용량의 절반이 기본 용량보다 작으면 안된다. 
      array = Arrays.copyOf(array, Math.max(DEFAULT_CAPACITY, newCapacity));
      return; 
    }

  }

  @Override
  public E push(E item) {

    if(size == array.length) { // 용량이 꽉 찬 경우 
      resize(); 
    }

    array[size] = item;
    size++;

    return item;
  }

  @Override
  public E pop() {
    
    if(size == 0) { // 아무 요소가 존재하지 않는 경우 
      throw new EmptyStackException();
    }

    // Object 타입을 E 타입으로 형변환 하기에 발생하는 경고를 무시하는 어노테이션
    // => Object 타입이 E 타입으로 형변환이 불가능 할 수 있는 가능성 때문에 발생하는 경고
    // => Stack의 입력값은 오직 E 타입이므로, 형 안정성이 보장되기 때문에 무시해도 괜찮다.  
    @SuppressWarnings("unchecked") 
    E obj = (E) array[size - 1]; // 삭제될 요소의 값을 저장하는 변수
    
    array[size - 1] = null;
    size--;
    resize();

    return obj;
  }

  @SuppressWarnings("unchecked")
  @Override
  public E peek() {

    if(size == 0) {
      throw new EmptyStackException();
    }

    return (E) array[size - 1];
  }

  @Override
  public int search(Object value) {

    for(int idx = size; idx >= 0; size--) {

      if(array[idx].equals(value)) {
        return size - idx;
      }
    }
    return -1;
  }

  @Override
  public int size() {
    return size;
  }

  @Override
  public void clear() {

    for(int i = 0; i < size; i++) {
      array[i] = null;
    }
    size = 0;
    resize();
  }

  @Override
  public boolean empty() {
    return size == 0;
  }
  
}
