# Heap Sort

# 1) Heap Sort의 개념
#   - Heap은 완전이진트리로 구성된 자료구조다. 
#   - 완전이진트리란 왼쪽을 우선적으로 채우는, 왼쪽의 트리가 전부 채워진 이진트리를 말한다.
#   - Heap은 max Heap(최대 힙)과 min Heap(최소 힙), 두가지로 구분된다. 
#      - max Heap은 루트노드에 항상 최대값의 요소가 위치한다. 
#      - min Heap은 루트노드에 항상 최소값의 요소가 위치한다. 
#   - 파이썬은 heapq 라이브러리를 통해 heap을 구현할 수 있는데, min Heap만을 지원한다. 

# 3) heapify가 동작하는 방식

# 3) Heap Sort 구현

from typing import List
import heapq

# 최대 힙을 이용해 오름차순으로 정렬하라. 
def heap_sort(case:List[int]) -> List[int]:
  # min Heap을 max Heap으로 만드는 과정 

  case = [-1 * n for n in case]
  heapq.heapify(case)

  sorted = [0] * len(case)

  for i in range(len(case) - 1, -1, -1):
    largest = -1 * heapq.heappop(case)
    sorted[i] = largest

  return sorted

print(heap_sort(case = [3, 5, 7, 9, 4, 2]))