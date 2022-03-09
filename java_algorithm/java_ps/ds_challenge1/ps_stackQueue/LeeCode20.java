package java_ps.ds_challenge1.ps_stackQueue;

import java.util.Stack;

public class LeeCode20 {

    public boolean isValid(String s) {
        // 괄호의 짝이 맞는지 확인할 것
        // 괄호가 닫히는 순서를 확인할 것

        int len = s.length();
        int result = 0;
        Stack<Character> stack = new Stack<>();

        for(int i = 0; i < len; i++) {
            char data = s.charAt(i);

            if(data == '(' || data == '{' || data == '[') {
                result += 1;
                stack.push(data);
            }
            else {
                result -= 1;

                if(stack.empty()) {
                    return false;
                }
                else {
                    char last = stack.pop();

                    if(data == ')' && last != '(') {
                        return false;
                    }
                    if(data == '}' && last != '{') {
                        return false;
                    }
                    if(data == ']' && last != '[') {
                        return false;
                    }
                }
            }
        }
        return result == 0;
    }
}
