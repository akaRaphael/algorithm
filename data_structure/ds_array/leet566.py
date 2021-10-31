# 566. Reshape the Matrix

from typing import List

# def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:

mat = [[1,2],[3,4]]
group = []
result = []
r = 2
c = 2

for i in range(len(mat)):
  for j in range(len(mat[i])):
    if r == 1:
        group.append(mat[i][j])
    
    elif len(group) // r == 0:
      group.append(mat[i][j])

    else:
      result.append(group)
      group = []
        
    if len(group) == c:
        result.append(group)
        group = []
    
print(result)
