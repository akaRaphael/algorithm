# 1) 개선된(향상된) 프림 알고리즘이란?
# - 기존의 프림 알고리즘을 개선한 알고리즘으로, 
#   간선의 가중치를 중심이 아닌 노드를 중심으로 우선순위 큐를 적용하는 알고리즘이다.

# 2) 무엇이 개선 되었을까?
# - 기존의 프림 알고리즘은 간선의 갯수의 따라 while 반복문의 횟수가 정해졌다. => O(E log E)
# - 개선된 프림 알고리즘은 노드를 기반으로 우선순위 큐를 적용하기 때문에,
#   노드의 수에 따라서 반복문의 횟수가 정해진다. => O(E log V) 여기서 V는 Vertex를 의미한다.
# - 그래프는 간선의 갯수 > 노드의 갯수 이므로, 간선과 노드의 갯수 차이만큼 반복문의 실행횟수가 감소한다.
#   즉, 반복문의 횟수가 줄어드는만큼 시간복잡도가 향상된 것이다. 

# 3) 개선된 프림 알고리즘의 로직
# - Prim 알고리즘의 우선순위 큐를 사용하는 방법과 다익스트라 알고리즘의 inf값을 사용하는 방법이 함께 적용된다.
#   a. 초기화
#    - 노드에 key값을 부여한다.
#    - 시작노드는 0을, 나머지 노드는 infinite 값을 부여한다. (다익스트라에서 사용한 기법)
#    - 모든 key값은 우선순위 큐에 저장된다. 

#   b. 최소값 추출 
#    - key값이 가장 작은 정점을 순서대로 추출한다. (최초에는 시작노드가 추출된다. key = 0)
#    - 우선순위 큐에서 추출하기 때문에 pop으로 구현한다.
#    - 인접노드의 key값과 간선의 가중치를 비교한다. 
#      가중치가 인접노드의 key값보다 작으면 해당 인접노드의 key값을 간선의 가중치로 갱신한다.   
#      그 외의 경우는 스킵하며, 가장 작은 값을 가진 인접노드의 key값이 mst에 삽입된다. 

#   c. 위의 과정을 계속해서 반복한다. 

# 4) 개선된 프림 알고리즘 구현 특징
# - 우선순위 큐(최소 힙)를 사용한다.
# - 구현 복잡도를 줄이기 위해 heapdict 라이브러리를 사용한다. 
#   (설치 필요 => pip install HeapDict 및 왼쪽 하단의 VSCode python 인터프리터 확인할 것)

# 5) 개선된 프림 알고리즘 구현 


graph = {
  'A': {'B': 7, 'D': 5}, 'B': {'A': 7, 'D': 9, 'C': 8, 'E': 7}, 
  'C': {'B': 8, 'E': 5}, 'D': {'A': 5, 'B': 9, 'E': 7, 'F': 6}, 
  'E': {'B': 7, 'C': 5, 'D': 7, 'F': 8, 'G': 9}, 
  'F': {'D': 6, 'E': 8, 'G': 11}, 'G': {'E': 9, 'F': 11}
}

from heapdict import heapdict

def imp_prim(graph, start):
  mst = list()
  keys = heapdict()
  update_history = dict()
  total_weight = 0
  
  for node in graph.keys():
    keys[node] = float('inf')
    update_history[node] = None
  keys[start], update_history[start] = 0, start
  
  while keys:
    current_node, current_key = keys.popitem()
    mst.append([update_history[current_node], current_node, current_key])
    total_weight += current_key
    
    for adjacent, weight in graph[current_node].items():
      if adjacent in keys and weight < keys[adjacent]:
        keys[adjacent] = weight
        update_history[adjacent] = current_node
  return mst, total_weight

mst, total = imp_prim(graph, 'A')

print(mst)
print(total)
