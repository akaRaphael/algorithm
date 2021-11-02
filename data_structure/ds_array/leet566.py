# 566. Reshape the Matrix

from typing import List
class Solution:
  def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    originalR = len(mat)
    originalC = len(mat[0])
    if originalR == r or originalC == c:
        return mat
    elif originalR * originalC != r * c:
        return mat

    # Valid at this point
    result = []
    for i in range(r * c):
        if not (i % c):
            result.append([])
        newItem = mat[i // originalC][i % originalC]
        result[-1].append(newItem)
    return result

foo = Solution()
print(foo.matrixReshape(mat = [[1,2,3,4]], r = 2, c = 2))