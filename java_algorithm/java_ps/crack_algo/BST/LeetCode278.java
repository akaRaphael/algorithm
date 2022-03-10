package java_ps.crack_algo.BST;

public class LeetCode278 {

    public boolean isBadVersion(int n) {
        return true;
    }

    public int firstBadVersion(int n) {

        int left = 1;
        int right = n;

        while(left < right) {
            int mid = left + (right - left) / 2;
            if(isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
