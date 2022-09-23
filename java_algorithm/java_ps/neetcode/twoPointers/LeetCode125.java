package java_ps.neetcode.twoPointers;


public class LeetCode125 {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();
        String base = s.toLowerCase();

        for(int i = 0; i < base.length(); i++) {
            if(Character.isLetter(base.charAt(i)) || Character.isDigit(base.charAt(i))) {
                sb.append(base.charAt(i));
            }
        }

        String str = sb.toString();
        String reverse = sb.reverse().toString();

        return str.equals(reverse);
    }
}
