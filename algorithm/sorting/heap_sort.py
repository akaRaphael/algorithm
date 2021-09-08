# Heap Sort

# 1) Heap Sort의 개념
#   - Heap은 완전이진트리로 구성된 자료구조다. 
#   - 완전이진트리란 왼쪽을 우선적으로 채우는, 왼쪽의 트리가 전부 채워진 이진트리를 말한다.
#   - Heap은 max Heap(최대 힙)과 min Heap(최소 힙), 두가지로 구분된다. 
#      - max Heap은 루트노드에 항상 최대값의 요소가 위치한다. 
#      - min Heap은 루트노드에 항상 최소값의 요소가 위치한다. 
#   - 파이썬은 heapq 라이브러리를 통해 heap을 구현할 수 있는데, min Heap만을 지원한다. 

# 2) heapify가 동작하는 방식
#    - heapify 함수 클릭해서 읽어보기 

# 3) Heap Sort 구현

from typing import List
import heapq

# 최대 힙을 이용해 오름차순으로 정렬하라. 
def heap_sort(case:List[int]) -> List[int]:

  # min Heap을 max Heap으로 만드는 과정 
  case = [-1 * n for n in case] # 1) 배열의 모든 요소에 -1을 곱한다
  heapq.heapify(case) # 2) min Heap을 만든다. 

  sorted = [0] * len(case) # [0, 0, 0, 0, 0, 0]

  for i in range(len(case) - 1, -1, -1):
  # 위에서 모든 요소에 -1을 곱한 이유는 이 과정을 위해서다. 
  # min Heap에서 가장 큰 수를 제일 먼저 뽑기 위해서는 음수로 변환시킨 것이다. 
  
    largest = -1 * heapq.heappop(case) 
    sorted[i] = largest

  return sorted

print(heap_sort(case = [3, 5, 7, 9, 4, 2]))


# 4) Min Heap으로 Max Heap 만들기 
import heapq

nums = [4, 1, 7, 3, 8, 5]
heap = []
max_heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  max_heap.append((heapq.heappop(heap)[1]))  # index 1

print(max_heap)