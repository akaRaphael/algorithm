package java_ps.highScoreKit.java_hash;

import java.util.HashMap;

public class Programmers42576 {

    public String inCompletedPlayer(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> map = new HashMap<>();

        for(String name : completion) {
            map.put(name, map.getOrDefault(name, 0) + 1);
        }

        for(String name : participant) {
            if(map.containsKey(name) && map.get(name) > 0) {
                map.put(name, map.get(name) - 1);
            }
            else {
                answer = name;
                break;
            }
        }
        return answer;
    }
}
