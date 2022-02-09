package java_algorithm.java_ds.javaArrayList;

import java.util.Arrays;

import java_algorithm.java_ds.interfaceImpl.List;

public class ArrayListImpl<E> implements List<E>{
  
  private static final int DEFAULT_CAPACITY = 10; // 초기 할당 크기, 상수(static final) 
  private static final Object[] EMPTY_ARRAY = {}; // 빈 배열 선언, 상수 (static final) 

  private int size; // 요소의 갯수(배열의 크기를 말하는게 아니다.)

  Object[] array; // 요소를 담을 배열 

  // 생성자1 (초기 공간 할당을 하지 않는다)
  // => 사용자가 객체만을 미리 생성하는 경우에 사용된다. 
  public ArrayListImpl() {
    this.array = EMPTY_ARRAY;
    this.size = 0;
  }

  // 생성자2 (초기 공간 할당 수행)
  // => 사용자가 객체 생성과 함께 크기를 선언한 경우 사용된다. 
  public ArrayListImpl(int capacity) {
    this.array = new Object[capacity];
    this.size = 0;
  }

  // 동적할당 메소드 
  private void resize() {
    int array_capacity = array.length;

    // case1. array에 아무런 데이터가 없는 경우 
    if (Arrays.equals(array, EMPTY_ARRAY)) { // Arrays.equals() - 동일한 원소의 갯수를 가지면 true 
      array = new Object[DEFAULT_CAPACITY];
      return;
    }

    // case2. 용량이 꽉 찬 경우 => 메모리 부족을 처리 
    if (size == array_capacity) {
      int new_capaicty = array_capacity * 2;

      // 기존 배열을 복사하여, 확장된 크기의 배열로 선언 
      array = Arrays.copyOf(array, new_capaicty); 
      // Arrays.copyOf() - 첫번째 인자인 배열을 복사하여, 두번째 인자인 배열의 길이를 적용한다.
      //                 - 추가된 공간에 요소가 없는 경우 null 값으로 채워진다.  

      return ;
    }

    // case3. 기존 배열 용량의 절반 미만을 사용하는 경우 => 메모리 낭비를 처리 
    if (size < (array_capacity / 2)) {
      int new_capaicty = array_capacity / 2;
      array = Arrays.copyOf(array, new_capaicty);
      return;
    }
  }

  @Override
  public boolean add(E value) {
    addLast(value);
    return true;
  }

  public void addLast(E value) {

    // case1. array가 꽉 차있는 상태 
    if (size == array.length) {
      resize();
    }

    array[size] = value; // array의 마지막 위치에 요소 삽입 
    size ++; // array의 마지막 위치 갱신 

  }

  @Override
  public void add(int index, E value) {

    // case1. index가 범주를 벗어났을 때
    if (index > size || index < 0) {
      throw new IndexOutOfBoundsException();
    }
    
    // case2. index가 마지막 위치를 가리키는 경우 
    if (index == size) {
      addLast(value);
    }

    // case3. array의 중간 위치에 데이터를 삽입하는 경우 
    else {
      
      // 만약 array가 꽉 차 있는 경우 
      if (size == array.length) {
        resize();
      }

      // array의 마지막 위치를 기준으로
      // 삽입 위치까지의 모든 요소를 한칸씩 뒤로 옮기는 작업 
      for (int i = size; i > index; i--) {
        array[i] = array[i - 1];
      }

      array[index] = value; // 삽입 위치에 데이터를 삽입 
      size ++; // array의 마지막 위치를 갱신 
    }
  }

  // array의 맨 앞에 데이터를 삽입하는 경우 
  public void addFirst(E value) {
    add(0, value);
  }

