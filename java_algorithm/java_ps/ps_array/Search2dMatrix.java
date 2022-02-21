package java_algorithm.java_ps.ps_array;

import java.util.Arrays;
import java.util.stream.IntStream;

public class Search2dMatrix {

  public static void main(String[] args) {
    
    int[][] matrix = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
    int target = 3;

    Search2dMatrix foo = new Search2dMatrix();
    System.out.println(foo.searchMatrix(matrix, target));
    
  }

  // 내가 생각한 해결방법 
  // - 각 행의 가장 끝 요소가 각 행에서 가장 큰 숫자임을 이용
  public boolean searchMatrix(int[][] matrix, int target) {

    int len = matrix.length;
    int size = matrix[0].length;

    for(int i = 0; i < len; i++) {
      if(matrix[i][size - 1] >= target) {
        int[] array = matrix[i];
        return IntStream.of(array).anyMatch(x -> x == target);
      }
    }
    return false;
  }

  // 이진 탐색을 이용한 풀이 => 속도 0ms (100%)
  public boolean searchMatrix2(int[][] matrix, int target) {
    int x = 0;
    int y = 0;
    
    while(x < matrix.length && y < matrix[0].length){
        if(matrix[x][y] == target)
          return true;
        
        else if(target > matrix[x][matrix[0].length-1])
            x++;
        
        else
            y++;
        
    }
    return false;
  } 
}
