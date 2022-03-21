package java_ps.crack_algo.dynamic;

public class LeetCode70 {

    public static void main(String[] args) {
        LeetCode70 foo = new LeetCode70();
        foo.climbStairs(3);
    }

    public int climbStairs(int n) { // 배열을 사용한 방식
        if(n == 1) return n;

        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;

        for(int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }

    public int climbStairs2(int n) { // 배열 없이
        if(n == 1) return n;

        int oneStep = 1;
        int twoStep = 2;

        for(int i = 3; i <= n; i++) {
            int temp = twoStep;
            twoStep = oneStep + twoStep; // n = 3일 때, 경우의 수
            oneStep = temp;// n번째 스텝을 구하기 위해서 n - 2번째를 기준으로 바꿈
            // ex) 4번째 계단 = 3번째 계단 + 2번째 계단
        }
        return twoStep;
    }
}
