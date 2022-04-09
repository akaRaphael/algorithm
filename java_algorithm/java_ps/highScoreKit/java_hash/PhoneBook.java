package java_ps.highScoreKit.java_hash;

import java.util.Arrays;
import java.util.HashMap;

public class PhoneBook {

    public boolean phoneBook(String[] phone_book) {
        boolean answer = true;
        HashMap<String, Integer> map = new HashMap<>();

        Arrays.sort(phone_book); // 시간 초과 나지 않기 위해서 정렬 후 찾기

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
