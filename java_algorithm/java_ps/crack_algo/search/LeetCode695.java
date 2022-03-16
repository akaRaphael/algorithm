package java_ps.crack_algo.search;

public class LeetCode695 {


    public int maxAreaOfIsland(int[][] grid) {
        int maxArea = 0;
        int row = grid.length;
        int col = grid[0].length;

        for(int i = 0; i < row; i++) {
            for(int j = 0; j < col; j++) {
                maxArea = Math.max(maxArea, findLand(i, j, grid));
            }
        }
        return maxArea;
    }

    public int findLand(int row, int col, int[][] grid) {
        if(row < 0 || col < 0 || row >= grid.length || col >= grid[0].length || grid[row][col] == 0) {
            return 0;
        }

        grid[row][col] = 0; // 방문했던 위치를 체크하기 위함

        return (1 + findLand(row - 1, col, grid)
                + findLand(row + 1, col, grid)
                + findLand(row, col - 1, grid)
                + findLand(row, col + 1, grid));
    }
}
