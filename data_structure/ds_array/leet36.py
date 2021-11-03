# 36. Valid Sudoku

from typing import List

class Solution:
  def getBoxIdx(self, i, j):
    return (i//3)*3 + (j // 3)

  def isValidSudoku(self, board: List[List[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i, row in enumerate(board):
      for j, num in enumerate(row):
        if num.isdigit():
          # check for duplicates in row
          if num in rows[i]:
              return False
          rows[i].add(num)

          # check for duplicates in column
          if num in cols[j]:
              return False
          cols[j].add(num)

          # check for duplicates in sub-box
          boxIdx = self.getBoxIdx(i, j)
          if num in boxes[boxIdx]:
              return False
          boxes[boxIdx].add(num)
    return True

foo = Solution()
print(foo.isValidSudoku(board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))