package java_ps.crack_algo.slidingWindow;

import java.util.HashMap;
import java.util.HashSet;

public class LeetCode3 {

    public static void main(String[] args) {

        LeetCode3 foo = new LeetCode3();
        foo.lengthOfLongestSubstring("dvdf");

    }

    public int lengthOfLongestSubstring(String s) {
        int prev = 0;
        int idx = 0;
        int max = 0;
        HashSet<Character> hashSet = new HashSet<>();

        while (idx < s.length()) {
            if (hashSet.contains(s.charAt(idx)) == false) {
                hashSet.add(s.charAt(idx));
                idx++;
                max = Math.max(max, hashSet.size());
            } else {
                hashSet.remove(s.charAt(prev));
                prev++;
            }
        }
        return max;
    }
}
