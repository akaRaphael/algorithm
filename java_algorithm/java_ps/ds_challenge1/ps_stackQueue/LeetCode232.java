package java_ps.ds_challenge1.ps_stackQueue;

import java.util.Stack;

public class LeetCode232 {

    static class MyQueue { // Stack으로 구현
        Stack<Integer> inputStack;
        Stack<Integer> outputStack;

        public MyQueue() {
            inputStack = new Stack<>();
            outputStack = new Stack<>();
        }

        public void push(int x) {
            inputStack.push(x);
        }

        public int pop() {
            while(!inputStack.isEmpty()) {
                    outputStack.push(inputStack.pop());
            }

            int result = outputStack.pop();

            while(!outputStack.isEmpty()) {
                inputStack.push(outputStack.pop());
            }

            return result;
        }

        public int peek() {

            if(inputStack.isEmpty()) {
                return -1;
            }

            while(!inputStack.isEmpty()) {
                outputStack.push(inputStack.pop());
            }

            int result = outputStack.peek();

            while(!outputStack.isEmpty()) {
                inputStack.push(outputStack.pop());
            }

            return result;
        }

        public boolean empty() {
            return inputStack.isEmpty();
        }
    }
}
