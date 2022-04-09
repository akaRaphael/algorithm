package java_ps.highScoreKit.java_hash;

import java.util.HashMap;

public class Programmers42577 {

    public boolean phoneBook(String[] phone_book) {
        boolean answer = true;
        HashMap<String, Integer> map = new HashMap<>();

        for(int i = 0; i < phone_book.length; i++) {
            map.put(phone_book[i], i);
        }

        for(int i = 0; i < phone_book.length; i++) {
            for(int j = 0; j < phone_book[i].length(); j++) {
                if(map.containsKey(phone_book[i].substring(0, j))) {
                    return false;
                }
            }
        }
        return answer;
    }
}
