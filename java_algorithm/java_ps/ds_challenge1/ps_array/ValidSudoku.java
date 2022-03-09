package java_ps.ds_challenge1.ps_array;

import java.util.HashSet;

// 참고자료 - https://www.youtube.com/watch?v=Pl7mMcBm2b8

public class ValidSudoku { //https://leetcode.com/problems/valid-sudoku/

  public static void main(String[] args) {

    ValidSudoku foo = new ValidSudoku();
    char[][] board = new char[][]{{'5','3','.','.','7','.','.','.','.'}
    ,{'6','.','.','1','9','5','.','.','.'}
    ,{'.','9','8','.','.','.','.','6','.'}
    ,{'8','.','.','.','6','.','.','.','3'}
    ,{'4','.','.','8','.','3','.','.','1'}
    ,{'7','.','.','.','2','.','.','.','6'}
    ,{'.','6','.','.','.','.','2','8','.'}
    ,{'.','.','.','4','1','9','.','.','5'}
    ,{'.','.','.','.','8','.','.','7','9'}};

    System.out.println(foo.isValidSudoku(board));
  }

  public boolean isValidSudoku(char[][] board) {
    HashSet<String> checkSet = new HashSet<>();

    for(int i = 0; i < 9; i++) {
      for(int j = 0; j < 9; j++) {
        char current = board[i][j];
        if(current != '.') {
          if( !checkSet.add(current + "found in row " + i) ||
           !checkSet.add(current + "found in column " + j) ||
           !checkSet.add(current + "found in sub box " + i / 3 + " - " + j / 3)) return false;
        }
      }
    }
    return true;
  }
}
