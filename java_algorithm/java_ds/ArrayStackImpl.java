package java_algorithm.java_ds;

public class ArrayStackImpl {

    // 배열로 스택 구현하기 

    int top;
    int size;
    int[] stack;

    public ArrayStackImpl(int size) {
        this.size = size;
        stack = new int[size];
        top = -1;
    }

    public void push(int item) {
        stack[++top] = item;
        System.out.println("Push = " + stack[top]);
    }

    public void pop() {
        System.out.println("Pop = " + stack[top]);
        int pop = stack[top];
        stack[top--] = 0;
    }

    public void peek() {
        System.out.println("Peek = " + stack[top]);
    }
    
}