  // get(int index) - 특정 index에 위치한 요소를 반환하는 기능 
  // @SuppressWarnings("unchecked") - 타입 안정성 경고를 무시하는 어노테이션 
  // array는 Object 타입이지만, 삽입되는 데이터는 E 타입이다. 그리고 메서드의 반환 타입은 E 이다. 
  // 이 경우, Object 타입의 배열을 E 타입으로 변환하는 것으로, 메소드의 타입 안정성에 대한 경고가 발생한다.
  // 즉, E 타입으로 변환할 수 없는 경우가 발생할 수 있다는 것이다.
  // 현재 ArrayList 클래스의 설계상, input 데이터는 add() 메소드를 통한 E 타입 밖에 없기 때문에 문제가 되지 않는다.
  // 그러므로 타입 안정성 경고를 무시하는 어노테이션을 부착한 것이다. 
  // 이처럼 설계상의 타입 변환의 예외가 없는 경우에만 이 어노테이션을 사용하도록 하자. 
  // 해당 어노테이션을 남발하는 경우, 정말 큰 에러가 발생할 수 있으며 이를 인식하지 못하게 될 가능성이 크다. 
  @SuppressWarnings("unchecked")
  @Override
  public E get(int index) {

    if (index >= size || index < 0) { // array의 index 범주를 벗어난 경우 
      throw new IndexOutOfBoundsException();
    }

    // Object 타입(array) 에서 E 타입으로 캐스팅해준 다음 반환
    return (E) array[index]; 
  }

  // set(int index, E value) - 특정 index의 데이터를 새로운 value로 교체하는 기능 
  @Override
  public void set(int index, E value) {
    // array의 index 범주를 벗어난 경우 
    if (index >= size || index < 0) {
      throw new IndexOutOfBoundsException();
    }
    else {
      array[index] = value;
    }

  }

  // indexOf(Object value) - 특정 데이터의 index를 반환하는 기능
  @Override
  public int indexOf(Object value) {
    int i = 0;

    // value와 같은 요소일 경우 i를 반환 
    for (i = 0; i < size; i++) {
      if (array[i].equals(value)) {
        return i;
      }
    }
    // 일치하는 데이터가 array에 없는 경우 
    return -1;
  }

  // lastIndexOf(Object value) - 뒤쪽에서부터 데이터를 탐색하여 index를 반환하는 기능 
  public int lastIndexOf(Object value) {
    for (int i = size - 1; i >= 0; i--) {
      if (array[i].equals(value)) {
        return i;
      }
    }

    return -1;
  }

  // contains(Object value) - array의 요소로 value의 존재여부를 반환하는 기능 
  @Override
  public boolean contains(Object value) {
    
    if (indexOf(value) >= 0) {
      return true;
    } else {
      return false;
    }
  }

  // remove(int index) - 특정 위치의 데이터를 삭제하는 기능 
  @SuppressWarnings("unchecked")
  @Override
  public E remove(int index) {

    if (index >= size || index < 0) {
      throw new IndexOutOfBoundsException();
    }

    E element = (E) array[index]; // 타입 안정성의 경고가 발생하는 부분 
    array[index] = null;

    for (int i = index; i < size; i++) {
      array[i] = array[i + 1];
      array[i + 1] = null; // 가비지 컬렉터를 사용하기 위해 null로 명시(메모리 해제) 
    }

    size--;
    resize();
    return element;
  }

  // remove(Object value) - 특정 데이터를 삭제하는 기능 
  @Override
  public boolean remove(Object value) {
    
    // 삭제하고자 하는 요소의 index를 찾는다.
    int index = indexOf(value);

    // 특정 데이터가 존재하지 않는 경우 (index = -1)
    if (index == -1) {
      return false;
    }

    // 특정 index의 요소를 삭제 
    remove(index);
    return true;
  }

  // size() - 요소의 갯수를 반환하는 기능 
  @Override
  public int size() {
    return size;
  }

  // isEmpty() - 요소의 존재여부를 반환하는 기능 
  @Override
  public boolean isEmpty() {
    return size == 0;
  }

  // clear() - 모든 요소를 삭제하는 기능 
  @Override
  public void clear() {

    // 모든 공간을 null 처리한다. 
    // array의 크기를 초기값으로 초기화 하지 않는 이유는 
    // 사용한 공간만큼 또 사용할 가능성이 크기 때문이다. 
    for (int i = 0; i < size; i++) {
      array[i] = null;
    } 

    size = 0;
    resize();
  }
  
}