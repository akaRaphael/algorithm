# 1) 프림(Prim's) 알고리즘이란?
# - 크루스칼 알고리즘과 함께 꼽히는 대표적인 최소신장트리 알고리즘
# - 인접노드의 간선 중에서 최소 가중치를 가진 간선을 선택하여 MST를 구하는 알고리즘

# 2) 프림 VS 크루스칼 알고리즘
# - 두 알고리즘 모두 탐욕 알고리즘을 기반으로 한다는 공통점을 갖는다.

#   a. 크루스칼 알고리즘
#    - 모든 간선을 가중치 기반으로 정렬하여 최소 가중치를 가진 간선만을 선택하여 MST를 구한다.
#    -  사이클의 유무를 판단하기 위해서 Union-Find 알고리즘을 사용한다. 

#   b. 프림 알고리즘 
#    - 인접한 노드의 간선 중 최소 가중치를 가진 간선을 선택하여 MST를 구하는 알고리즘 


# 3) 프림 알고리즘의 로직 
#   a. 연결된(선택된) 노드정보를 관리하기 위한 리스트를 사용한다. => 연결된 노드 리스트
#   b. 선택된 노드의 인접노드가 가진 간선정보를 관리하기 위한 리스트를 사용한다. => 인접한 간선 리스트
#   c. '인접한 간선 리스트'에서 최소 가중치를 가진 간선부터 추출한다.
#   d. 추출된 간선이 이미 '연결된 노드 리스트'에 존재한다면, 스킵한다. (사이클 방지)
#      만약, 존재하지 않는 간선이라면 MST에 저장 후 '인접한 간선 리스트'에서 삭제한다.
#   e. '인접한 간선 리스트'에 더이상의 데이터가 존재하지 않을 때까지 C와 D 과정을 반복한다. 

# 4) 프림 알고리즘의 구현 특징
# - '인접한 간선 리스트'는 Min-Heap(= 우선순위 큐)을 이용하여 구현한다.
# - collections.defaultdict() 또는 typing.DefaultDict()를 사용하여 비어있는 자료구조를 반환할 수 있도록 한다.

edges = [
  (7, 'A', 'B'), (5, 'A', 'D'),
  (8, 'B', 'C'), (9, 'B', 'D'),
  (7, 'B', 'E'), (5, 'C', 'E'),
  (7, 'D', 'E'), (6, 'D', 'F'),
  (8, 'E', 'F'), (9, 'E', 'G'),
  (11, 'F', 'G')
]

from collections import defaultdict
from heapq import *

def prim(start, edges):
  mst = list()
  adjacent_edges = defaultdict(list)
  
  for weight, node_from, node_to in edges:
    adjacent_edges[node_from].append((weight, node_from, node_to))
    adjacent_edges[node_to].append((weight, node_to, node_from))
    
  connected_nodes = set(start)
  candidate_list = adjacent_edges[start]
  heapify(candidate_list)
  
  while candidate_list:
    weight, node_from, node_to = heappop(candidate_list)
    
    if node_to not in connected_nodes:
      connected_nodes.add(node_to)
      mst.append((weight, node_from, node_to))
      
      for edge in adjacent_edges[node_to]:
        if edge[2] not in connected_nodes:
          heappush(candidate_list, edge)
  return mst