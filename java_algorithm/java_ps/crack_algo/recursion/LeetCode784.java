package java_ps.crack_algo.recursion;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class LeetCode784 {

    public List<String> letterCasePermutation(String s) {
        List<String> result = new ArrayList<>();
        permute(result, s, 0);

        return result;
    }

    public void permute(List<String> result, String word, int start) {
        result.add(word);

        for(int i = start; i < word.length(); i++) {
            char[] wordArray = word.toCharArray();

            if(Character.isLetter(word.charAt(i))) {
                if(Character.isUpperCase(word.charAt(i))) {
                    wordArray[i] = Character.toLowerCase(word.charAt(i));
                    permute(result, String.valueOf(wordArray), i + 1);
                    // String.valueOf(char[] word) => CharArray를 String으로 반환함.
                }
                else {
                    wordArray[i] = Character.toUpperCase(word.charAt(i));
                    permute(result, String.valueOf(wordArray), i + 1);
                }
            }
        }
    }
}
