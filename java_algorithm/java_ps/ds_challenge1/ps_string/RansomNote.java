package java_ps.ds_challenge1.ps_string;


public class RansomNote {
  public static void main(String[] args) {
    
    String ransomNote = "aa";
    String magazine = "ab";

    RansomNote foo = new RansomNote();
    foo.canConstruct(ransomNote, magazine);
    
  }
  
  public boolean canConstruct(String ransomNote, String magazine) {
    
    // magazine을 이용하여 ransomeNote를 만들수 있냐 
    int[] alphabet = new int[26];

    for(int i = 0; i < ransomNote.length(); i++) {
      alphabet[ransomNote.charAt(i) - 'a'] ++;
      System.out.println(ransomNote.charAt(i) - 'a'); 
    }

    for(int i = 0; i < magazine.length(); i++) {
      alphabet[magazine.charAt(i) - 'a'] --;
    }

    for (int i : alphabet) {
      if (i > 0) {
        return false;
      }
    }

    return true;
  }
}
