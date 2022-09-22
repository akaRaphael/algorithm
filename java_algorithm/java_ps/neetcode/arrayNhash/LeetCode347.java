package java_ps.neetcode.arrayNhash;

import java.util.*;

public class LeetCode347 {
    public int[] topKFrequent(int[] nums, int k) {
        List<Integer> candidate = new ArrayList<>();
        Map<Integer, Integer> map = new HashMap<>();

        for(int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        List<Map.Entry<Integer, Integer>> listEntry = new ArrayList<>(map.entrySet());
        Collections.sort(listEntry, new Comparator<Map.Entry<Integer, Integer>>() {
            @Override
            public int compare(Map.Entry<Integer, Integer> o1, Map.Entry<Integer, Integer> o2) {
                return o1.getValue().compareTo(o2.getValue());
            }
        });

        for(Map.Entry<Integer, Integer> entry : listEntry) {
            candidate.add(entry.getKey());
            if(candidate.size() == k) break;
        }
        return candidate.stream().mapToInt(o -> o).toArray();
    }
}
