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
  visited = list()
  need_visit = list()
  need_visit.append(start_vertex)
  
  while need_visit:
    vertex = need_visit.pop()
    if vertex not in visited:
      visited.append(vertex)
      need_visit.extend(graph[vertex])
      
  return visited

print(dfs(graph, 'A'))
