package java_algorithm.java_ds;

public class Impl {
  public static void main(String[] args) {
    
    ArrayStack arrayStack = new ArrayStack(10);

    arrayStack.push(0);
    arrayStack.push(1);
    arrayStack.push(2);
    arrayStack.push(3);

    arrayStack.peek();
    arrayStack.pop();
    arrayStack.peek();

  }
  
}
