package java_algorithm.java_ps.ps_string;

public class ValidAnagram {
  public static void main(String[] args) {

    String s = "a";
    String t = "ab";

    ValidAnagram foo = new ValidAnagram();
    foo.isAnagram(s, t);
  } 
  
  public boolean isAnagram(String s, String t) {

    int[] alphabet = new int[26];
    
    for(int i = 0; i < s.length(); i++) {
      alphabet[s.charAt(i) - 'a']++;
    }

    for(int i = 0; i < t.length(); i++) {
      alphabet[t.charAt(i) - 'a']--;
    }

    for (int i : alphabet) {
      if (i != 0) {
        return false;
      }
    }
    return true;
  }
}
