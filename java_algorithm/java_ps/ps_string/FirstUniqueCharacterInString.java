import java.util.HashMap;

public class FirstUniqueCharacterInString {
  public static void main(String[] args) {
  }

  public int firstUniqChar(String s) { // 내가 작성한 코드 
    HashMap<Character, Integer> charMap = new HashMap<>();
    int len = s.length();

    for (int i = 0; i < len; i++) {
      charMap.put(s.charAt(i) , charMap.getOrDefault(s.charAt(i), 0) + 1);
      // 아래의 코드를 한줄로 작성한게 위의 코드다. 
      // char current = s.charAt(i);
      // if(charMap.containsKey(current)) {
      //   charMap.put(current, charMap.get(current) + 1);
      // } else {
      //   charMap.put(current, 1);
      // }
    }

    for(int i = 0; i < len; i++) {
      char key = s.charAt(i);
      if(charMap.get(key) == 1) {
        return i;
      }
    }

    return -1;
  }
}
