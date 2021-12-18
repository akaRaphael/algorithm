# 1) 크루스칼 알고리즘이란?
# - 최소 가중치의 합을 가지는 경로를 가진 신장트리(MST)를 만드는 알고리즘 
# - 사이클 유무를 판단하기 위해서 Union-Find 알고리즘을 내부 로직으로 사용한다.

# 2) 크루스칼 알고리즘의 연산과정 
# a. 신장트리 내부의 각 노드를 개별 집합화 한다.
# b. 모든 간선의 가중치를 오름차순으로 정리한다.
# c. Union-Find 알고리즘을 사용하여 합쳐진 트리의 사이클 유무를 확인한다. 
# d. 모든 노드가 연결되면서 최소 가중치를 가진 경로가 생성될 때까지 위의 과정을 반복한다.

# 3) 크루스칼 알고리즘의 동작과정 
# a. 하나의 노드를 기점으로 최소 가중치를 갖는 인접노드와 부분집합 A를 형성한다. 
#     => 부분집합 형성시 Union Find 수행 
# b. 동일한 방법으로 부분집합 A에 포함되지 않는 노드로 구성된 부분집합 B를 형성한다.
#     => 부분집합 형성시 Union Find 수행 
# c. 부분집합 A와 B를 합치기 위해 Union Find를 수행한다.
# d. 위의 과정을 반복하며 MST를 찾는다. 

# 3) 크루스칼 알고리즘의 시간복잡도
# - 크루스칼의 시간복잡도는 O(E log E)이다.
# - 그 이유는 다음과 같다.
#   a. 모든 노드를 개별 집합화 한다. => O(V)
#   b. 간선의 가중치를 오름차순으로 정렬한다. => O(E log E)
#   c. 각 부분집합의 사이클을 확인하고 합친다 => O(1) == Union-Find의 시간복잡도  
# - Big O Notation은 최대 시간복잡도를 기준으로 하므로 O(E log E)만큼의 시간을 소요한다.

# 4) 크루스칼 알고리즘 구현 
graph = {
  'nodes':['A', 'B', 'C', 'D', 'E', 'F', 'G'], 
  'edges':[
    (7, 'A', 'B'), (5, 'A', 'D'), 
    (7, 'B', 'A'), (8, 'B', 'C'), 
    (9, 'B', 'D'), (7, 'B', 'E'), 
    (8, 'C', 'B'), (5, 'C', 'E'), 
    (5, 'D', 'A'), (9, 'D', 'B'), 
    (7, 'D', 'E'), (6, 'D', 'F'), 
    (7, 'E', 'B'), (5, 'E', 'C'), 
    (7, 'E', 'D'), (8, 'E', 'F'), 
    (9, 'E', 'G'), (6, 'F', 'D'), 
    (8, 'F', 'E'), (11, 'F', 'G'), 
    (9, 'G', 'E'), (11, 'G', 'F') 
  ]
}

parent = dict() # 루트 노드 정보를 저장
rank = dict() # 각 부분집합의 rank를 저장

def kruskal(graph):
  mst = list()
  
  for node in graph['nodes']:
    make_set(node) # 각 노드를 개별 집합화 
    
  edges = graph['edges']
  edges.sort() # 간선 오름차순 정리 
  
  for edge in edges:
    # ex) edge = (11, A, B) => weight = 11, node_v = A, node_u = B
    weight, node_v, node_u = edge
    
    if find(node_v) != find(node_u):
      union(node_v, node_u)
      mst.append(edge)
      
  return mst

def make_set(node):
  parent[node] = node
  rank[node] = 0
  
def find(node):
  if parent[node] != node:
    parent[node] = find(parent[node]) # 재귀적으로 루트를 탐색 
  
  return parent[node]

def union(node_v, node_u): # Union By Rank 기법을 사용 
  root1 = find(node_v)
  root2 = find(node_u)
  
  if rank[root1] > rank[root2]:
    parent[root2] = root1
  else:
    parent[root1] = root2
    if rank[root1] == rank[root2]:
      rank[root2] += 1

print(kruskal(graph))
    
  