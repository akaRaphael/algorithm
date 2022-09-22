package java_ps.neetcode.arrayNhash;

import java.util.*;

public class LeetCode49 {
    public List<List<String>> groupAnagrams(String[] strs) {

        List<List<String>> result = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();

        for(String str : strs) {
            char[] arr = str.toCharArray();
            Arrays.sort(arr);
            String temp = new String(arr);
            if(map.containsKey(temp)) {
                map.get(temp).add(str);
            }
            else {
                List<String> candidate = new ArrayList<>();
                candidate.add(str);
                map.put(temp, candidate);
            }
        }
        for(String s : map.keySet()) {
            result.add(map.get(s));
        }
        return result;
    }
}
