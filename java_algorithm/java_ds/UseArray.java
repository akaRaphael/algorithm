package java_algorithm.java_ds;

public class UseArray {
  public static void main(String[] args) {

    // 0. 자바 배열의 기본특징 
    // - 고정길이 
    // - 동일한 자료형의 데이터 
    // - 배열도 객체다. 

    // 1. Primitive 자료형의 배열 
    // a) 배열 참조변수만 선언 (크기, 초기값 없음) => 초기값 없어서 사용 못함 
    int[] arr; 
    int arr1[]; 
    
    // b) 배열 선언 및 크기, 초기값 할당을 순차적으로 해보자. 
    int[] arr2; // 배열 참조변수 선언 
    arr2 = new int[3]; // 배열 객체생성 및 크기 할당 => 초기값 설정 안하면 0이 deafult 
    
    // c) 배열 선언 및 크기와 초기값 할당 
    int[] arr3 = {1,2,3};
    int[] arr4 = new int[]{1,2,3};
    String[] week = {"월", "화", "수", "목", "금", "토", "일"};
    
    // d) 배열 선언 및 크기만 할당 
    int[] arr5 = new int[3];
    
    // 2. wrapper 클래스를 이용한 배열 
    Integer[] arr6; // 초기값 설정(초기화)이 안되어 사용할 수 없다. 
    Integer[] arr7 = {1,2,3};
    Integer[] arr8 = new Integer[3]; // 초기값 설정 안하면 null이 default 
    Integer[] arr9 = null;

    // 3. 배열 출력
    int[] array = {1,2,3};
    Integer[] array2 = {4,5,6};
    System.out.println(array); // I@76ccd017 출력함 
    System.out.println(arr7); // java.lang.Integer;@182decdb출력함 
    // => 배열을 직접 출력하면 배열 객체의 메모리 주소값이 출력된다. 
    // => 그러므로 반드시 for문을 사용하여 각 객체에 접근해야한다. 

    for (int i : array) {
      System.out.println(i);
    }

    for (int i : array2) {
      System.out.println(i);
    }


    // 4. Primitive vs Wrapper

    // a) Primitive  
    // - primitive는 Java의 기본 자료형을 말한다.
    // - 기본 자료형은 null 값을 가질 수 없으며, 각 자료형마다의 default 값이 존재한다. (int = 0) 
    
    // b) Wrapper 클래스 
    // - wrapper 클래스는 primitive 자료형을 객체로 만든 것이다. 
    // - wrapper 클래스는 default 값이 null이다. 
    // - wrapper 클래스로 생성된 객체는 당연히 해당 클래스에서 제공하는 메소드를 사용할 수 있다.
    

  }
}