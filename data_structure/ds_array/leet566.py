# 566. Reshape the Matrix

from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        mat_row = len(mat)
        mat_col = len(mat[0])

        if mat_row == r and mat_col == c:
            return mat
        elif mat_row * mat_col != r * c:
            return mat
        
        result = []
        for i in range(r * c):
            if i % c == 0:
                result.append([])
            new_item = mat[i // mat_col][i % mat_col]
            result[-1].append(new_item)
        return result
        
foo = Solution()
print(foo.matrixReshape(mat = [[1,2,3,4]], r = 2, c = 2))