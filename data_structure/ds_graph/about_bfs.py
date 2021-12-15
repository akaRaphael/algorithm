# 1) BFS(Breadth First Search)란?
# - 같은 레벨의 Vertex를 우선적으로 탐색하는 방법 
# - 왼쪽 또는 오른쪽 vertex를 기준으로 같은 level에 존재하는 vertex를 우선적으로 탐색한다.

# 2) BFS의 동작방식 
# - BFS를 구현하기 위해서는 2가지 Queue가 요구된다.
#  a. need-visit Queue: 방문이 필요한 노드 정보를 가진 Queue
#  b. visited Queue: 방문한 Vertex의 방문 순서를 가진 Queue 

# 3) BFS 구현 
# a. dict를 이용한 그래프 구현 
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

def bfs(graph, start_vertex):
  visited = list()
  need_visit = list()
  need_visit.append(start_vertex)
  
  while need_visit:
    vertex = need_visit.pop(0)
    
    if vertex not in visited:
      visited.append(vertex)
      need_visit.extend(graph[vertex])
      print(need_visit)
      
  return visited

print(bfs(graph, 'A')) 
  
