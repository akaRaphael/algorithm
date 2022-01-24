# 1) DFS(Depth First Search)란?
#  - 한 Vertex의 자식노드를 먼저 탐색하는 방법 
#  - 왼쪽 또는 오른쪽 vertex를 기준으로 자식노드를 타고 끝까지 탐색한다. 
#  - 하나의 Vertex 탐색이 끝나면, 탐색을 시작한 level로 돌아와 탐색하지 않은 형제 vertex를 탐색한다.

# 2) DFS 동작방식의 의해 
# - DFS 알고리즘은 Stack과 Queue를 이용하여 구현할 수 있다.
# - need_visit Stack과 visited Queue를 사용한다. 
# - Stack의 LIFO 특성으로 인해, need_visit Stack에서 꺼내오는 데이터는 가장 최근에 삽입된 데이터다.

# 3) DFS 구현
#          a
#     b        c 
#   d        g h i
#   e f          j
graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def dfs(graph, start_vertex):
  visited_q = list()
  need_visit_stack = list()
  need_visit_stack.append(start_vertex)
  
  while need_visit_stack:
    vertex = need_visit_stack.pop()
    
    if vertex not in visited_q:
      visited_q.append(vertex)
      need_visit_stack.extend(graph[vertex])
      
  return visited_q

print(dfs(graph, 'A'))

# 4) DFS 시간복잡도 => O(V + A) 
# - BFS와 동일하게 need_visit Stack의 길이에 따라 시간복잡도가 달라진다.
# - 그러므로 Vertex와 Arc의 수에 의해 시간복잡도가 결정된다. 
# - 이와같은 이유로 DFS의 시간복잡도는 O(V + A)를 갖는다. 


# 5) DFS 구현 연습 
graph2 = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9

def dfs2(graph, v, visited):
  visited[v] = True
  print(v, end = '')
  
  for i in graph[v]: 
    if not visited[i]:
      dfs2(graph2, i, visited)
    
dfs2(graph2, 1, visited)