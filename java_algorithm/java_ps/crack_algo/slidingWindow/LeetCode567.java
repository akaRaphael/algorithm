package java_ps.crack_algo.slidingWindow;

import java.util.HashMap;
import java.util.HashSet;

public class LeetCode567 {

    public boolean checkInclusion(String s1, String s2) {
        HashMap<Character, Integer> map1 = new HashMap<>();

        for(char c: s1.toCharArray()) {
            map1.put(c, map1.getOrDefault(c, 0) + 1);
        }

        HashMap<Character, Integer> map2 = new HashMap<>();
        int start = 0;

        for(int end = 0; end < s2.length(); end++) {
            char c = s2.charAt(end);
            map2.put(c, map2.getOrDefault(c, 0) + 1);

            if(end + 1 >= s1.length()) {
                if(map1.equals(map2)) {
                    return true;
                }

                char leftChar = s2.charAt(start++);
                map2.put(leftChar, map2.get(leftChar) - 1);
                if(map2.get(leftChar) == 0) {
                    map2.remove(leftChar, 0);
                }
            }
        }
        return false;
    }
}
