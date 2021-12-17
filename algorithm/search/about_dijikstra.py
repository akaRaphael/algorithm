# 다익스라 알고리즘이란?
#  - 최단거리 알고리즘 중 하나로, 단일출발 케이스를 구하는 알고리즘  
#  - 우선순위 큐(min-heap)를 사용하여 구현한다. 

import heapq

graph = {
  'A':{'B':8, 'C':1, 'D':2},
  'B':{}, 'C':{'B':5, 'D':2},
  'D':{'E':3, 'F':5},
  'E':{'F':1},
  'F':{'A':5}
}

def dijikstra(graph, start):
  distances = {node:float('inf') for node in graph} #모든 노드의 가중치를 무한(int)으로 설정한 딕셔너리 생성 
  distances[start] = 0 # 시작 노드의 거리
  pr_queue = [] # 우선순위 큐 생성
  
  heapq.heappush(pr_queue, [distances[start], start])
  
  while pr_queue:
    current_distance, current_node = heapq.heappop(pr_queue)
    if distances[current_node] < current_distance:
      continue
    
    for adjacent, weight in graph[current_node].items():
      cal_distance = current_distance + weight
      if cal_distance < distances[adjacent]:
        distances[adjacent] = cal_distance
        heapq.heappush(pr_queue, [cal_distance, adjacent])  
  
  return distances

print(dijikstra(graph, 'A'))


  