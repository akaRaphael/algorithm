package java_ps.crack_algo.search;

public class LeetCode733 {

    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {

        if(image[sr][sc] == newColor) {
            return image;
        }

        changeColor(image, sr, sc, image[sr][sc], newColor);
        return image;
    }

    public void changeColor(int[][] image, int sr, int sc, int orgColor, int newColor) {
        if(sr < 0 || sc < 0 || sr >= image.length || sc >= image[0].length || image[sr][sc] != orgColor) {
            return;
        }

        image[sr][sc] = newColor;

        changeColor(image, sr - 1, sc, orgColor, newColor);
        changeColor(image, sr + 1, sc, orgColor, newColor);
        changeColor(image, sr, sc - 1, orgColor, newColor);
        changeColor(image, sr, sc + 1, orgColor, newColor);
    }
}
