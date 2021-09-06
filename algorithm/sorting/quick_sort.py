# Quick Sort

# 1) Quick Sort 개념
#  - Quick Select와 마찬가지로 파티셔닝(partitioning)을 이용한 알고리즘이다.
#  - Quick Sort는 Quick Select와 다르게 배열을 반환한다. 

# 2) Quick Sort 시간복잡도 
#   - Best Case의 경우 O(n log n)
#   - Worst Case의 경우 O(n^2)
#   - Average Case의 경우 O(n log n)

# 3) Quick Sort의 Stability
#   - unstable 

# 4) Quick Sort 코드구현
from typing import List
import random

def quick_sort(case:List[int], begin_idx:int, last_idx:int) -> List[int]:
  length = last_idx - begin_idx + 1
  if length <= 1:
    return case
  
  pivot_idx = random.randrange(begin_idx, last_idx + 1)
  case[pivot_idx], case[last_idx] = case[last_idx], case[pivot_idx]
  left_idx = 0
  right_idx = last_idx - 1
  pivot = case[last_idx]

  while left_idx <= right_idx:
    if case[left_idx] <= pivot:
      left_idx += 1
      continue

    if case[right_idx] > pivot:
      right_idx -= 1
      continue

    if pivot < case[left_idx] and pivot >= case[right_idx]:
      case[left_idx], case[right_idx] = case[right_idx], case[left_idx]
      continue
  case[left_idx], case[last_idx] = case[last_idx], case[left_idx]

  # pivot의 우측 파티션을 대상으로 quick sort 적용
  quick_sort(case = case, begin_idx = left_idx + 1, last_idx = last_idx) 

  # pivot의 좌측 파티션을 대상으로 quick sort 적용
  quick_sort(case = case, begin_idx = begin_idx, last_idx = left_idx - 1) 

  return case

case = [5, 7, 9, 3, 1, 5, 5, 2, 4]
quick_sort(case = case, begin_idx = 0, last_idx = len(case) - 1)
print(case)
