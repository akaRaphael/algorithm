package java_ps.neetcode.arrayNhash;

import java.util.HashMap;
import java.util.Map;

public class LeetCode242 {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        Map<Character, Integer> map = new HashMap<>();
        char[] base = s.toCharArray();
        char[] target = t.toCharArray();

        for(char one : base) {
            map.put(one, map.getOrDefault(one, 0) + 1);
        }

        for(char one : target) {
            if(map.get(one) == null || map.get(one) <= 0) return false;
            map.put(one, map.get(one) - 1);
        }
        return true;
    }
}
