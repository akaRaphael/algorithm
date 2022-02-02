package java_algorithm.java_ds;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;

public class arrayList {
  public static void main(String[] args) {
    
    // 1. ArrayList의 특징 
    // - 배열(Array)과 동일한 특성을 가진다. 
    // - 다만, 크기가 가변적인 선형 리스트다.  
    
    // 2. ArrayList 사용방법 

    // a) 선언 
    ArrayList arrayList = new ArrayList<>(); //타입을 설정하지 않으면 object로 선언된다.
    ArrayList<Integer> arrayList2 = new ArrayList<>(); // Integer 타입
    ArrayList<String> arrayList3 = new ArrayList<>(); // String 타입 

    ArrayList<Student> studentList = new ArrayList<>(); // 클래스를 만들어서 타입지정 가능 

    ArrayList<Integer> arrayList4 = new ArrayList<>(10); // 선언 및 크기 설정, 길이 10 
    ArrayList<Integer> arrayList5 = new ArrayList<>(Arrays.asList(1, 2, 3)); // 선언 및 초기값 설정 

    // b) 값 추가 
    arrayList2.add(1);
    arrayList2.add(2);
    arrayList2.add(3);
    arrayList2.add(null); // null 값을 담을 수 있다.
    arrayList2.add(0, 0); // add(index, value) 형식으로 추가 가능 
  
    Student student = new Student("일이삼", 123);
    studentList.add(student);
    studentList.add(new Student("사오육", 456));

    // c) 값 삭제
    arrayList2.remove(0); // remove(index) 형식으로 삭제 
    arrayList2.clear(); // 모든 원소 삭제 

    // d) 크기 출력 
    arrayList2.add(1);
    arrayList2.add(2);
    arrayList2.add(3);
    System.out.println("arrayList2.size = " + arrayList2.size());

    // e) 값 검색
    System.out.println("arrayList2.contains(1) = " + arrayList2.contains(1)); // contains(value)형식, 값의 존재여부를 반환(boolean) 
    System.out.println("arrayList2.indexOf(3) = " + arrayList2.indexOf(3)); // indexOf(value)형식, 값의 index를 반환 

    // f) 값 출력 - for문 
    for (Integer num : arrayList2) {
      System.out.println(num);
    }

    for (Student member : studentList) {
      System.out.println("이름: " + member.getName() + " 나이: " + member.getAge());
    }

    
    // g) 값 출력 - iterator 선언 
    Iterator iter = arrayList2.iterator(); // Iterator 선언

    while(iter.hasNext()) { // 다음 값의 존재여부 
      System.out.println(iter.next());
    }

  }

}

class Student {
  private String name;
  private int age;

  public Student(String name, int age) {
    this.name = name;
    this.age = age;
  }

  public int getAge() {
    return age;
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public void setAge(int age) {
    this.age = age;
  }

}