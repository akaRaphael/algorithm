# 1) 다익스라 알고리즘이란?
#  - 최단거리 알고리즘 중 하나로, 단일출발 케이스를 구하는 알고리즘  
#  - 우선순위 큐(min-heap)를 사용하여 구현한다. 
#  - 가중치를 사용하기에 동일한 목적지의 가중치 합이 더 큰 경로가 나오면 계산을 스킵한다.
#  - 그러므로, 최단경로를 우선적으로 계산한다는 것이 장점이다. 

import heapq

graph = {
  'A':{'B':8, 'C':1, 'D':2},
  'B':{}, 'C':{'B':5, 'D':2},
  'D':{'E':3, 'F':5},
  'E':{'F':1},
  'F':{'A':5}
}

def dijikstra(graph, start):
  distances = {node:float('inf') for node in graph}
  distances[start] = 0
  queue = []
  heapq.heappush(queue, [distances[start], start])
  
  while queue:
    current_distance, current_node = heapq.heappop(queue)
    
    if distances[current_node] < current_distance:
      continue
    
    for adjacent, weight in graph[current_node].items():
      distance = current_distance + weight
      
      if distance < distances[adjacent]:
        distances[adjacent] = distance
        heapq.heappush(queue, [distance, adjacent])
  return distances
        
print(dijikstra(graph, 'A'))