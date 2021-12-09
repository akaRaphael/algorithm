# 1) priority queue란?
# - 입력순서가 아닌라 우선순위를 기준으로 추출순서가 정해지는 Queue
# - 우선순위 큐는 연결리스트, 이진탐색트리, 힙으로 구현이 가능한데, 
# - 힙으로 구현한 우선순위 큐가 가장 효율이 우수하다. 

# 2) Heap 기본개념 
# - 이진트리를 기본으로 하는 자료구조
# - Max Heap = 가장 큰 값을 root로 유지하는 이진트리
# - Min Heap = 가장 작은 값을 root로 유지하는 이진트리 

# 3) 우선순위 큐 구현에 Heap을 사용하는 이유 
# - 앞서 우선순위 큐를 구현하는데 Heap이 가장 효율적이라고 했다.
# - 그 이유는 우선순위 큐가 우선순위를 기준으로 추출 순서를 결정하기 때문이다.
# - 우선순위가 높은 요소가 가장 먼저 추출되므로, 
#   우선순위가 가장 높은 요소를 쉽게 찾을 수 있어야 한다.
# - 이러한 특성을 가장 잘 살릴 수 있는 자료구조가 Max/Min Heap이다. 

# 4) 파이썬 queue 라이브러리를 이용한 구현 
# - 1이 최상위 우선순위다. 
from queue import PriorityQueue
pq = PriorityQueue(maxsize=10) # 최대크기 설정 가능
pq.put((3, "c"))
pq.put((2, "b"))
pq.put((4, "d"))
pq.put((1, "a"))
# print(pq.get())


# 5) 파이썬 heapq 라이브러리를 이용한 구현 
# - heapq 라이브러리는 min-heap을 기본으로 한다.
# - 그러므로 1이 최상위 우선순위가 된다.  
import heapq
arr = [(2, "b"), (5, "e"), (3, "c"), (1, "a"), (4, "d"), (2, "b")]
heapq.heapify(arr)
print(heapq.heappop(arr))


# 6) max-heap 구현
# - min heap의 가장 작은 값을 우선 추출하는 특성을 역이용 하는 방법 
# - 우선순위를 음수로 설정한다. 
max_heap = []
for i in range(10):
  heapq.heappush(max_heap, (-i, i))

while max_heap:
  print(heapq.heappop(max_heap)[1]) # 인덱스를 안붙이면 (1, 'a') 형태로 출력함. 