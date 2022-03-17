package java_ps.crack_algo.search;

public class LeetCode542 {

    public int[][] updateMatrix(int[][] mat) {

        int[][] result = new int[mat.length][mat[0].length];
        int maxDistance = (mat.length - 1) + (mat[0].length - 1);

        // case1. 위에서 아래로, 왼쪽에서 오른쪽으로 탐색
        for(int i = 0; i < mat.length; i++) {
            for(int j = 0; j < mat[0].length; j++) {
                if(mat[i][j] != 0) {
                    int upperCell = (i > 0) ? result[i - 1][j] : maxDistance;
                    int leftCell = (j > 0) ? result[i][j - 1] : maxDistance;
                    result[i][j] = Math.min(upperCell, leftCell) + 1;
                }
            }
        }

        // case2. 아래에서 위로, 오른쪽에서 왼쪽으로 탐색
        for(int i = mat.length - 1; i >= 0; i--) {
            for(int j = mat[0].length - 1; j >= 0; j--) {
                if(mat[i][j] != 0) {
                    int bottomCell = (i < mat.length - 1) ? result[i + 1][j] : maxDistance;
                    int rightCell = (j < mat[0].length - 1) ? result[i][j + 1] : maxDistance;
                    result[i][j] = Math.min(Math.min(bottomCell, rightCell) + 1, result[i][j]);
                }
            }
        }
        return result;
    }
}
