package java_ps.ds_challenge1.ps_array;

public class ReshapetheMatrix {
  
  public static void main(String[] args) {

    int[][] mat = {{1,2},{3,4}}; 
    int r = 1;
    int c = 4;

    ReshapetheMatrix foo = new ReshapetheMatrix();

    foo.matrixReshape(mat, r, c);
    
  }

  public int[][] matrixReshape(int[][] mat, int r, int c) {

    int matRow = mat.length;
    int matCol = mat[0].length;

    if (matRow * matCol != r * c) {
      return mat;
    }

    int[][] result = new int[r][c];
    int resRow = 0;
    int resCol = 0;

    for (int i = 0; i < matRow; i++) {
      for (int j = 0; j < matCol; j++) {
        result[resRow][resCol] = mat[i][j];
        resCol++;

        if (resCol == c) {
          resCol = 0;
          resRow++;
        }
      }
    }
    return result;
  }
}
