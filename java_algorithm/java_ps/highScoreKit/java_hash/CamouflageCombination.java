package java_ps.highScoreKit.java_hash;

import java.util.HashMap;
import java.util.Iterator;

public class CamouflageCombination {

    public int camouflage(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> map = new HashMap<>();

        for(String[] items : clothes) {
            map.put(items[1], map.getOrDefault(items[1], 0) + 1);
        }

        Iterator<Integer> iter = map.values().iterator();

        while(iter.hasNext()) {
            answer *= iter.next().intValue() + 1;
        }

        return answer - 1;
    }
}
