package java_ps.crack_algo.twoPointers;


public class LeetCode557 {

    public String reverseWords(String s) {

        String[] array = s.split(" ");
        StringBuilder result = new StringBuilder();

        for(String word : array) {
            StringBuilder sb = new StringBuilder(word);
            result.append(sb.reverse() + " ");
        }
        return result.toString().trim();
    }
}
